# Traditional_Culture_Graduation

## 介绍
传统文化毕业设计

## 软件架构
### 软件架构说明

#### 实现功能

##### 用户侧

- 关于用户类
  - 登录 1
  - 注册 1
  - 个人信息查看 1
  - 个人信息修改 1
    - 基础信息 1
    - 密码 1

- 关于作品
  - 全作品展示 1
  - 作品检索 1
    - 标题搜索
  - 作品分类 
    - 视频、图文 
    - 传统文化分类 1 ?
  - 作品点赞 1
    - 点赞 1 
    - 取消点赞 1
  - 作品查看 1
  - 作品评论 1
    - 查看评论 1
    - 收藏评论 1
    - 删除自己的评论 1
  - 作品收藏 1
  - 查看视频 
  - 查看图文 1

##### 管理员
- 管理员属性
  - 登录 1
  - 注册新管理员 1
  - 修改管理员信息 
  - 查看管理员信息 1
  - 删除管理员 1
  - 管理员列表（查询所有管理员） 1
  - 用户列表 1
  - 用户查询（username查询） 1
  
- 作品管理
  - 新增作品 1
  - 删除作品 1
  - 修改作品 1
  - 作品列表展示 1
    - 分页 
    - 统计点赞数 1
    - 统计评论量 1
    - 统计收藏数 1
    - 查看评论 1
    - 删除评论 1
  - 上传图片 1
  - 上传视频 1

。
### 项目存储位置信息

前端项目在 font end 文件夹

后端项目在 back end文件夹



## 安装教程

### 1. 后端

pip清华源 `-i https://mirrors.aliyun.com/pypi/simple/`

1.  检查django有没有安装
    1.  `python -m django --version`

2.  创建django项目
    1.  `django-admin startproject mysite`

3.  安装第三方包 `pip install -r requiresment.txt -i https://mirrors.aliyun.com/pypi/simple/`

4.  新增apps接口包 `python manage.py startapp xxx`  # xxx为app名称



### 2. 前端

配置路径： `https://blog.csdn.net/majingbobo/article/details/134034891`

- 安装node.js
- 更换下载源 npm config get registry `npm config set registry https://registry.npmmirror.com`
- 配置 NPM 环境变量 `NPM_HOME`

## 使用说明
### 后端服务
1.  运行`python manage.py runserver`

### 前端服务
1.  

## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


## 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
