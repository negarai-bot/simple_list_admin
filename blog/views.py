from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Postblog

def Post_list_view(request):
    #post_list = Postblog.objects.all()
    post_list =Postblog.objects.filter(status='pub')
    return render(request, 'blog/post_list.html', {'post_list':post_list})

def post_detail_view(request, pk):
    #post = Postblog.objects.get(pk=pk)
    post =get_object_or_404(Postblog, pk=pk)
    return render(request, 'blog/post_dtail.html', {'post': post})

def post_created_view(request):
    return render(request, 'blog/post_created.html')
