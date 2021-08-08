from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey("Board", models.DO_NOTHING)
    shop = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True, )
    category = models.ForeignKey("BoardCategory", models.DO_NOTHING)
    is_secret = models.BooleanField(blank=True, null=True, help_text="비공개여부")
    is_answered = models.BooleanField(blank=True, null=True, help_text="답변여부")
    is_shown = models.BooleanField(blank=True, null=True, help_text="노출여부")
    thumbnail = models.TextField(help_text="썸네일", blank=True, null=True, )
    title = models.CharField(max_length=250, help_text="제목")
    contents = models.CharField(max_length=250, help_text="내용")
    name = models.CharField(max_length=100, blank=True, null=True, help_text="이름")
    email = models.CharField(max_length=100, blank=True, null=True, help_text="이메일")
    password = models.CharField(max_length=100, blank=True, null=True, help_text="패스워드")
    hit = models.IntegerField(help_text="조회수")
    ip = models.CharField(max_length=20, blank=True, null=True, help_text="아이피")
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성일")
    updated_at = models.DateTimeField(blank=True, null=True, help_text="수정일")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일")

    class Meta:
        managed = False
        db_table = "posts"


class BoardCategory(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey("Board", models.DO_NOTHING)
    name = models.CharField(max_length=250, help_text="카테고리 이름")

    class Meta:
        managed = False
        db_table = "board_categories"

class Codes(models.Model):
    group = models.CharField(max_length=20, help_text="코드그룹")
    code = models.CharField(max_length=40, unique=True, help_text="코드")
    name = models.CharField(max_length=200, help_text="코드명")
    description = models.CharField(max_length=200, help_text="코드설명")
    status = models.CharField(max_length=1, help_text="사용상태")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="생성일")
    updated_at = models.DateTimeField(blank=True, null=True, help_text="수정일")

    class Meta:
        verbose_name = "코드테이블"
        managed = False
        db_table = "codes"
        unique_together = (("group", "code"),)

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="생성일")
    updated_at = models.DateTimeField(blank=True, null=True, help_text="갱신일")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일", )
    # ------- v2
    post_table = models.CharField(max_length=128, help_text="적용테이블명")
    name = models.CharField(max_length=250, help_text="이름")
    use_comment = models.IntegerField(blank=True, null=True, help_text="")
    section_code = models.ForeignKey(Codes, models.DO_NOTHING, db_column="section_code", to_field='code', blank=True, null=True, max_length=20)

    class Meta:
        managed = False
        db_table = "boards"

