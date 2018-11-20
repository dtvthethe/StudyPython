from django.shortcuts import render, HttpResponse
from .models import Post


# Create your views here.
def create(request):
    return HttpResponse('list')


def detail(request, id = -1):
    return HttpResponse('detail')


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
