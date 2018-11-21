from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.
@login_required(login_url='/login')
def create(request):
    try:
        if request.method == 'POST':
            form = PostForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'post/create.html', {'form': PostForm()})


def detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        'title': 'Detail: %s' % (instance.title),
        'data_row': instance
    }
    return render(request, 'post/detail.html', context=context)


def list(request):

    if 'posts.view_post' not in request.user.get_all_permissions():
        raise Http404

    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {
        'title': 'Post List',
        'data_rows': data_rows
    }
    return render(request, 'post/index.html', context=context)


@login_required(login_url='/login')
def update(request, id=None):
    try:
        instance = get_object_or_404(Post, id=id)
        form = PostForm(request.POST or None, files=request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('posts:index')
        context = {
            'title': 'Post edit %s' % (instance.title),
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'post/edit.html', context=context)


def delete(request, id=None):
    try:
        instance = get_object_or_404(Post, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('posts:index')


def login_page(request):
    return HttpResponse('hihi')
