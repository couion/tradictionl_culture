## traditional - api

### 用户相关

#### 用户登录功能

地址：`http://localhost:8000/user/login`

请求: `POST`

数据结构：

`json`

```json
{
    "username": "admin1",  // 用户名
    "password": "admin1", // 密码
    "request_type": "login" // login
}
```

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,  // 返回状态码
    "status": "success", // 返回状态
    "message": "成功", // 信息
    "data": {  // 返回数据
        "id": 2  // 用户id
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "用户密码输入错误，请重新输入！",
    "data": "失败"
}
```





#### 用户注册

地址：`http://localhost:8000/user/register`

请求: `POST`

数据结构：

`json`

```json
{
    "username": "admin3",  // 用户名
    "password": "admin3", // 密码
    "request_type": "register" // login
}
```

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "注册成功",
    "data": {
        "id": 3
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "用户已存在，请重新输入用户名！",
    "data": "失败"
}
```



#### 用户信息获取 根据id

地址：`http://localhost:8000/user/info`

请求: `GET`

数据结构：QUERY `http://localhost:8000/user/info?user_id=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": {
        "id": 1,
        "username": "admin"
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```



#### 修改个人信息

地址：`http://localhost:8000/user/update/userinfo`

请求: `PUT`

数据结构：`json`

```json
{
    "user_id": 1, // 修改的用户id
    "request_type" : "user_info", // 修改的类型 用户信息
    "username": "admin1", // 修改后名称
    "phone": "13888888888", // 修改后手机号码
    "personal_info": "xxxxx我是后端，你是前端" // 个人简介
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "用户信息修改成功",
    "data": {
        "user_id": 1
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "用户名已存在，请重试",
    "data": "失败"
}
```



#### 修改用户密码

地址：`http://localhost:8000/user/update/password`

请求: `PUT`

数据结构：`json`

```json
{
    "user_id": 1, // 修改的用户id
    "request_type": "user_password", // 修改的类型 用户信息
    "password": "admin", // 账号原密码
    "new_password": "admin1" // 账号新密码
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "用户密码修改成功",
    "data": {
        "user_id": 1
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "原始密码输入错误",
    "data": "请重新输入"
}
```



#### 禁用账号

地址：`http://localhost:8000/user/update/isbanned`

请求: `PUT`

数据结构：`json`

```json
{
    "user_id": 1, // 修改的用户id
    "request_type": "banned" // 禁用账号
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "删除成功",
    "data": "删除成功"
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到该用户",
    "data": "失败"
}
```

#### 删除用户

地址：`http://localhost:8000/user/update/isbanned`

请求: `DELETE`

数据结构：`QUERY` `http://localhost:8000/user/update/isbanned?user_id=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "删除成功",
    "data": "删除成功"
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到该用户",
    "data": "失败"
}
```



#### 查询用户点赞列表

地址：`http://localhost:8000/user/like/list?user_id=1`

请求: `GET`

数据结构：`QUERY` `http://localhost:8000/user/like/list?user_id=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": [
        {
            "work_id": 1, // 文章id
            "title": "测试", // 文章标题
            "work_type": "文章", //文章类型
            "description": "测试描述",  //文章副标题
            "image_url": "测试地址", // 文章封面地址
            "content": "测试内容", // 文章正文
            "video_url": "测试地址", // 文章视频
            "created_at": "2024-04-08T16:10:13", // 创建时间
            "view_count": 2, // 文章阅读次数
            "like_count": 1, // 点赞数
            "comments_count": 3, // 评论数
            "marks_count": 0 // 收藏数
        }
    ]
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到该用户",
    "data": "失败"
}
```



#### 查询用户收藏列表

地址：`http://localhost:8000/user/mark/list?user_id=1`

请求: `GET`

