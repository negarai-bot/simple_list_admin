

from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_dtail'),
    path('created/', views.PostCreatedView.as_view(), name='post_created'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.Postdeleteview.as_view(), name='post_delete'),
]
