
from django.db import models

class Reviews(models.Model):
    """
        리뷰
    """

    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0, help_text='주문아이디')
    contents = models.TextField(help_text="내용")
    image_path = models.TextField(db_column='image', blank=True, null=True, help_text="이미지리스트")
    parent = models.OneToOneField(
        "self",
        models.DO_NOTHING,
        related_name="review_parent",
        blank=True,
        null=True,
        help_text="부모아이디(리뷰의리뷰)",
    )
    good = models.IntegerField(default=0, blank=True, null=True, help_text="추천")
    bad = models.IntegerField(default=0, blank=True, null=True, help_text="비추천")
    is_visible = models.BooleanField(default=True, blank=True, null=True, help_text="리뷰노출")
    received_at = models.DateTimeField(blank=True, null=True, help_text="상품받은날짜")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="생성일")
    updated_at = models.DateTimeField(auto_now=True, null=True, help_text="갱신일")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일")



    class Meta:
        managed = False
        db_table = "reviews"
        ordering = ['-id']


class ReviewWarnings(models.Model):
    """
        리뷰신고
    """

    id = models.AutoField(primary_key=True)
    review = models.ForeignKey(
        Reviews, models.DO_NOTHING, blank=True, null=True, help_text="리뷰아이디"
    )

    warning_reason = models.CharField(
        max_length=250, blank=True, null=True, help_text="신고사유"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, help_text="생성일"
    )
    updated_at = models.DateTimeField(
        blank=True, null=True, help_text="갱신일"
    )
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일")

    class Meta:
        managed = False
        db_table = "review_warnings"


class ReviewImage(models.Model):
    '''
        리뷰 이미지
    '''

    id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, help_text='리뷰아이디')
    original_path = models.CharField(db_column='original', max_length=1024, help_text='호스트url을 제외한 주소')
    sort = models.SmallIntegerField(help_text='정렬')
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, help_text="생성일"
    )
    updated_at = models.DateTimeField(
        blank=True, null=True, help_text="갱신일"
    )
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일")

    class Meta:
        managed = False
        db_table = 'review_images'
        ordering = ['-sort']

