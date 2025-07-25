from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .form import NewPostForm
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
    if request.method == 'POST':
       form=NewPostForm(request.POST)
       if form.is_valid():
           form.save()
           form =NewPostForm()
    else: #Get request
        form = NewPostForm()
    return render(request, 'blog/post_created.html', context= {'form': form})
    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.object.all()[0]
    #     POST.objects.created(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('Get request')
    # return render(request, 'blog/post_created.html')
