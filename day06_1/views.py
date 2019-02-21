#!/usr/bin/env python  认证和权限
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView06_1(APIView):

    def get(self, request, *args, **kwargs):
        # self.dispatch
        # print(request.user)
        # print(request.auth)
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
