from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list),
    path('post/create', views.create),
    path('post/delete', views.delete),
    path('post/detail/<int:id>/', views.detail, name='detail'),
    path('post/update', views.update),
]
