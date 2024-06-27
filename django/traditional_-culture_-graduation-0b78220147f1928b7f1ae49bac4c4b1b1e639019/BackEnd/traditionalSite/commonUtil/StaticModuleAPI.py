import json

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from Admins.models import Admins
from Users.models import Users
from commonUtil.returnDataObject import success_json_response


class FileUploadAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """ 存储文件 """
        # data = json.loads(request.body.decode('utf-8'))
        # 1. 获取文件
        file_serializer = request.data['file']
        request_type = request.data['request_type']
        # print(request_type)
        # 2. 将文件写入 static路径
        # 读取文件内容
        file_name = file_serializer.name
        file_path = 'uploads/' + file_name
        # 保存文件
        saved_path = default_storage.save(file_path, file_serializer)
        file_url = request.build_absolute_uri(default_storage.url(saved_path))
        # 3. 将文件的地址存储给对应的数据
        if request_type == 'user_photo_url':
            # 获取用户id 存储数据
            user_id = request.data['user_id']
            user_id = int(user_id)
            user = Users.objects.filter(id=user_id).first()
            user.photo_url = file_url
            user.save()
        if request_type == 'admin_photo_url':
            admin_id = request.data['admin_id']
            admin_id = int(admin_id)
            admin = Admins.objects.filter(id=admin_id).first()
            admin.photo_url = file_url
            admin.save()
        # if request_type == 'work_image_url' or request_type == 'work_video_url':
        # 4. 将路径数据返回
        return JsonResponse(success_json_response("上传成功", {"file_url": file_url}))
