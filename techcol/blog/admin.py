from django.contrib import admin
from django.db import models
from .models import NewsPost, AbiturintuPost, StudentuPost


# Register your models here.

def publish(modeladmin, request, queryset):
    queryset.update(is_active=True)


def unpublish(modeladmin, request, queryset):
    queryset.update(is_active=False)


class NewsPostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "pub_date", "is_active"]
    list_filter = ["is_active", "pub_date"]
    list_editable = ["title"]
    list_display_links = ["id"]
    actions = [publish, unpublish]
    search_fields = ["id", "title"]
    actions_on_top = False
    actions_on_bottom = True

    class Meta:
        model = NewsPost



class AbiturientuPostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "pub_date", "is_active"]
    list_filter = ["is_active", "pub_date"]
    list_editable = ["title"]
    list_display_links = ["id"]
    actions = [publish, unpublish]
    search_fields = ["id", "title"]
    actions_on_top = False
    actions_on_bottom = True

    class Meta:
        model = AbiturintuPost


class StudentuPostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "pub_date", "is_active"]
    list_filter = ["is_active", "pub_date"]
    list_editable = ["title"]
    list_display_links = ["id"]
    actions = [publish, unpublish]
    search_fields = ["id", "title"]
    actions_on_top = False
    actions_on_bottom = True

    class Meta:
        model = StudentuPost


admin.site.register(NewsPost, NewsPostModelAdmin)
admin.site.register(AbiturintuPost, AbiturientuPostModelAdmin)
admin.site.register(StudentuPost, StudentuPostModelAdmin)