数据结构：`QUERY` `http://localhost:8000/user/mark/list?user_id=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": [
        {
            "work_id": 1, // 文章id
            "title": "测试", // 文章标题
            "work_type": "文章", //文章类型
            "description": "测试描述",  //文章副标题
            "image_url": "测试地址", // 文章封面地址
            "content": "测试内容", // 文章正文
            "video_url": "测试地址", // 文章视频
            "created_at": "2024-04-08T16:10:13", // 创建时间
            "view_count": 2, // 文章阅读次数
            "like_count": 1, // 点赞数
            "comments_count": 3, // 评论数
            "marks_count": 0 // 收藏数
        }
    ]
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到该用户",
    "data": "失败"
}
```

#### 用户列表

地址：`http://localhost:8000/user/list`

请求: `GET`

数据结构：`QUERY` 

- 如果没有传递参数，为全量查询
- 如果有，为关键词查询
  - 可以查询 `username` 参数是 `query_keyword=xxxx`
  - 举例：`http://localhost:8000/user/list?query_keyword=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": {
        "count": 2,  // 条数
        "next": null, //下一页链接
        "previous": null, //上一页链接
        "results": [ //结果
            {
                "user_id": 2,
                "username": "admin1",  // 用户名
                "phone": "", // 手机号码
                "personal_info": "", // 个人简介
                "photo_url": "", // 头像地址
                "is_banned": "0",  // 是否被禁用 0为不被禁用 1为被禁用
                "created_at": "2024-04-09T15:50:34",  // 创建时间
                "updated_at": "2024-04-15T09:14:15" // 更新时间
            },
            {
                "user_id": 1,
                "username": "admin0",
                "phone": "13888888889",
                "personal_info": "xxxxx我是后端，你是前端",
                "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                "is_banned": "0",
                "created_at": "2024-04-08T16:43:24",
                "updated_at": "2024-04-15T09:41:25"
            }
        ]
    }
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```



### 管理员相关功能

#### 管理员登录

地址：`http://localhost:8000/api/admin/login`

请求: `POST`

数据结构：`JSON` 

```json
{
    "username": "admin",
    "password": "admin",
    "request_type": "login"
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "成功",
    "data": {
        "id": 1
    }
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```





#### 管理员注册

地址：`api/admin/register`

请求: `POST`

数据结构：`JSON` 

```json
{
    "username": "admin1",
    "password": "admin1",
    "register_username": "admin", // 注册人信息
    "request_type": "register"
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "注册成功",
    "data": {
        "id": 2
    }
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "用户已存在，请重新输入用户名！",
    "data": "失败"
}
```





#### 根据管理员id查询管理员信息

地址：`http://localhost:8000/api/admin/info?admin_id=1`

请求: `GET`

数据结构：`QUERY` 

- 举例： `http://localhost:8000/api/admin/info?admin_id=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": {
        "id": 1,
        "username": "admin",
        "phone": "",
        "personal_info": "",
        "photo_url": "http://localhost:8000/media/uploads/admin%E5%A4%B4%E5%83%8F1_sfA4WxV.png"
    }
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```





#### 根据管理员id修改管理员信息

地址：`http://localhost:8000/api/admin/update/userinfo`

请求: `PUT`

数据结构：`json`

```json
{
    "admin_id": 2, // 管理员id
    "username": "admin2", // 管理员的用户名
    "request_type": "admin_info",  // 固定
    "phone": "15888888886", // 管理员的手机号码
    "personal_info": "admin2修改" // 管理员的个人简介
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "用户信息修改成功",
    "data": {
        "admin_id": 2
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "用户名已存在，请重试",
    "data": "失败"
}
```



#### 根据管理员id修改管理员密码

地址：`http://localhost:8000/api/admin/update/password`

请求: `PUT`

数据结构：`json`

```json
{
    "admin_id": 2,
    "request_type": "admin_password",
    "new_password": "admin1",
    "password": "new_password"
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "用户密码修改成功",
    "data": {
        "admin_id": 2
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "原始密码输入错误",
    "data": "请重新输入"
}
```



#### 根据管理员id删除管理员

地址：`http://localhost:8000/api/admin/delete`

请求: `DELETE`

