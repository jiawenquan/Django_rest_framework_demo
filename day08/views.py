#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import exceptions
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
from rest_framework.settings import api_settings

# 保存访问记录
RECORD = {
    '用户IP': [12312139, 12312135, 12312133, ]
}


class TestThrottle(BaseThrottle):
    ctime = time.time

    def get_ident(self, request):
        """
        根据用户IP和代理IP，当做请求者的唯一IP
        Identify the machine making the request by parsing HTTP_X_FORWARDED_FOR
        if present and number of proxies is > 0. If not use all of
        HTTP_X_FORWARDED_FOR if it is available, if not use REMOTE_ADDR.
        """
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        remote_addr = request.META.get('REMOTE_ADDR')
        num_proxies = api_settings.NUM_PROXIES

        if num_proxies is not None:
            if num_proxies == 0 or xff is None:
                return remote_addr
            addrs = xff.split(',')
            client_addr = addrs[-min(num_proxies, len(addrs))]
            return client_addr.strip()

        return ''.join(xff.split()) if xff else remote_addr

    def allow_request(self, request, view):
        """
        是否仍然在允许范围内
        Return `True` if the request should be allowed, `False` otherwise.
        :param request: 
        :param view: 
        :return: True，表示可以通过；False表示已超过限制，不允许访问
        """
        # 获取用户唯一标识（如：IP）

        # 允许一分钟访问10次
        num_request = 10
        time_request = 60

        now = self.ctime()
        ident = self.get_ident(request)  # 获取id
        self.ident = ident
        if ident not in RECORD:
            RECORD[ident] = [now, ]
            return True
        history = RECORD[ident]
        while history and history[-1] <= now - time_request:
            history.pop()
        if len(history) < num_request:
            history.insert(0, now)
            return True
        else:
            return False

    def wait(self):
        """
        多少秒后可以允许继续访问
        Optionally, return a recommended number of seconds to wait before
        the next request.
        """
        last_time = RECORD[self.ident][0]
        now = self.ctime()
        return int(60 + last_time - now)


class VisitThrottle(SimpleRateThrottle):
    scope = "Luffy"

    def get_cache_key(self, request, view):
        return self.get_ident(request)


from rest_framework.throttling import AnonRateThrottle


class TestView08(APIView):
    throttle_classes = [TestThrottle]

    def get(self, request, *args, **kwargs):
        # self.dispatch
        print(request.user)
        print(request.auth)
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')

    def throttled(self, request, wait):
        """
        访问次数被限制时，定制错误信息
        """

        class Throttled(exceptions.Throttled):
            default_detail = '请求被限制.'
            extra_detail_singular = '请 {wait} 秒之后再重试.'
            extra_detail_plural = '请 {wait} 秒之后再重试.'

        raise Throttled(wait)
