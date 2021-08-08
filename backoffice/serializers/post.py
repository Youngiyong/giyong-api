from rest_framework import serializers
from backoffice.models import (
    BoardCategory, Board, Post, Shop
)
from django.conf import settings


class PostShopSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class BoardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCategory
        fields = "__all__"

class PostListSerializer(serializers.ModelSerializer):
    shop = PostShopSerailizer()
    category = BoardCategorySerializer()
    class Meta:
        model = Post
        fields = ["id",
                  "board_id",
                  "shop_id",
                  "category_id",
                  "is_secret",
                  "thumbnail",
                  "title",
                  "contents",
                  "name",
                  "email",
                  "password",
                  "hit",
                  "ip",
                  "created_at",
                  "deleted_at",
                  "shop",
                  'category'
                  ]