import request from "@/utils/request";
//用户方面接口
//用户登陆
export const loginAPI=({username,password})=>request.post('/user/login',{username,password,request_type:'login'})
//用户注册
export const registerAPI=({username,password})=>request.post('/user/login',{username,password,request_type:'register'})
//获取用户信息
export const getUserInfoByIdAPI=(user_id)=>request.get('/user/info',{params:{user_id}})

//用户点赞列表
export const getUserLikeListAPI=(user_id)=>request.get('/user/like/list',{params:{user_id}})
//用户收藏列表
export const getUserMarkListAPI=(user_id)=>request.get('/user/mark/list',{params:{user_id}})
//修改用户密码
export const updateUserPasswordAPI=(data)=>request.put('/user/update/password',data)

