#!/usr/bin/env python  认证和权限
# -*- coding:utf-8 -*-
from rest_framework.permissions import BasePermission
from rest_framework import exceptions


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
        try:
            if request.user.username == "admin":
                return True
        except:
            exceptions.PermissionDenied()
            # raise
            return False
        return False

    # GenericAPIView中get_object时调用
    def has_object_permission(self, request, view, obj):
        if request.user.username == "admin":
            return True
