from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from core.models import ModelWithAuthor, ModelWithDates, User


# class EventType(models.E)

# Create your models here.
class Event(ModelWithDates, ):
    title = models.TextField(null=False)
    user = models.ForeignKey(User)  # not author but user connected with this event

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id')
