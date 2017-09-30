from __future__ import unicode_literals
from core.models import *


# Create your models here.

class Comment(ModelWithAuthor, ModelWithDates, LikeAble):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id')
    edited_count = models.IntegerField(default=0)

    text = models.TextField()
    text_was = None


class CommentAble(models.Model):
    comments_count = models.IntegerField(default=0)

    class Meta:
        abstract = True
