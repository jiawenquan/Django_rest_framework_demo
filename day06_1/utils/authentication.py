#!/usr/bin/env python  认证
# -*- coding:utf-8 -*-

from rest_framework.authentication import BaseAuthentication

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
