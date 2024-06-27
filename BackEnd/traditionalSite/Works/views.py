import json

from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from Users.models import Users
from Users.views import StandardResultsSetPagination
from Works.models import Works, Likes, Marks, Comments, Comments_Likes, Comments_Marks
from commonUtil.returnDataObject import success_json_response, fail_json_response


# Create your views here.
class WorksAPI(APIView):
    def get(self, request, *args, **kwargs):
        """ 获取所有作品 """
        queryset = Works.objects.filter().order_by('-id')
        # paginator = StandardResultsSetPagination()  # 分页器
        # page = paginator.paginate_queryset(queryset, request)
        if not queryset:
            return JsonResponse(success_json_response("查询成功", []))
        # 获取返回数据结构
        return JsonResponse(
            success_json_response("查询成功", get_message_by_works(queryset)))

    def post(self, request, *args, **kwargs):
        """ TODO： 上传作品 """
        # 接收数据
        data = json.loads(request.body.decode("utf-8"))
        work_type = data["work_type"]
        title = data["title"]
        worker = data["worker"]
        description = data["description"]
        image_url = data.get("image_url", "")
        content = data["content"]
        video_url = data.get("video_url", "")

        # 存储
        if not (work_type, title, worker, description, content):
            return JsonResponse(fail_json_response("创建失败", "缺少数据"))
        work = Works.objects.create(
            work_type=work_type,
            title=title,
            worker=worker,
            description=description,
            image_url=image_url,
            content=content,
            video_url=video_url
        )
        # 返回
        if not work:
            return JsonResponse(fail_json_response("创建失败", "数据库异常"))
        return JsonResponse(success_json_response("创建成功", work.id))

    def put(self, request, *args, **kwargs):
        """ TODO 编辑作品 """
        # 接收数据
        data = json.loads(request.body.decode("utf-8"))
        work_id = data["work_id"]
        work = Works.objects.filter(id=work_id).first()
        if not work:
            return JsonResponse(fail_json_response("修改失败，查询不到目标", "失败"))
        work.title = data["title"]
        work.work_type = data["work_type"]
        work.worker = data["worker"]
        work.description = data["description"]
        work.image_url = data.get("image_url", "")
        work.content = data["content"]
        work.video_url = data.get("video_url", "")
        work.save()
        return JsonResponse(success_json_response("修改成功", work.id))

    def delete(self, request, *args, **kwargs):
        """ TODO 删除作品 """
        # 接收数据
        work_id = request.GET.get("work_id")
        work = Works.objects.filter(id=work_id).first()
        if not work:
            return JsonResponse(fail_json_response("删除失败", "查询不到作品"))
        work.delete()
        return JsonResponse(success_json_response("删除成功", "删除成功"))


class WorkQueryAPI(APIView):
    def get(self, request, *args, **kwargs):
        """ 作品检索 """
        # 查询标题
        query_keyword = request.GET.get("query_keyword", "")
        work_id = request.GET.get("work_id", 0)
        work_id = int(work_id)
        return_data = []
        if query_keyword != "" and query_keyword:
            works = Works.objects.filter(title__icontains=query_keyword).all()
            if not works:
                return JsonResponse(success_json_response("查询成功", return_data))
            return JsonResponse(success_json_response("查询成功", get_message_by_works(works)))

        # 根据id查询详细信息
        if work_id > 0:
            works = Works.objects.filter(id=work_id).all()
            # 观看次数 +1
            for work in works:
                work.view_count += 1
                work.save()
            return JsonResponse(success_json_response("查询成功", get_message_by_works(works)))

        # 如果没有检索条件，返回所有
        return WorksAPI.get(self, request)


def get_message_by_works(works):
    """ 遍历works获取数据 """
    return_data = []
    for work in works:
        work_id = work.id
        like_count = Likes.objects.filter(work_id=work_id).count()
        mark_count = Marks.objects.filter(work_id=work_id).count()
        comments = Comments.objects.filter(work_id=work_id).all()
        comment_count = comments.count()
        comments_return_data = []
        if comment_count > 0:
            for comment in comments:
                user = Users.objects.filter(id=comment.user_id).first()
                comment_like_count = Comments_Likes.objects.filter(comment_id=comment.id).count()
                comment_mark_count = Comments_Marks.objects.filter(comment_id=comment.id).count()
                comments_return_data.append({
                    'comment_id': comment.id,
                    "username": user.username,
                    "photo_url": user.photo_url,
                    "content": comment.content,
                    "comment_like_count": comment_like_count,
                    "comment_mark_count": comment_mark_count,
                    "created_at": comment.created_at,
                    "updated_at": comment.updated_at
                })
        return_data.append({
            "id": work_id,
            "title": work.title,
            "work_type": work.work_type,
            "worker": work.worker,
            "description": work.description,
            "content": work.content,
            "img_url": work.image_url,
            "video_url": work.video_url,
            "created_at": work.created_at,
            "updated_at": work.updated_at,
            "like_count": like_count,
            "mark_count": mark_count,
            "comment_count": comment_count,
            "view_count": work.view_count,
            "comment": comments_return_data
        })
    return return_data


