from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True, help_text="주문 아이디")
    old_order_id = models.IntegerField(default=0)
    status = models.CharField(max_length=5, blank=True, null=True, help_text="주문상태")
    member = models.ForeignKey("Member", models.DO_NOTHING, help_text="멤버아이디")
    shop = models.ForeignKey(
        "Shop",
        models.DO_NOTHING,
        db_column="shop_id",
        blank=True,
        null=True,
        help_text="상점아이디",
    )
    order_number = models.CharField(max_length=20, blank=True, null=True, help_text="결제번호", unique=True)
    pickup_type = models.CharField(max_length=1, help_text="픽업방법")
    people = models.IntegerField(blank=True, null=True, help_text="방문인원)")
    pickup_at = models.DateTimeField(blank=True, null=True, help_text="주문 픽업시간")

    pay_result = models.CharField(max_length=1, help_text="결제결과")
    pay_method = models.CharField(max_length=1, help_text="결제방법")
    pay_bank = models.CharField(max_length=50, help_text="결제은행")

    total_item = models.IntegerField(blank=True, null=True, default=0, help_text="상품 가격 합계 (할인X)")
    total_delivery = models.IntegerField(default=0, help_text="(기본 배송/배달비 + 추가 배송/배달비)")
    subtotal_delivery = models.IntegerField(default=0, help_text="기본 배송/배달비")
    subtotal_delivery_extra = models.IntegerField(default=0, help_text="추가 배송/배달비")
    total_point = models.IntegerField(default=0, help_text="사용한 총 포인트 (라오포인트 + 외부포인트)")
    subtotal_point_out = models.IntegerField(default=0, help_text="사용한 외부포인트")
    subtotal_point_lastorder = models.IntegerField(default=0, help_text="사용한 라오포인트")
    total_purchase = models.IntegerField(default=0, help_text="총 금액")
    subtotal_pg = models.IntegerField(default=0, help_text="PG로 요청한 결제금액")

    auto_approve_type = models.IntegerField(default=2, blank=True, null=True, help_text="자동승인")
    auto_approve_duration = models.IntegerField(blank=True, null=True, help_text="자동승인대기시간")

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="생성일")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, help_text="갱신일")
    canceled_at = models.DateTimeField(blank=True, null=True, help_text="주문 취소시간")
    checked_at = models.DateTimeField(blank=True, null=True, help_text="주문 수신확인")
    confirmed_at = models.DateTimeField(blank=True, null=True, help_text="주문 승인시간")
    finished_at = models.DateTimeField(blank=True, null=True, help_text="구매 확정시간")
    purchased_at = models.DateTimeField(blank=True, null=True, help_text="구매 확정시간")


    class Meta:
        managed = False
        db_table = "orders"