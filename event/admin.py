from django.contrib import admin
from .models import Event
from core.adminsupplier import LikeAbleAdmin


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass