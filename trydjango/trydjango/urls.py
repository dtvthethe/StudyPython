"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('posts.urls', namespace='abc')),
    path('cat/', include('categories.urls')),
    path('api/post/', include('posts.api.urls', namespace='thisisnamespaceapi')),
    path('admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls'))
    url(r'^api-token-auth/', obtain_jwt_token),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
curl -X POST -d "username=admin&password=password123" http://localhost:8000/api-token-auth/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTQzMTkyMTI3LCJlbWFpbCI6ImR0dnRoZUBnbWFpbC5jb20ifQ.JFE040Q883E2-5dFKkt1w3ZsLyuNKf6fMZTQa1GBWBw

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTQzMTkyODA5LCJlbWFpbCI6ImR0dnRoZUBnbWFpbC5jb20ifQ.2JHvqHbEFiBvJJp6UF3n1ZJfkD4hXNiNehrhHv103hI" http://localhost:8000/api/post/post

'''