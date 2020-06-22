from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField

class NewsPost(models.Model):
    is_active = models.BooleanField(default=True)
    main_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)
    # description = models.TextField(blank=True)
    # short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("blog:news_post", kwargs={"post_id": self.id})

    def is_post_active(self):
        filtered=[]
        for post_item in list(NewsPost.objects.all()):
            if post_item.is_active:
                filtered.append(post_item)
        return filtered

    class Meta:
        verbose_name = "Новини"
        verbose_name_plural = "Новини"





class AbiturintuPost(models.Model):
    is_active = models.BooleanField(default=True)
    main_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("blog:abiturientu_post", kwargs={"post_id": self.id})

    def is_post_active(self):
        filtred=[]
        for post_item in list(AbiturintuPost.objects.all()):
            if post_item.is_active:
                filtred.append(post_item)
        return filtred

    class Meta:
        verbose_name = "Абітурієнту"
        verbose_name_plural = "Абітурієнту"



class StudentuPost(models.Model):
    is_active = models.BooleanField(default=True)
    main_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("blog:studentu_post", kwargs={"post_id": self.id})

    def is_post_active(self):
        filtred=[]
        for post_item in list(StudentuPost.objects.all()):
            if post_item.is_active:
                filtred.append(post_item)
        return filtred

    class Meta:
        verbose_name = "Студенту"
        verbose_name_plural = "Студенту"