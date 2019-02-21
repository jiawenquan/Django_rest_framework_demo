#!/usr/bin/env python  认证和权限
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission

from rest_framework.request import Request
from rest_framework import exceptions

token_list = [
    'sfsfss123kuf3j123',
    'asijnfowerkkf9812',
]


class TestAuthentication(BaseAuthentication):
    def authenticate(self, request):
        val = request.query_params.get('token')
        if val not in token_list:
            raise exceptions.AuthenticationFailed("用户认证失败")
        return (request._request.user, val)

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        pass


class TestPermission(BasePermission):
    message = "权限验证失败"
    """
    has_permission 是用户对这个视图有没有 GET POST PUT PATCH DELETE 权限的分别判断。
    has_object_permission 是用户过了 has_permission 判断有权限以后，再判断这个用户有没有对一个具体的对象有没有操作权限。
    """

    def has_permission(self, request, view):
        """
        判断是否有权限访问当前请求
        Return `True` if permission is granted, `False` otherwise.
        :param request: 
        :param view: 
        :return: True有权限；False无权限
        """
        if request.user.username == "admin":
            return True

        return False

    # GenericAPIView中get_object时调用
    def has_object_permission(self, request, view, obj):
        if request.user.username == "admin":
            return True

class TestView06(APIView):
    # 认证的动作是由request.user触发
    authentication_classes = [TestAuthentication, ]

    # 权限
    # 循环执行所有的权限
    permission_classes = [TestPermission, ]

    def get(self, request, *args, **kwargs):
        # self.dispatch
        # print(request.user)
        # print(request.auth)
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
