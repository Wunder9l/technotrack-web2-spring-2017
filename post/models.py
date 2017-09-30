from __future__ import unicode_literals

from comment.models import CommentAble
from core.models import *


# Create your models here.

class Post(ModelWithAuthor, ModelWithDates, LikeAble, CommentAble, WatchableModel):
    title = models.CharField(max_length=255)
