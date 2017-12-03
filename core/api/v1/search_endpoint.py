from rest_framework.decorators import api_view
from rest_framework.response import Response
from haystack.query import SearchQuerySet, AutoQuery
from core.api.v1.serializers import UserBriefSerializer, User
from comment.api.v1.serializers import CommentSerializer, Comment
from post.api.v1.serializers import PostSerializer, Post
from event.api.v1.serializers import EventSerializer, Event

SEARCH_TYPE_TO_SERIALIZER = {
    User: UserBriefSerializer,
    Comment: CommentSerializer,
    Post: PostSerializer,
    Event: EventSerializer
}
SEARCH_TYPE_GROUP_NAME = {
    User: 'users',
    Post: 'posts',
    Event: 'events',
    Comment: 'comments',
}


def serialize_search_result(res):
    response = {}
    for search_item in res:
        item = search_item.object
        item_type = type(item)
        if item_type not in SEARCH_TYPE_GROUP_NAME or item_type not in SEARCH_TYPE_TO_SERIALIZER:
            raise TypeError("Invalid type in search: {}".format(item_type))
        else:
            response.setdefault(SEARCH_TYPE_GROUP_NAME[item_type], []).append(
                dict(SEARCH_TYPE_TO_SERIALIZER[item_type](item).data))
    return response


@api_view(['GET'])
# @throttle_classes([OncePerDayUserThrottle])
def search_api(request):
    if request.GET and request.GET.get('query'):
        sqs = SearchQuerySet().filter(text=AutoQuery(request.GET.get('query')))
        res = sqs.load_all()
        response = serialize_search_result(res)
        return Response(response)

    return Response({})
