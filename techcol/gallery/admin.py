from django.contrib import admin
from .models import GalleryPost, GalleryImage

# Register your models here.

def publish(modeladmin, request, queryset):
    queryset.update(is_active=True)


def unpublish(modeladmin, request, queryset):
    queryset.update(is_active=False)

class InLineImages(admin.StackedInline):
    model = GalleryImage
    extra = 1

class GalleryPostModelAdmin(admin.ModelAdmin):
    inlines = [InLineImages]
    list_display = ["id", "title", "pub_date", "is_active"]
    list_filter = ["is_active", "pub_date"]
    list_editable = ["title"]
    list_display_links = ["id"]
    actions = [publish, unpublish]
    search_fields = ["id", "title"]
    actions_on_top = False
    actions_on_bottom = True

    class Meta:
        model = GalleryPost


admin.site.register(GalleryPost, GalleryPostModelAdmin)