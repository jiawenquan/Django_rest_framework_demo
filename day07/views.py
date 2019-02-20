# coding:utf-8
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from day07 import models
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission

# from day07.utils.permission import MyPermission
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

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        return True


class AuthView(APIView):
    authentication_classes = []  # 局部不使用认证

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


class OrderView(APIView):
    # authentication_classes = [Authentication, ]

    def get(self, request, *args, **kwargs):

        # request.user
        # request.auth
        ret = {'code': 1000, 'msg': None}

        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass

        return JsonResponse(ret)


from rest_framework.authentication import BasicAuthentication


class UserInfoView(APIView):
    """
    订单相关业务
    """

    # authentication_classes = [rest_framework.authentication.BasicAuthentication,]
    # permission_classes = [MyPermission,]

    def get(self, request, *args, **kwargs):
        user = request.user

        # try:
        #     if user.user_type == 1:
        #         return HttpResponse("普通用户无权访问")
        #     elif user.user_type == 2:
        #         return HttpResponse("vip 有权访问部分")
        #     elif user.user_type == 3:
        #         return HttpResponse("SVIP 有权访问全部")
        # except exceptions as exc:
        #     print(exc)
        #
        # print(user.user_type)
        # if user == "匿名用户":
        #     return HttpResponse("匿名用户访问用户信息！")

        return HttpResponse("登录用户访问用户信息")
