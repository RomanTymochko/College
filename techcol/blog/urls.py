from django.urls import path
from .views import (
    all_news_view,
    news_post_view,
    abiturientu_post_view,
    studentu_post_view,
    all_abiturientu_posts_view,
    all_studentu_posts_view,
)

app_name = "blog"
urlpatterns=[
    path('news/', all_news_view, name = 'news'),
    path('news/<int:post_id>/', news_post_view, name='news_post'),

    path('studentu/', all_studentu_posts_view, name = 'studentu'),
    path('studentu/<int:post_id>/', abiturientu_post_view, name='studentu_post'),

    path('abiturientu/', all_abiturientu_posts_view, name = 'abiturientu'),
    path('abiturientu/<int:post_id>/', studentu_post_view, name='abiturientu_post'),
]