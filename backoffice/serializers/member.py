from rest_framework import serializers

from backoffice.models import Members


class MemberSerializer(serializers.ModelSerializer):
    """
        백오피스 회원
    """
    class Meta:
        model = Members
        fields = "__all__"