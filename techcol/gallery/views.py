from django.shortcuts import render, get_object_or_404
from .models import GalleryPost, GalleryImage

# Create your views here.

def gallery_view(request):
    allposts = list(reversed(GalleryPost.objects.all()))
    images = list(GalleryImage.objects.all())

    context = {
        'posts': allposts,
        'images': images,
    }
    return render(request, 'gallery.html', context)
