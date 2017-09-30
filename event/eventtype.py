from core.utils import Enum

EVENT_SUBSCRIPTION = "subscribed_at"
EVENT_POST_PUBLISHED = "post_published"
EVENT_POST_EDITED = "post_edited"
EVENT_COMMENT_PUBLISHED = "comment_created"
EVENT_COMMENT_EDITED = "comment_edited"
EVENT_LIKE = "like"


class EventType(Enum):
    choices = [
        EVENT_SUBSCRIPTION,
        EVENT_POST_PUBLISHED,
        EVENT_POST_EDITED,
        EVENT_COMMENT_PUBLISHED,
        EVENT_COMMENT_EDITED,
        EVENT_LIKE,
    ]
