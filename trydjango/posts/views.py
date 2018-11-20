from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.
def create(request):
    try:
        if request.method == 'POST':
            form = PostForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'post/create.html', {'form': PostForm()})


def detail(request, id = None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Detail: %s' %(instance.title),
        'data_row': instance
    }
    return render(request, 'post/detail.html', context= context)

def list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {
        'title': 'Post List',
        'data_rows': data_rows
    }
    return render(request, 'post/index.html', context=context)


def update(request, id = None):
    try:
        instance = get_object_or_404(Post, id = id)
        form = PostForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('posts:index')
        context = {
            'title':'Post edit %s' %(instance.title),
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request,'post/edit.html', context=context)

def delete(request, id = None):
    try:
        instance = get_object_or_404(Post, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('posts:index')

