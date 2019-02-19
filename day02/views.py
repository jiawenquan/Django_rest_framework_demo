# coding:utf-8
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView02(APIView):
    # def dispatch(self, request, *args, **kwargs):
    #     """
    #     请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法
    #
    #     注意：APIView中的dispatch方法有好多好多的功能
    #     """
    #     return super().dispatch(request, *args, **kwargs)
    #

    # 这里的父类 dispatch 方法 根据请求分发
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
