from rest_framework import serializers
from backoffice.serializers.post import BoardCategorySerializer
from backoffice.models import (
    Board, Codes
)

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = "__all__"


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Codes
        fields = "__all__"

class BoardListSerializer(serializers.ModelSerializer):

    section_code = CodeSerializer()
    categories = BoardCategorySerializer(
        source="boardcategory_set", many=True, help_text="카테고리"
    )
    class Meta:
        model = Board
        fields = [
            "id",
            "section_code",
            "post_table",
            "name",
            "use_comment",
            "created_at",
            "updated_at",
            "deleted_at",
            "categories"
        ]