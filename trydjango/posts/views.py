from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    return render(request, 'post/create.html', {'form': PostForm()})


def detail(request, id = None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Detail: %s' %(instance.title),
        'data_row': instance
    }
    return render(request, 'post/detail.html', context= context)

def list(request):
    context = {
        'title': 'Post List',
        'data_rows': Post.objects.all()
    }
    return render(request, 'post/index.html', context=context)


def update(request, id = None):
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('posts:index')
    context = {
        'title':'Post edit %s' %(instance.title),
        'form': form
    }
    return render(request,'post/edit.html', context=context)

def delete(request, id = None):
    return HttpResponse('delete')
