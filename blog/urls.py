

from django.urls import path
from . import views
urlpatterns = [
    path('', views.Post_list_view, name='posts_list'),
]
