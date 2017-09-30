from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from core.models import ModelWithAuthor, ModelWithDates, User
from core.utils import Enum


class EventType(Enum):
    choices = ["post_published",
               "post_edited",
               "comment_created",
               "comment_edited",
               "liked_object",
               "subscribed_at"
               ]


def add_event_for_object(instance):
    event = Event(title=instance.get_title_for_event(), user=instance.author, object=instance)
    event.save()


def update_event_for_object(event, instance):
    event.title = instance.get_title_for_event()
    event.save()


# Create your models here.
class Event(ModelWithDates, ):
    title = models.TextField(null=False)
    user = models.ForeignKey(User)  # not author but user connected with this event
    type = models.IntegerField(null=False)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id', )
