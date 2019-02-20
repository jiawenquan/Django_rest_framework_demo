# coding: utf-8
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator


class LoginRequiredMixin(View):

    @method_decorator(login_required(login_url="/admin/"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # python 2.7 的写法
    # @method_decorator(login_required(login_url="/admin/"))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


# @login_required
class Users(LoginRequiredMixin):

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
