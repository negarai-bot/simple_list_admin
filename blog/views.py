from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .form import NewPostForm
from django.views import generic
from .models import Postblog
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    # model = Postblog
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Postblog.objects.filter(status='pub').order_by('-datetime_modified')
class PostDetailView(generic.DetailView):
    model = Postblog
    template_name = 'blog/post_dtail.html'
    context_object_name = 'post'

class PostCreatedView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_created.html'

class PostUpdateView(generic.UpdateView):
        model = Postblog
        form_class = NewPostForm
        template_name = 'blog/post_created.html'

class Postdeleteview(generic.DeleteView):
    model = Postblog
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.object.all()[0]
    #     POST.objects.created(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('Get request')
    # return render(request, 'blog/post_created.html')


# def Post_list_view(request):
#     #post_list = Postblog.objects.all()
#     post_list =Postblog.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/post_list.html', {'post_list':post_list})
#
# def post_detail_view(request, pk):
#     #post = Postblog.objects.get(pk=pk)
#     post =get_object_or_404(Postblog, pk=pk)
#     return render(request, 'blog/post_dtail.html', {'post': post})


# def post_created_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form =NewPostForm()
#             return redirect('posts_list')  #get_absolute_url
#     else:  # Get request
#         form = NewPostForm()
#     return render(request, 'blog/post_created.html', context={'form': form})


# def post_update_views(request, pk):
#     post = get_object_or_404(Postblog, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)  # save the past data and now you can edit
#
#     if form.is_valid():
#         form.save()
#     return render(request, 'blog/post_created.html', {'form': form})

# def post_delete_views(request, pk):
#     post = get_object_or_404(Postblog, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_delete.html', {'post': post})

