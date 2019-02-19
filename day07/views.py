# coding:utf-8
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from day07 import models
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

# Create your views here.
ORDER_DICT = {
    1: {
        'name': "细分",
        'age': 18,
        'gender': "男",
        'content': "..."
    },
    2: {
        'name': "老公",
        'age': 18,
        'gender': "男",
        'content': "..."
    }
}


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())

    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding="utf-8"))
    return m.hexdigest()


class AuthView(APIView):

    def post(self, request, *args, **kwargs):
        ret = {"code": 1000, "msg": None}

        try:
            user = request._request.POST.get("username")
            pwd = request._request.POST.get("password")
            obj = models.UserInfo.objects.filter(username=user, password=pwd).first()

            if not obj:
                ret['code'] = 1001
                request['msg'] = "用户名或密码错误"

            token = md5(user)
            models.UserToken.objects.update_or_create(user=obj, defaults={"token": token})
            ret["token"] = token
        except Exception as e:
            ret["code"] = 1002
            ret["msg"] = "请求异常"

        return JsonResponse(ret)


class Authentication(object):
    def authenticate(self, request):
        token = request._request.GET.get("token")
        token_obj = models.UserToken.objects.filter(token=token).first()

        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")

        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass


class OrderView(APIView):
    authentication_classes = [Authentication, ]

    def get(self, request, *args, **kwargs):

        # request.user
        # request.auth
        ret = {'code': 1000, 'msg': None}

        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass

        return JsonResponse(ret)
