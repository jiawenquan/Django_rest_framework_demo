# coding: utf-8
from django.views import View
from django.http import JsonResponse


class Users(View):
    def get(self, request, *args, **kwargs):
        result = {
            'status': True,
            'data': 'response data'
        }
        return JsonResponse(result, status=200)

    def post(self, request, *args, **kwargs):
        result = {
            'status': True,
            'data': 'response data'
        }
        return JsonResponse(result, status=200)
