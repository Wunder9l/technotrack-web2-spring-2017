from django.contrib.auth import password_validation
from django.core.exceptions import FieldError
from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.views import MultiSerializerViewSet
from .serializers import LikeSerializer, UserListSerializer, UserDetailSerializer, UserSelfSerializer, \
    PasswordSerializer
from core.models import Like, User
from  core.permissions import IsOwnerOrAdminOrReadOnly


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOrReadOnly)

    def get_queryset(self):
        qs = super(LikeViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserSelfViewSet(ModelViewSet):
    model = User
    serializer_class = UserSelfSerializer
    permission_classes = IsAuthenticated, IsOwnerOrAdminOrReadOnly
    queryset = User.objects.all()

    def get_queryset(self):
        return [self.request.user, ]

    @list_route(methods=['post'], permission_classes=[IsAuthenticated, IsOwnerOrAdminOrReadOnly])
    def set_password(self, request):
        # user = self.get_object()
        user = request.user
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['new_password']
            # TODO: check if old_password is belongs to user
            old_password = serializer.validated_data["old_password"]
            if not user.check_password(old_password):
                raise serializers.ValidationError("Old password field is not valid")
            else:
                if old_password == new_password:
                    raise serializers.ValidationError("New password is equal to old password")
                else:
                    password_validation.validate_password(new_password, request.user)
                    user.set_password(new_password)
                    user.save()
                    return Response({'status': 'password changed'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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
                    qs = qs.filter(**{param: self.request.query_params[param]})
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
