from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


# Create your views here.
def create(request):
    return HttpResponse('list')


def detail(request, id = -1):
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


def update(request):
    return HttpResponse('update')


def delete(request):
    return HttpResponse('delete')