数据结构：`QUERY` `http://localhost:8000/api/admin/delete?admin_id=2`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "删除成功",
    "data": "删除成功"
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户信息",
    "data": "失败"
}
```



#### 查询管理员列表

地址：http://localhost:8000/api/admin/list

请求: `GET`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "username": "admin",
                "phone": "",
                "personal_info": "",
                "photo_url": "http://localhost:8000/media/uploads/admin%E5%A4%B4%E5%83%8F1_sfA4WxV.png"
            }
        ]
    }
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 





### 作品相关功能

#### 查询作品列表

地址：`http://localhost:8000/works/list`

请求: `GET`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "title": "测试",
                "work_type": "文章",
                "worker": "测试",
                "description": "测试描述",
                "img_url": "测试地址",
                "video_url": "测试地址",
                "created_at": "2024-04-08T16:10:13",
                "updated_at": "2024-04-09T14:04:10",
                "like_count": 1,
                "mark_count": 0,
                "comment_count": 3,
                "view_count": 2,
                "comment": [
                    {
                        "username": "admin0",
                        "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                        "content": "测试评论一下",
                        "comment_like_count": 1,
                        "comment_mark_count": 0,
                        "created_at": "2024-04-08T17:45:11",
                        "updated_at": "2024-04-08T17:45:11"
                    },
                    {
                        "username": "admin0",
                        "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                        "content": "测试评论一下",
                        "comment_like_count": 0,
                        "comment_mark_count": 1,
                        "created_at": "2024-04-08T17:46:14",
                        "updated_at": "2024-04-08T17:46:14"
                    },
                    {
                        "username": "admin0",
                        "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                        "content": "测试评论一下",
                        "comment_like_count": 1,
                        "comment_mark_count": 0,
                        "created_at": "2024-04-08T17:46:50",
                        "updated_at": "2024-04-08T17:46:50"
                    }
                ]
            }
        ]
    }
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 根据作品id查询作品信息

地址：`http://localhost:8000/work/query?work_id=1`

请求: `GET`  假设查询文章id=1的文章，如上链接

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": [
        {
            "id": 1,
            "title": "测试",
            "work_type": "文章",
            "worker": "测试",
            "description": "测试描述",
            "img_url": "测试地址",
            "video_url": "测试地址",
            "created_at": "2024-04-08T16:10:13",
            "updated_at": "2024-04-15T11:47:31.623",
            "like_count": 1,
            "mark_count": 0,
            "comment_count": 3,
            "view_count": 3,
            "comment": [
                {
                    "username": "admin0",
                    "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                    "content": "测试评论一下",
                    "comment_like_count": 1,
                    "comment_mark_count": 0,
                    "created_at": "2024-04-08T17:45:11",
                    "updated_at": "2024-04-08T17:45:11"
                },
                {
                    "username": "admin0",
                    "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                    "content": "测试评论一下",
                    "comment_like_count": 0,
                    "comment_mark_count": 1,
                    "created_at": "2024-04-08T17:46:14",
                    "updated_at": "2024-04-08T17:46:14"
                },
                {
                    "username": "admin0",
                    "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                    "content": "测试评论一下",
                    "comment_like_count": 1,
                    "comment_mark_count": 0,
                    "created_at": "2024-04-08T17:46:50",
                    "updated_at": "2024-04-08T17:46:50"
                }
            ]
        }
    ]
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 根据标题查询作品

地址：`http://localhost:8000/work/query?query_keyword=测试`

