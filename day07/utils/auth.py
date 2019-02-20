# encoding: utf-8
'''
@author: allen-jia
@file: auth.py
@time: 2019/2/20 0020 16:21
@desc:
'''

from day07 import models

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class Authentication(object):
    def authenticate(self, request):
        token = request._request.GET.get("token")
        token_obj = models.UserToken.objects.filter(token=token).first()

        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")

        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass
