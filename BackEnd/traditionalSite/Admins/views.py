import json

from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView

from Admins.models import Admins
from Users.views import StandardResultsSetPagination
from commonUtil.returnDataObject import fail_json_response, success_json_response


# Create your views here.
class \
        AdminAPI(APIView):

    def get(self, request, *args, **kwargs):
        """
        根据ID获取用户信息
        """
        admin_id = request.query_params.get('admin_id', 0)
        if not admin_id or admin_id == 0:
            return JsonResponse(fail_json_response('参数缺失，请联系管理员', '失败'))
        admin = Admins.objects.filter(id=admin_id).first()
        if not admin:
            return JsonResponse(fail_json_response('查询不到用户', '失败'))
        admin.save()  # 更新登录时间
        return JsonResponse(success_json_response("查询成功", {
            "id": admin.id,
            "username": admin.username,
            "phone": admin.phone,
            "personal_info": admin.personal_info,
            "photo_url": admin.photo_url
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
        admin = Admins.objects.filter(username=username).first()
        if request_type == 'login':
            # 登录
            if not admin:
                return JsonResponse(fail_json_response("用户不存在，请重新输入用户名！", "失败"))

            if admin.password != password:
                return JsonResponse(fail_json_response("用户密码输入错误，请重新输入！", "失败"))
            return JsonResponse(success_json_response("成功", {"id": admin.id}))

        elif request_type == 'register':
            # 注册
            if admin:
                return JsonResponse(fail_json_response("用户已存在，请重新输入用户名！", "失败"))
            admin_new = Admins.objects.create(
                username=username,
                password=password,
                register_username=data["register_username"]
            )
            if not admin_new:
                return JsonResponse(fail_json_response("注册失败，请联系管理员", "失败"))
            return JsonResponse(success_json_response("注册成功", {"id": admin_new.id}))
        return JsonResponse(fail_json_response("操作失败，操作类型未开启", "失败"))

    def put(self, request, *args, **kwargs):
        """ 修改管理员信息 """
        data = json.loads(request.body.decode("utf-8"))
        admin_id = data['admin_id']
        admin = Admins.objects.filter(id=admin_id).first()
        if not admin:
            return JsonResponse(fail_json_response("查询不到该用户", "失败"))
        if data["request_type"] == 'admin_info':
            admin.username = data['username']
            admin.phone = data['phone']
            admin.personal_info = data['personal_info']
            admin.save()
            return JsonResponse(success_json_response("用户信息修改成功", {"admin_id": admin.id}))
        elif data["request_type"] == 'admin_password':
            if admin.password != data['password']:
                return JsonResponse(fail_json_response("原始密码输入错误", "请重新输入"))
            admin.password = data['new_password']
            admin.save()
            return JsonResponse(success_json_response("用户密码修改成功", {"admin_id": admin.id}))
        return JsonResponse(fail_json_response("修改失败", "修改失败"))

    def delete(self, request, *args, **kwargs):
        """ 删除用户 """
        admin_id = request.GET.get("admin_id")
        admin = Admins.objects.filter(id=admin_id).first()
        if not admin:
            return JsonResponse(fail_json_response("查询不到用户信息", "失败"))
        admin.delete()
        return JsonResponse(success_json_response("删除成功", "删除成功"))


class AdminListAPI(APIView):
    def get(self, request, *args, **kwargs):
        """ 获取所有用户信息 """
        query_condition = Q()

        query_keyword = request.query_params.get("query_keyword")
        if query_keyword:
            query_condition &= Q(username__icontains=query_keyword)

        queryset = Admins.objects.filter(query_condition).order_by("-id")
        paginator = StandardResultsSetPagination()  # 分页器
        page = paginator.paginate_queryset(queryset, request)
        return_data_list = []
        for admin in page:
            return_data_list.append({
                "id": admin.id,
                "username": admin.username,
                "phone": admin.phone,
                "personal_info": admin.personal_info,
                "photo_url": admin.photo_url
            })
        return JsonResponse(success_json_response("查询成功", paginator.get_paginated_response(return_data_list).data))
