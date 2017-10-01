from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from core.models import ModelWithAuthor, ModelWithDates, User
from event.eventtype import EventType


def add_event_for_object(instance, created):
    event_type = EventType().get_id(instance.get_event_type(created=created))
    event = Event(title=instance.get_title_for_event(eventtype=event_type),
                  type=event_type,
                  user=instance.author,
                  object=instance)
    event.save()


# Create your models here.
class Event(ModelWithDates, ):
    title = models.TextField(null=False)
    user = models.ForeignKey(User)  # not author but user connected with this event
    type = models.IntegerField(null=False)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id', )
