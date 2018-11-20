from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('create', views.create),
    path('delete', views.delete),
    path('detail', views.detail),
    path('update', views.update),
]
