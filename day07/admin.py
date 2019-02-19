from django.contrib import admin
from .models import UserInfo, UserToken


# Register your models here.


@admin.register(UserInfo)  # 直接注册model 数据表
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'username', 'password')
    # list_display_links = ['name', 'product_id']


@admin.register(UserToken)  # 直接注册model 数据表
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')
    list_display_links = []