class operationForWorkByUserAPI(APIView):

    def post(self, request, *args, **kwargs):
        """ 用户对作品进行操作 """
        data = json.loads(request.body.decode("utf-8"))
        work_id = data["work_id"]
        user_id = data["user_id"]
        request_type = data["request_type"]

        if not user_id or not work_id or not request_type:
            return JsonResponse(fail_json_response("数据异常，操作失败", "失败"))

        user = Users.objects.filter(id=user_id).first()
        work = Works.objects.filter(id=work_id).first()
        if not user or not work:
            return JsonResponse(fail_json_response("数据不存在，操作失败", "失败"))

        if request_type == "like":
            like = Likes.objects.filter(
                work_id=work.id, user_id=user.id
            ).first()
            if not like:
                like = Likes.objects.create(
                    work_id=work.id,
                    user_id=user.id
                )
                if not like:
                    return JsonResponse(fail_json_response("点赞失败", "失败"))
                return JsonResponse(success_json_response("点赞成功", like.id))
            like.delete()
            return JsonResponse(success_json_response("点赞已取消", "点赞已取消"))
        elif request_type == "mark":
            mark = Marks.objects.filter(
                work_id=work.id, user_id=user.id
            ).first()
            if not mark:
                mark = Marks.objects.create(
                    work_id=work.id,
                    user_id=user.id
                )
                if not mark:
                    return JsonResponse(fail_json_response("收藏失败", "失败"))
                return JsonResponse(success_json_response("收藏成功", mark.id))
            mark.delete()
            return JsonResponse(fail_json_response("收藏已取消", "收藏已取消"))

        elif request_type == "comment":
            comment_content = data["comment_content"]
            if not comment_content:
                return JsonResponse(fail_json_response("数据缺失，操作失败", "失败"))

            comment = Comments.objects.create(
                work_id=work.id,
                user_id=user.id,
                content=comment_content,
            )
            if not comment:
                return JsonResponse(fail_json_response("操作失败", "失败"))
            return JsonResponse(success_json_response("评论成功", comment.id))


class operationForCommentByUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        """ 对评论进行点赞、收藏 """
        data = json.loads(request.body.decode("utf-8"))
        comment_id = data["comment_id"]
        user_id = data["user_id"]
        request_type = data["request_type"]

        if not user_id or not comment_id or not request_type:
            return JsonResponse(fail_json_response("数据异常，操作失败", "失败"))
        user_id = int(user_id)
        comment_id = int(comment_id)
        user = Users.objects.filter(id=user_id).first()
        comment = Comments.objects.filter(id=comment_id).first()
        if not user or not comment:
            return JsonResponse(fail_json_response("数据不存在，操作失败", "失败"))

        if request_type == "like":
            cl = Comments_Likes.objects.filter(user_id=user.id, comment_id=comment_id).first()
            if cl:
                cl.delete()
                return JsonResponse(success_json_response("点赞已取消", "操作成功"))

            cl = Comments_Likes.objects.create(
                user_id=user.id,
                comment_id=comment.id
            )
            if not cl:
                return JsonResponse(fail_json_response("点赞失败", "失败"))
            return JsonResponse(success_json_response("点赞成功", cl.id))

        elif request_type == "mark":
            cm = Comments_Marks.objects.filter(user_id=user.id, comment_id=comment_id).first()
            if cm:
                cm.delete()
                return JsonResponse(success_json_response("收藏已取消", "操作成功"))

            cm = Comments_Marks.objects.create(
                user_id=user.id,
                comment_id=comment.id
            )
            if not cm:
                return JsonResponse(fail_json_response("收藏失败", "失败"))
            return JsonResponse(success_json_response("收藏成功", cm.id))
        else:
            return JsonResponse(fail_json_response("操作失败", "失败"))

    def delete(self, request, *args, **kwargs):
        """ 删除评论 """
        comment_id = request.GET.get('comment_id')
        user_id = request.GET.get('user_id')
        if not comment_id or not user_id:
            return JsonResponse(fail_json_response("删除失败，缺失数据", "失败"))
        comment = Comments.objects.filter(id=comment_id).first()
        if not comment:
            return JsonResponse(fail_json_response("删除失败", "查询不到内容"))
        if comment.user_id != int(user_id):
            return JsonResponse(fail_json_response("删除失败，无法删除非个人评论", "失败"))
        comment.delete()
        return JsonResponse(success_json_response("删除成功", "删除成功"))


