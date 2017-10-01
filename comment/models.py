from __future__ import unicode_literals
from core.models import *
from event.eventtype import EVENT_COMMENT_EDITED, EVENT_COMMENT_PUBLISHED


# Create your models here.

class Comment(ModelWithAuthor, ModelWithDates, LikeAble, WatchableModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id')
    edited_count = models.IntegerField(default=0)

    text = models.TextField()
    text_was = None

    def get_title_for_like(self):
        return 'the comment of ' + self.author.get_username() + ' on ' + self.object.get_title_for_comment()

    def get_event_type(self, created):
        return EVENT_COMMENT_PUBLISHED if created else EVENT_COMMENT_EDITED

    def get_title_for_event(self, eventtype):
        if eventtype is EVENT_COMMENT_PUBLISHED:
            return "User " + self.author.get_username() + " commented " + self.object.get_title_for_comment() + ": " \
                   + self.text
        else:
            return "User " + self.author.get_username() + " edited comment on " + self.object.get_title_for_comment() \
                   + ": " + self.text

    def is_tracked(self):
        # TODO: add a condition when we create an event on this action
        return True


class CommentAble(models.Model):
    comments_count = models.IntegerField(default=0)

    def get_title_for_comment(self):
        raise NotImplementedError

    class Meta:
        abstract = True
