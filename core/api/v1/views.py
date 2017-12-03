from django.contrib.auth import password_validation
from django.core.exceptions import FieldError
from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.views import MultiSerializerViewSet
from .serializers import LikeSerializer, UserListSerializer, UserDetailSerializer, UserSelfSerializer, \
    PasswordSerializer, CreateRelationshipSerializer
from core.models import Like, User, Relationship, RelationshipEnum
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


class UserSelfViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    model = User
    serializer_class = UserSelfSerializer
    permission_classes = IsAuthenticated,
    queryset = User.objects.all().filter(id=0)  #

    # def get_serializer(self, instance=None, data=None, many=False, partial=True):
    #     serializer = self.serializer_class(self.request.user, data=kwargs.get('data'), partial=True)
    #     serializer.is_valid()
    #     return serializer

    # def get_serializer(self, instance, *args, **kwargs):
    #     print  args, kwargs
    #     print kwargs.get('data'), type(kwargs.get('data'))
    #     serializer = self.serializer_class(self.request.user, data=dict(kwargs.get('data')), partial=True)
    #     serializer.is_valid()
    #     return serializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=request.user)
        return Response(serializer.data)

    def get_queryset(self):
        return [self.request.user, ]

    def partial_update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @list_route(methods=['post', ], permission_classes=[IsAuthenticated, IsOwnerOrAdminOrReadOnly])
    def relationship(self, request):
        user = request.user
        serializer = CreateRelationshipSerializer(data=request.data)
        if serializer.is_valid():
            to_user = User.objects.filter(id=serializer.validated_data['to_person'])[0]
            validated_status = serializer.validated_data['status']
            if user.id == to_user.id:
                return Response({'to_person': 'You can not create relationship to yourself'},
                                status=status.HTTP_400_BAD_REQUEST)
            relationship = user.add_relationship(to_user, validated_status)
            if not relationship:
                return Response(
                    {'result': "Could not create relation, please try later"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {'result': 'You {} {}'.format(RelationshipEnum().get_name(validated_status), to_user.username)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

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
