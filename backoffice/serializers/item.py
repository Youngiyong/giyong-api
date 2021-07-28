from rest_framework import serializers

from backoffice.models import SiteGoods


class ItemSerializer(serializers.ModelSerializer):
    """
        백오피스 회원
    """
    class Meta:
        model = SiteGoods
        fields = "__all__"