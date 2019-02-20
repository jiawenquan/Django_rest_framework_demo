# -*- coding:utf-8 -*-
# todo: 请求头认证
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions

token_list = [
    'sfsfss123kuf3j123',
    'asijnfowerkkf9812',
]


class TestAuthentication(BaseAuthentication):
    def authenticate(self, request):
        import base64
        auth = request.META.get("HTTP_AUTHORIZATION", b"")

        if auth:
            auth = auth.encode('utf-8')

        auth = auth.split()

        if not auth or auth[0].lower() != b"basic":
            raise exceptions.AuthenticationFailed("验证失败")

        if len(auth) != 2:
            raise exceptions.AuthenticationFailed("验证失败")

        username, part, password = base64.b64decode(auth[1]).decode("utf-8").partition(':')

        print(username, part, password)
        if username == "alex" and password == "123":

            return ("alex", "123")
        else:
            raise exceptions.AuthenticationFailed("用户名或密码错误")

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return 'Basic realm=api'  # 请求头登录


class TestView04(APIView):
    # authentication_classes = [TestAuthentication, ]
    # permission_classes = []

    def get(self, request, *args, **kwargs):
        # auth = request.META.get("HTTP_AUTHORIZATION", b"")
        # raise exceptions.AuthenticationFailed('用户名或密码错误')
        print(request.user)
        print(request.auth)
        # msg = 'Invalid basic header. No credentials provided.'
        # raise exceptions.AuthenticationFailed(msg)

        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