请求: `GET`  假设查询文章title=测试的文章，如上链接

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "查询成功",
    "data": [
        {
            "id": 1,
            "title": "测试",
            "work_type": "文章",
            "worker": "测试",
            "description": "测试描述",
            "img_url": "测试地址",
            "video_url": "测试地址",
            "created_at": "2024-04-08T16:10:13",
            "updated_at": "2024-04-15T11:47:32",
            "like_count": 1,
            "mark_count": 0,
            "comment_count": 3,
            "view_count": 3,
            "comment": [
                {
                    "username": "admin0",
                    "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                    "content": "测试评论一下",
                    "comment_like_count": 1,
                    "comment_mark_count": 0,
                    "created_at": "2024-04-08T17:45:11",
                    "updated_at": "2024-04-08T17:45:11"
                },
                {
                    "username": "admin0",
                    "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                    "content": "测试评论一下",
                    "comment_like_count": 0,
                    "comment_mark_count": 1,
                    "created_at": "2024-04-08T17:46:14",
                    "updated_at": "2024-04-08T17:46:14"
                },
                {
                    "username": "admin0",
                    "photo_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_GMgz54p.png",
                    "content": "测试评论一下",
                    "comment_like_count": 1,
                    "comment_mark_count": 0,
                    "created_at": "2024-04-08T17:46:50",
                    "updated_at": "2024-04-08T17:46:50"
                }
            ]
        }
    ]
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 对某作品进行点赞、收藏

地址：`http://localhost:8000/work/operation`

请求: `POST`   `json`

```json
{
    "work_id": 1,
    "user_id": 1,
    "request_type": "like" // like or mark
}
```



返回数据类型：

`json`

```json
// 成功
// 点赞
{
    "code": 200,
    "status": "success",
    "message": "点赞成功",
    "data": 6
}
// 收藏
{
    "code": 200,
    "status": "success",
    "message": "收藏成功",
    "data": 2
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 对某作品进行评论

地址：`http://localhost:8000/work/operation`

请求: `POST`   `json`

```json
{
    "work_id": 1,
    "user_id": 1,
    "comment_content": "你说的呢？确实不错",
    "request_type": "comment"
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "评论成功",
    "data": 5
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 删除本人评论的内容

地址：`http://localhost:8000/comment/operation`

请求: `delete`   `query` 

 `http://localhost:8000/comment/operation?comment_id=5&user_id=1`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "删除成功",
    "data": "删除成功"
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 对评论进行点赞、收藏

地址：`http://localhost:8000/comment/operation`

请求: `POST`   `json`

```json
{
    "comment_id": 4,
    "user_id": 1,
    "request_type": "like" // or mark
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "操作成功",
    "data": 4
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 



#### 上传文件（图片、视频）

地址：`http://localhost:8000/file/upload`

请求: `POST`   `form-data`

```json
{
    "file": "", // 文件对象
    "user_id": 1,
    "request_type": "user_photo_url" // 用户头像
}
```

- 上述的参数 `request_type` 可以为3种值
  - `user_photo_url`  表示 用户头像
  - `admin_photo_url ` 表示管理员头像
  - `空None`  表示其他的地址路径

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "上传成功",
    "data": {
        "file_url": "http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_WHVUSMo.png"
    }
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

####  新增作品

地址：`http://localhost:8000/work/add`

请求: `POST`   `json`

```json
{
    "work_type": "文章", //  作品类型
    "title": "中华传统文化是最优秀的",  //   作品标题
    "worker": "中华人民", //  作者
    "description": "中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的",  // 作品描述
    "image_url": "", // 封面图片（可为空
    "content": "中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的", // 正文内容
    "video_url": "" // 视频 （可为空
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "创建成功",
    "data": 2 // 文章id
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 修改作品

地址：`http://localhost:8000/work/update`

请求: `PUT`   `json`

```json
{
    "work_id": 2,
    "work_type": "文章", //  作品类型
    "title": "中华传统文化是最优秀的!!!",  //   作品标题
    "worker": "中华人民!!", //  作者
    "description": "中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的",  // 作品描述
    "image_url": "", // 封面图片（可为空
    "content": "中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的!!!", // 正文内容
    "video_url": "" // 视频 （可为空
}
```



返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "修改成功",
    "data": 2
}

// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 

#### 删除作品

地址：`http://localhost:8000/work/delete`

请求: `delete`   `query` 

 `http://localhost:8000/work/delete?work_id=3`

返回数据类型：

`json`

```json
// 成功
{
    "code": 200,
    "status": "success",
    "message": "删除成功",
    "data": "删除成功"
}
// 失败
{
    "code": 300,
    "status": "fail",
    "message": "查询不到用户",
    "data": "失败"
}
```

#### 