# encoding: utf-8
'''
@author: allen-jia
@file: permission.py
@time: 2019/2/20 0020 19:15
@desc:
'''

from rest_framework.permissions import BasePermission
from rest_framework import exceptions


class SVIPPermission(BasePermission):
    message = "必须式SVIP才能访问"

    def has_permission(self, request, view):
        print(request.user)
        if request.user.user_type != 3:
            return False
        return True
        # try:
        #
        #     if request.user.user_type != 3:
        #         return False
        #     return True
        # except:
        #     return False
        #     # exceptions.PermissionDenied("权限认证失败")

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        return True
