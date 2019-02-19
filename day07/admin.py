from django.contrib import admin
from .models import UserInfo, UserToken


# Register your models here.


@admin.register(UserInfo)  # ֱ��ע��model ���ݱ�
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'username', 'password')
    # list_display_links = ['name', 'product_id']


@admin.register(UserToken)  # ֱ��ע��model ���ݱ�
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')
    list_display_links = []
