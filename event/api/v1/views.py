from rest_framework.viewsets import ReadOnlyModelViewSet

from  core.permissions import IsOwnerOrAdminOrReadOnly
from .serializers import Event, EventSerializer


class EventReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        qs = super(EventReadOnlyViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(user__username=self.request.query_params.get('username'))
        return qs
