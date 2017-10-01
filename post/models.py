from __future__ import unicode_literals

from comment.models import CommentAble
from core.models import *
from event.eventtype import EVENT_POST_PUBLISHED, EVENT_POST_EDITED


# Create your models here.

class Post(ModelWithAuthor, ModelWithDates, LikeAble, CommentAble, WatchableModel):
    title = models.CharField(max_length=255)

    def get_title_for_like(self):
        return 'the post ' + self.title + ' of ' + self.author.get_username()

    def get_title_for_comment(self):
        return 'the post ' + self.title + ' of ' + self.author.get_username()

    def get_event_type(self, created):
        return EVENT_POST_PUBLISHED if created else EVENT_POST_EDITED

    def get_title_for_event(self, eventtype):
        if eventtype is EVENT_POST_PUBLISHED:
            return "User " + self.author.get_username() + " created post with title \"" + self.title + "\""
        else:
            return "User " + self.author.get_username() + " edited post with title \"" + self.title + "\""

    def is_tracked(self):
        # TODO: add a condition when we create an event on this action
        return True
