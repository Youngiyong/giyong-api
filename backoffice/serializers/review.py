from rest_framework import serializers

from backoffice.models import Reviews


class MemberSerializer(serializers.ModelSerializer):
    """
        백오피스 리뷰 상품
    """
    class Meta:
        model = Reviews
        fields = "__all__"