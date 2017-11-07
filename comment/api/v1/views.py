from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import FieldError
from django.http import Http404
from  core.permissions import IsOwnerOrAdminOrReadOnly
from .serializers import Comment, CommentSerializer

from django.views.decorators.csrf import ensure_csrf_cookie


# @ensure_csrf_cookie
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().select_related('author')
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOrReadOnly)

    def get_queryset(self):
        qs = super(CommentViewSet, self).get_queryset()
        for param in self.request.query_params:
            if u'username' == param:
                qs = qs.filter(author__username=self.request.query_params[param])
            else:
                # print {param: self.request.query_params[param]}
                try:
                    qs = qs.filter(**{param: self.request.query_params[param]})
                except FieldError as e:
                    print e
                    raise Http404("Cannot resolve keyword u'%s' into field" % param)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
