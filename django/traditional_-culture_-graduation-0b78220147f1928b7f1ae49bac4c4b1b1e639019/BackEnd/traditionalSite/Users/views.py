import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from Users.models import Users
from commonUtil.returnDataObject import success_json_response, fail_json_response


# Create your views here.
class UsersAPI(APIView):
    def get(self, request, *args, **kwargs):
        """
        根据ID获取用户信息
        """
        user_id = request.query_params.get('user_id', 0)
        if not user_id or user_id == 0:
            return JsonResponse(fail_json_response('参数缺失，请联系管理员', '失败'))
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse(fail_json_response('查询不到用户', '失败'))
        user.save()  # 更新登录时间
        return JsonResponse(success_json_response("查询成功", {
            "id": user.id,
            "username": user.username
        }))

    def post(self, request, *args, **kwargs):
        """
        用户登录与注册
        """
        data = json.loads(request.body.decode("utf-8"))
        request_type = data['request_type']
        username = data['username']
        password = data['password']
        if not username or not password:
            return JsonResponse(fail_json_response("用户名或密码不能为空！", "失败"))
        user = Users.objects.filter(username=username).first()
        if request_type == 'login':
            # 登录
            if not user:
                return JsonResponse(fail_json_response("用户不存在，请重新输入用户名！", "失败"))

            if user.password != password:
                return JsonResponse(fail_json_response("用户密码输入错误，请重新输入！", "失败"))

            if user.is_banned == '1':
                return JsonResponse(fail_json_response("登录失败，账号被封禁！", "失败"))

            return JsonResponse(success_json_response("成功", {"id": user.id}))

        elif request_type == 'register':
            # 注册
            if user:
                return JsonResponse(fail_json_response("用户已存在，请重新输入用户名！", "失败"))
            user_new = Users.objects.create(
                username=username,
                password=password
            )
            if not user_new:
                return JsonResponse(fail_json_response("注册失败，请联系管理员", "失败"))
            return JsonResponse(success_json_response("注册成功", {"id": user_new.id}))

    def put(self, request, *args, **kwargs):
        """修改个人信息"""
        data = json.loads(request.body.decode("utf-8"))
        user_id = data['user_id']
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse(fail_json_response("查询不到该用户", "失败"))
        if data["request_type"] == 'user_info':
            user_by_name = Users.objects.filter(username=data['username']).first()
            if user_by_name:
                return JsonResponse(fail_json_response("用户名已存在，请重试", "失败"))
            user_by_phone = Users.objects.filter(phone=data['phone']).first()
            if user_by_phone:
                return JsonResponse(success_json_response("手机号码已被使用，请重试", "失败"))
            user.username = data['username']
            user.phone = data['phone']
            user.personal_info = data['personal_info']
            user.save()
            return JsonResponse(success_json_response("用户信息修改成功", {"user_id": user.id}))
        elif data["request_type"] == 'user_password':
            if user.password != data['password']:
                return JsonResponse(fail_json_response("原始密码输入错误", "请重新输入"))
            user.password = data['new_password']
            user.save()
            return JsonResponse(success_json_response("用户密码修改成功", {"user_id": user.id}))
        elif data["request_type"] == 'banned':
            if user.is_banned == "1":
                user.is_banned = "0"
                user.save()
                return JsonResponse(success_json_response("取消用户禁用成功", {"user_id": user.id}))
            elif user.is_banned == "0":
                user.is_banned = "1"
                user.save()
                return JsonResponse(success_json_response("用户禁用成功", {"user_id": user.id}))
            return JsonResponse(success_json_response("操作失败", "操作失败"))

        return JsonResponse(fail_json_response("修改失败", "修改失败"))

    def delete(self, request, *args, **kwargs):
        """ 删除用户 """
        user_id = request.GET.get("user_id")
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse(fail_json_response("查询不到用户信息", "失败"))
        user.delete()
        return JsonResponse(success_json_response("删除成功", "删除成功"))


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserListAPI(APIView):
    def get(self, request, *args, **kwargs):
        """ 获取所有员工信息 """
        query_condition = Q()

        query_keyword = request.query_params.get('query_keyword')

        if query_keyword:
            query_condition &= Q(username__contains=query_keyword)

        queryset = Users.objects.filter(query_condition).order_by("-id")
        if not queryset:
            return JsonResponse(success_json_response("查询成功", []))

        paginator = StandardResultsSetPagination()  # 分页器
        page = paginator.paginate_queryset(queryset, request)

        return_data = []
        for user in page:
            return_data.append(
                {
                    "user_id": user.id,
                    "username": user.username,
                    "phone": user.phone,
                    "personal_info": user.personal_info,
                    "photo_url": user.photo_url,
                    "is_banned": user.is_banned,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at
                }
            )
        return JsonResponse(success_json_response("查询成功", paginator.get_paginated_response(return_data).data))
