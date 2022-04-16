from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from django.shortcuts import get_object_or_404

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', read_only=True)
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, data):
        get_following = get_object_or_404(
            User, username=data['following'].username)
        check_follow = Follow.objects.filter(
            user=self.context['request'].user, following=get_following)
        if get_following == self.context['request'].user:
            raise serializers.ValidationError(
                "Нельзя подписаться на себя")
        if check_follow.exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого автора")
        return data
