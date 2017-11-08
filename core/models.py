from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.utils import Enum
from event.eventtype import EventType, EVENT_SUBSCRIPTION, EVENT_LIKE

RELATIONSHIP_FOLLOWING = 'subscribed on'
RELATIONSHIP_CANCEL_FOLLOWING = 'stopped subscription on'
RELATIONSHIP_BLOCKED = 'blocked'
RELATIONSHIP_CANCEL_BLOCKED = 'canceled block of'


class RelationshipEnum(Enum):
    choices = [RELATIONSHIP_FOLLOWING, RELATIONSHIP_CANCEL_FOLLOWING,
               RELATIONSHIP_BLOCKED, RELATIONSHIP_CANCEL_BLOCKED]


class ModelWithDates(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WatchableModel(models.Model):
    def get_event_type(self, created):
        raise NotImplementedError

    def get_title_for_event(self, eventtype):
        raise NotImplementedError

    def is_tracked(self):
        raise NotImplementedError

    def get_event_creator(self):
        try:
            return self.author
        except AttributeError:
            raise NotImplementedError

    class Meta:
        abstract = True


class User(AbstractUser):
    objects_count = models.IntegerField(default=0)
    relationships = models.ManyToManyField('self', related_name='related_to', symmetrical=False,
                                           through='Relationship')

    def add_relationship(self, user, status):
        if user.id == self.id:
            return
        for relation in Relationship.objects.filter(from_person=self, to_person=user):
            relation.delete()  # you cannot follow and block user in the same time
        relationship, created = Relationship.objects.get_or_create(
            from_person=self,
            to_person=user,
            status=status)
        return relationship

    def remove_relationship(self, person, status):
        Relationship.objects.filter(
            from_person=self,
            to_person=person,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_person=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_people__status=status,
            from_people__to_person=self)

    def get_following(self):
        return self.get_relationships(RelationshipEnum().get_id(RELATIONSHIP_FOLLOWING))

    def get_followers(self):
        return self.get_related_to(RelationshipEnum().get_id(RELATIONSHIP_FOLLOWING))

    def get_friends(self):
        following_id = RelationshipEnum().get_id(RELATIONSHIP_FOLLOWING)
        return self.relationships.filter(
            to_people__status=following_id,
            to_people__from_person=self,
            from_people__status=following_id,
            from_people__to_person=self)


class Relationship(WatchableModel, ModelWithDates):
    from_person = models.ForeignKey(User, related_name='from_people')
    to_person = models.ForeignKey(User, related_name='to_people')
    status = models.IntegerField(choices=RelationshipEnum().get_as_tuple())

    def get_event_creator(self):
        return self.from_person

    def get_event_type(self, created):
        return EVENT_SUBSCRIPTION

    def get_title_for_event(self, eventtype):
        return "User {0} {1} {2}".format(self.from_person.get_username(),
                                         RelationshipEnum().get_name(self.status),
                                         self.to_person.get_username())

    def is_tracked(self):
        return True
        # return RELATIONSHIP_FOLLOWING == RelationshipEnum().get_name(self.status)


class ModelWithAuthor(models.Model):
    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class Like(ModelWithDates, ModelWithAuthor, WatchableModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id')

    def get_event_type(self, created):
        return EVENT_LIKE

    def get_title_for_event(self, eventtype):
        return "User " + self.author.get_username() + " liked " + self.object.get_title_for_event(eventtype)

    def is_tracked(self):
        # TODO: add a condition when we create an event on this action
        return True


class LikeAble(models.Model):
    likes = GenericRelation(Like, object_id_field='object_id', content_type_field='content_type')
    likes_count = models.IntegerField(default=0)

    def get_title_for_like(self):
        raise NotImplementedError

    class Meta:
        abstract = True


class LikeAbleNotAbstract(LikeAble):
    class Meta:
        abstract = False
