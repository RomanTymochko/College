from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import NewsPost, AbiturintuPost, StudentuPost
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.

def all_news_view(request):
    allposts = list(reversed(NewsPost.is_post_active(NewsPost)))
    paginator = Paginator(allposts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'news.html', {'posts': posts})


def news_post_view(request, post_id):
    obj = get_object_or_404(NewsPost, id=post_id)
    context = {
            'post': obj
        }
    return render(request, "post.html", context)

def abiturientu_post_view(request, post_id):
    obj = get_object_or_404(NewsPost, id=post_id)
    context = {
            'post': obj
        }
    return render(request, "post.html", context)

def studentu_post_view(request, post_id):
    obj = get_object_or_404(NewsPost, id=post_id)
    context = {
            'post': obj
        }
    return render(request, "post.html", context)

def home_page_view(request):
    # allposts = list(reversed(Post.objects.all()))
    allposts = list(reversed(NewsPost.is_post_active(NewsPost)))[:6]
    if len(allposts) == 6:
        context = {
            'amount': len(allposts),
            'post1': allposts[0],
            'post2': allposts[1],
            'post3': allposts[2],
            'post4': allposts[3],
            'post5': allposts[4],
            'post6': allposts[5]
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponse("There should be 6 or more than 6 posts on home page!")


def all_abiturientu_posts_view(request):
    allposts = reversed(AbiturintuPost.objects.all())
    context = {
        'object': allposts
    }
    return render(request, 'abiturientu.html', context)



def all_studentu_posts_view(request):
    allposts = reversed(StudentuPost.objects.all())
    context = {
        'object': allposts
    }
    return render(request, 'studentu.html', context)
