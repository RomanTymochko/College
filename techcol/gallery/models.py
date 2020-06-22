from django.db import models
from django.urls import reverse

# Create your models here.

class GalleryPost(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)


    def is_post_active(self):
        filtered=[]
        for post_item in list(GalleryPost.objects.all()):
            if post_item.is_active:
                filtered.append(post_item)
        return filtered

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


class GalleryImage(models.Model):
    gallery = models.ForeignKey(GalleryPost, default=None, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="gallery/")

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural = "Зображення"