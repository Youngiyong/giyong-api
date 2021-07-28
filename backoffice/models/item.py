from django.db import models



class SiteGoods(models.Model):
    """
        v2 상품 목록
    """


    id = models.AutoField(primary_key=True)
    item_number = models.CharField(max_length=20, blank=True)
    delivery_type = models.CharField(
        max_length=1,
        help_text="배송/미배송(S:배송, N:미배송)",
    )
    goods_type = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        help_text="상품타입(D:할인,N:정가,O:옵션)",
    )


    sell_start_at = models.DateTimeField(blank=True, null=True, help_text="판매시작일시")
    sell_end_at = models.DateTimeField(blank=True, null=True, help_text="판매종료일시")
    buy_start_at = models.TimeField(blank=True, null=True, help_text="운영시작시간")
    buy_end_at = models.TimeField(blank=True, null=True, help_text="운영종료시간")
    cook_time = models.SmallIntegerField(
        blank=True, null=True, default=0, help_text="조리시간(분단위- 최대 180)"
    )

    shop = models.IntegerField(help_text="매장정보")
    franchisee_code = models.CharField(
        max_length=2, blank=True, null=True, help_text="프랜차이즈 코드"
    )
    franchisee_goods_code = models.CharField(
        max_length=16, blank=True, null=True, help_text="CU,K7 자체상품코드"
    )
    supplier_code = models.CharField(
        max_length=20, blank=True, null=True, help_text="모상품업체상품코드"
    )
    plucode = models.CharField(
        max_length=24, blank=True, null=True, help_text="PLU 포함된 ITF-14코드"
    )

    name = models.CharField(db_column="name", max_length=200, help_text="상품명")
    description = models.TextField(blank=True, null=True, help_text="상품정보 내용")
    search_keywords = models.CharField(
        max_length=255, blank=True, null=True, help_text="검색키워드"
    )
    is_new = models.BooleanField(default=False, help_text="새로 들어온 상품 여부")

    original_price = models.PositiveIntegerField(help_text="원가")
    offer_price = models.IntegerField(default=0, help_text="매입가격")
    price = models.PositiveIntegerField(default=0, help_text="판매가")
    reward = models.DecimalField(null=True, max_digits=5, decimal_places=2, default=0.00, help_text="적립률")
    commission = models.DecimalField(max_digits=5, decimal_places=2, default=3.5, help_text="취급수수료")
    min_sell = models.SmallIntegerField(default=1, help_text="최소판매수량")
    max_sell = models.SmallIntegerField(default=2, help_text="최대판매수량")
    is_tax = models.BooleanField(default=True, help_text="과세여부")
    is_adult = models.BooleanField(default=False, help_text="성인상품여부")

    created_at = models.DateTimeField(auto_now_add=True, help_text="생성일")
    updated_at = models.DateTimeField(blank=True, null=True, help_text="갱신일")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일")

    last_modifier = models.IntegerField(blank=True, null=True, help_text="최근변경자")


    class Meta:
        managed = False
        db_table = "items"
