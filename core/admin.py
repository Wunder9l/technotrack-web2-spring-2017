from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Relationship


@admin.register(User)
class UserAdmin(BaseUserAdmin, ):
    pass


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass
