from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from  core.permissions import IsOwnerOrAdminOrReadOnly
from .serializers import Comment, CommentSerializer

from django.views.decorators.csrf import ensure_csrf_cookie


# @ensure_csrf_cookie
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOrReadOnly)

    def get_queryset(self):
        qs = super(CommentViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