class UserLikeListAPI(APIView):
    def get(self, request, *args, **kwargs):
        """查询用户喜欢列表"""
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse(fail_json_response("缺失user_id", ""))

        user = Users.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse(fail_json_response("找不到用户", ""))

        likes = Likes.objects.filter(user_id=user.id).all()
        if not likes:
            return JsonResponse(success_json_response("成功", []))
        return_data = []
        for like in likes:
            work = Works.objects.filter(id=like.work_id).first()
            like = Likes.objects.filter(work_id=work.id).count()
            comment = Comments.objects.filter(work_id=work.id).count()
            mark = Marks.objects.filter(work_id=work.id).count()
            return_data.append(
                {
                    "id": work.id,
                    "title": work.title,
                    "work_type": work.work_type,
                    "description": work.description,
                    "image_url": work.image_url,
                    "content": work.content,
                    "video_url": work.video_url,
                    "created_at": work.created_at,
                    "view_count": work.view_count,
                    "like_count": like,
                    "comments_count": comment,
                    "mark_count": mark
                }
            )
        return JsonResponse(success_json_response("查询成功", return_data))


class UserMarkListAPI(APIView):
    def get(self, request, *args, **kwargs):
        """ 获取用户收藏列表 """
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse(fail_json_response("缺失user_id", ""))

        user = Users.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse(fail_json_response("找不到用户", ""))

        marks = Marks.objects.filter(user_id=user.id).all()
        if not marks:
            return JsonResponse(success_json_response("成功", []))
        return_data = []
        for mark in marks:
            work = Works.objects.filter(id=mark.work_id).first()
            like = Likes.objects.filter(work_id=work.id).count()
            comment = Comments.objects.filter(work_id=work.id).count()
            mark = Marks.objects.filter(work_id=work.id).count()
            return_data.append(
                {
                    "id": work.id,
                    "title": work.title,
                    "work_type": work.work_type,
                    "description": work.description,
                    "image_url": work.image_url,
                    "content": work.content,
                    "video_url": work.video_url,
                    "created_at": work.created_at,
                    "view_count": work.view_count,
                    "like_count": like,
                    "comments_count": comment,
                    "mark_count": mark
                }
            )
        return JsonResponse(success_json_response("查询成功", return_data))


class WorkMaxMarkQueryAPI(APIView):

    def get(self, request, *args, **kwargs):
        # 获取所有作品，获取所有作品的收藏数
        works_data = []
        works = Works.objects.all()
        for work in works:
            like = Likes.objects.filter(work_id=work.id).count()
            mark_count = Marks.objects.filter(work_id=work.id).count()
            comment = Comments.objects.filter(work_id=work.id).count()
            works_data.append(
                {
                    "id": work.id,
                    "title": work.title,
                    "work_type": work.work_type,
                    "description": work.description,
                    "image_url": work.image_url,
                    "content": work.content,
                    "video_url": work.video_url,
                    "created_at": work.created_at,
                    "view_count": work.view_count,
                    "like_count": like,
                    "comments_count": comment,
                    "mark_count": mark_count
                }
            )
        works_data.sort(key=lambda item: item['mark_count'], reverse=True)
        return JsonResponse(success_json_response("success", works_data))


class WorkMaxLikeQueryAPI(APIView):
    def get(self, request, *args, **kwargs):
        works_data = []
        works = Works.objects.all()
        for work in works:
            like_count = Likes.objects.filter(work_id=work.id).count()
            mark_count = Marks.objects.filter(work_id=work.id).count()
            comment = Comments.objects.filter(work_id=work.id).count()
            works_data.append(
                {
                    "id": work.id,
                    "title": work.title,
                    "work_type": work.work_type,
                    "description": work.description,
                    "image_url": work.image_url,
                    "content": work.content,
                    "video_url": work.video_url,
                    "created_at": work.created_at,
                    "view_count": work.view_count,
                    "like_count": like_count,
                    "comments_count": comment,
                    "mark_count": mark_count
                }
            )
        works_data.sort(key=lambda item: item['like_count'], reverse=True)
        return JsonResponse(success_json_response("success", works_data))
