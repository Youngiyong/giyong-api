from django.db import models

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    memtype = models.CharField(max_length=1, blank=True, null=True, default="1", help_text="회원종류")
    cp = models.CharField(max_length=20, blank=True, null=False, help_text="폰번")
    name = models.CharField(max_length=20, blank=True, help_text="사용자명")
    password = models.CharField(blank=True, null=True, max_length=100, help_text="비밀번호")
    sex = models.CharField(max_length=1, blank=True, null=True, help_text="성별")
    birth_year = models.CharField(max_length=4, blank=True, null=True, help_text="생년")
    birth_month = models.CharField(max_length=2, blank=True, null=True, help_text="생월")
    birth_day = models.CharField(max_length=2, blank=True, null=True, help_text="생일")
    email = models.CharField(max_length=50, blank=True, null=True, help_text="이메일")
    point_total = models.IntegerField(default=0, help_text="총 포인트")
    alliance_code = models.CharField(max_length=10, blank=True, null=True, help_text="본인 추천인코드")
    alliance = models.CharField(max_length=10, blank=True, null=True, help_text="가입시 입력한 추천인 코드")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="생성일")
    updated_at = models.DateTimeField(blank=True, null=True, help_text="갱신일")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="탈퇴일")
    deleted_cd = models.CharField(max_length=1, blank=True, null=True, help_text="탈퇴사유 코드")
    deleted_reason = models.CharField(max_length=200, blank=True, null=True, help_text="탈퇴사유")
    last_login = models.DateTimeField(auto_now=True, help_text="마지막 로그인")
    is_active = models.BooleanField("계정사용여부", default=True)
    is_staff = models.BooleanField("관리자", default=False)
    is_superuser = models.BooleanField("최고관리자", default=False)

    class Meta:
        managed = False
        db_table = "members"
        ordering = ['-id']
