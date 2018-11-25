from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post, Category

User = get_user_model()

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='thisisnamespaceapi:retrieve'
    )
    url_update = HyperlinkedIdentityField(
        view_name= 'thisisnamespaceapi:update'
    )
    url_delete = HyperlinkedIdentityField(
        view_name= 'thisisnamespaceapi:destroy'
    )
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'category',
            'user',
            'url',
            'url_update',
            'url_delete',
            'image'
        ]
    def get_user(self, obj):
        return str(obj.user.username)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'timestamp',
            'category',
            'timestamp',
            'updated'
        ]


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            'slug',
            'content',
            # 'timestamp',
            'category',
            # 'timestamp',
            # 'updated'
        ]
    def create(self, validated_data):
        title = validated_data['title']
        slug = validated_data['slug']
        
        return validated_data


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'timestamp',
            'category',
            'timestamp',
            'updated'
        ]


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'timestamp',
            'category',
            'timestamp',
            'updated'
        ]
