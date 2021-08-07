"""
백오피스 리뷰
"""
from rest_framework import serializers
from backoffice.models import (
    Reviews,
    ReviewImage,
    SiteGoods, Members
)
from giyong import settings


class ReviewMemberSerializer(serializers.ModelSerializer):
    cp = serializers.CharField(source="mobile")
    class Meta:
        model = Members
        fields = ['id', 'name', 'cp']

class ReviewItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteGoods
        fields = ['id', 'name', 'delivery_type']

class ReviewImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewImage
        fields = ["id", "review_id", "original"]

    def to_representation(self, instance):
        res = super(ReviewImageSerializer, self).to_representation(instance)

        res['original'] = "/"+res['original'].lstrip(settings.GIYONG["CDN"])
        print(res['original'])
        return res


class ReviewChildrenSerializer(serializers.ModelSerializer):
    image = ReviewImageSerializer(
        source="reviewimage_set", many=True, help_text="리뷰이미지"
    )
    created_at = serializers.DateTimeField(
        required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S", help_text="생성일"
    )
    updated_at = serializers.DateTimeField(
        required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S", help_text="생성일"
    )
    deleted_at = serializers.DateTimeField(
        required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S", help_text="생성일"
    )
    member_id = serializers.IntegerField(source="member.id")
    item_id = serializers.IntegerField(source="item.id")
    parent_id = serializers.IntegerField(source='parent.id')
    member = ReviewMemberSerializer()
    class Meta:
        model = Reviews
        fields = [
            "id",
            "item_id",
            "member_id",
            "order_id",
            "contents",
            "image",
            "parent_id",
            "good",
            "bad",
            "is_visible",
            "created_at",
            "updated_at",
            "deleted_at",
            "member"
        ]


class ReviewsSerializer(serializers.ModelSerializer):
    """
        리뷰
    """

    id = serializers.IntegerField(read_only=True)
    contents = serializers.CharField(required=False, allow_null=True, help_text="내용")
    image = ReviewImageSerializer(
        source="reviewimage_set", many=True, help_text="리뷰이미지"
    )
    parent_id = serializers.IntegerField(
        required=False, default=None, help_text="부모아이디(리뷰의 리뷰)"
    )
    # item = ReviewItemSerializer()
    good = serializers.IntegerField(required=False, default=0, help_text="추천")
    bad = serializers.IntegerField(required=False, default=0, help_text="비추천")
    is_visible = serializers.IntegerField(
        required=False, default=True, help_text="리뷰노출 여부"
    )
    created_at = serializers.DateTimeField(
        required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S", help_text="생성일",
    )
    updated_at = serializers.DateTimeField(
        required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S", help_text="갱신일",
    )
    received_at = serializers.DateTimeField(
        required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S", help_text="상품인계날짜",
    )
    member_name = serializers.CharField(
        source="member.name", required=False, help_text=""
    )

    class Meta:
        model = Reviews
        fields = [
            "id",
            "member",
            "member_name",
            "image",
            "order_id",
            "contents",
            "parent_id",
            # "item",
            "good",
            "bad",
            "is_visible",
            "created_at",
            "updated_at",
            "received_at",
        ]





class ReviewListSerializer(ReviewsSerializer):
    """
    백오피스 - 리뷰 관리
    """
    image = serializers.CharField(source="image_path")
    review_image = ReviewImageSerializer(
        source="reviewimage_set", many=True, help_text="리뷰이미지"
    )
    parent_id = serializers.IntegerField(source="parent")
    member_id = serializers.IntegerField(source="member.id")
    item_id = serializers.IntegerField(source="item.id")
    children = ReviewChildrenSerializer(source="review_parent")
    item = ReviewItemSerializer()
    member = ReviewMemberSerializer()
    class Meta:
        model = Reviews
        fields = [
            "id",
            "item_id",
            "member_id",
            "order_id",
            "contents",
            "image",
            "parent_id",
            "good",
            "bad",
            "is_visible",
            "received_at",
            "created_at",
            "updated_at",
            "deleted_at",
            "item",
            "member",
            "children",
            "review_image"
        ]

    def to_representation(self, instance):
        res = super(ReviewListSerializer, self).to_representation(instance)
        if not res["updated_at"]:
            res["updated_at"] = res["created_at"]
        return res

