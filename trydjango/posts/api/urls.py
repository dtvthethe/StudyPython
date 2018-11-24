from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.PostListAPIView().as_view(), name='list'),
    path('cat', views.CategoryListAPIView().as_view(), name='cat_list'),
    path('<int:pk>', views.PostRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>', views.PostUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', views.PostDestroyAPIView.as_view(), name='destroy'),
    path('insert', views.PostCreateAPIView.as_view(), name='create'),
]
