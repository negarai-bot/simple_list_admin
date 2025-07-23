from django.shortcuts import render
from .models import Postblog

def Post_list_view(request):
    post_list = Postblog.objects.all()
    return render(request, 'blog/post_list.html', {'post_list':post_list})

def post_detail_view(request, pk):
    post = Postblog.objects.get(pk=pk)
    return render(request, 'blog/post_dtail.html', {'post': post})
