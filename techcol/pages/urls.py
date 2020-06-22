from django.urls import path
from .views import (
    contacts_view,
    administration_view,
    departments_view,
    internactiv_view,
    pubinfo_view,
)

app_name = "pages"
urlpatterns = [
    path('contacts/', contacts_view, name='contacts'),
    path('administration/', administration_view, name='administration'),
    path('departments/', departments_view, name='departments'),
    path('internactiv/', internactiv_view, name='internactiv'),
    path('pubinfo/', pubinfo_view, name='pubinfo'),
]