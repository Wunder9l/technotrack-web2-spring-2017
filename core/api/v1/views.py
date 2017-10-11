from django.core.exceptions import FieldError
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.views import MultiSerializerViewSet
from .serializers import LikeSerializer, UserListSerializer, UserDetailSerializer
from core.models import Like, User
from  core.permissions import IsOwnerOrReadOnly


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        qs = super(LikeViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(MultiSerializerViewSet):
    model = User
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializers = {
        'default': UserListSerializer,
        'list': UserListSerializer,
        'retrieve': UserDetailSerializer,
        'create': UserDetailSerializer,
    }

    def get_queryset(self):
        qs = super(UserViewSet, self).get_queryset()
        for param in self.request.query_params:
            print param, self.request.query_params[param]
            if not u'username' == param and not u'pk' == param and not u'id' == param:
                try:
                    qs.filter(**{param: self.request.query_params[param]})
                except FieldError as e:
                    print e
                    raise Http404("Cannot resolve keyword u'%s' into field" % param)
        return qs

    def get_object(self):
        # return super(UserViewSet, self).get_object()
        queryset = self.filter_queryset(self.get_queryset())

        user_id = self.kwargs[self.lookup_field]
        try:
            filter_kwargs = {self.lookup_field: int(user_id)}
        except ValueError:
            filter_kwargs = {'username': user_id}

        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
