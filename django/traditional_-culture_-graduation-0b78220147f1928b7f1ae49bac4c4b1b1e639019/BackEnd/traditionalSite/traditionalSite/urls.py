"""
URL configuration for traditionalSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Admins.views import AdminAPI, AdminListAPI
from Users.views import UsersAPI, UserListAPI
from Works.views import WorksAPI, WorkQueryAPI, operationForWorkByUserAPI, operationForCommentByUserAPI, \
    UserLikeListAPI, UserMarkListAPI
from commonUtil.StaticModuleAPI import FileUploadAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户
    path('user/info', UsersAPI.as_view(), name='用户模块（GET 根据ID获取用户信息）'),
    path('user/login', UsersAPI.as_view(), name='用户模块（POST 登录）'),
    path('user/register', UsersAPI.as_view(), name='用户模块（POST 注册'),
    path('user/update/userinfo', UsersAPI.as_view(), name='用户模块（PUT 用户修改基础信息)'),
    path('user/update/password', UsersAPI.as_view(), name='用户模块（PUT 用户修改密码）'),
    path('user/update/isbanned', UsersAPI.as_view(), name='用户模块（PUT 禁用用户）'),
    path('user/delete', UsersAPI.as_view(), name='用户模块（delete 删除用户）'),
    path('user/list', UserListAPI.as_view(), name='查询用户列表 get请求'),
    path("user/like/list", UserLikeListAPI.as_view(), name='get请求，查询用户点赞列表'),
    path("user/mark/list", UserMarkListAPI.as_view(), name='get请求，查询用户收藏列表'),

    # 作品
    path("works/list", WorksAPI.as_view(), name="作品模块（GET 获取作品列表）"),
    path("work/add", WorksAPI.as_view(), name="新增作品（POST请求）"),
    path("work/update", WorksAPI.as_view(), name="修改作品（PUT请求）； 删除作品（DELETE）"),
    path("work/delete", WorksAPI.as_view(), name="删除作品（DELETE)"),
    path("work/query", WorkQueryAPI.as_view(), name="作品检索 GET"),
    path("work/operation", operationForWorkByUserAPI.as_view(), name="点赞、收藏、评论 POST"),
    path("comment/operation", operationForCommentByUserAPI.as_view(), name="点赞、收藏评论（POST)"),
    path("comment/delete", operationForCommentByUserAPI.as_view(), name="删除评论（DELETE）"),
    path("file/upload", FileUploadAPI.as_view(), name="上传静态资源"),

    # 管理员
    path("api/admin/login", AdminAPI.as_view(), name="管理员登录 POST"),
    path("api/admin/register", AdminAPI.as_view(), name="管理员注册 POST"),
    path("api/admin/info", AdminAPI.as_view(), name="根据ID查询管理员信息 GET"),
    path("api/admin/update/userinfo", AdminAPI.as_view(), name="根据ID修改管理员信息 POST"),
    path("api/admin/update/password", AdminAPI.as_view(), name="根据ID修改管理员 POST"),
    path("api/admin/delete", AdminAPI.as_view(), name="根据ID删除管理员 DELETE"),
    path("api/admin/list", AdminListAPI.as_view(), name="查询管理员列表"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
