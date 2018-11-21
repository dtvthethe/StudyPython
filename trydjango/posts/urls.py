from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='index'),
    path('post/create', views.create, name='create'),
    path('post/delete/<int:id>/', views.delete, name='delete'),
    path('post/detail/<str:slug>/', views.detail, name='detail'),
    path('post/update/<int:id>/', views.update, name='update'),
]
