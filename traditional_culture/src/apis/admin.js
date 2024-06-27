import request from "@/utils/request";
//管理员用户方面接口
//管理员登陆
export const loginAPI=({username,password})=>request.post('/api/admin/login',{username,password,request_type:'login'})
//获取用户列表接口
export const getUserListAPI=()=>request.get('/user/list')
//新增用户
export const addUserAPI=(userData)=>request.post('/user/register',userData)
//删除用户
export const deleteUserAPI=(user_id)=>request.delete('/user/update/isbanned',{params:{user_id}})
//禁止用户
export const banUserAPI=(user_id)=>request.put('/user/update/isbanned',{user_id,request_type: "banned"})
//修改用户信息
export const updateUserInfoAPI=(data)=>request.put('/user/update/userinfo',data)
//修改头像
export const updateImgAPI=(data)=>request.post('/file/upload',data)
//搜索用户
export const serachUserAPI=(query_keyword)=>request.get('/user/list',{params:{query_keyword}})
//管理员管理管理员方面接口
//获取管理员列表
export const getAdminListAPI=()=>request.get('/api/admin/list')
//新增管理员
export const addAdminAPI=(adminData)=>request.post('/api/admin/register',adminData)
//删除管理员
export const deleteAdminAPI=(admin_id)=>request.delete('/api/admin/delete',{params:{admin_id}})
//修改管理员信息
export const updateAdminInfoAPI=(data)=>request.put('/api/admin/update/userinfo',data)
//根据管理员id获取管理员信息
export const getAdminInfoByIdAPI=(admin_id)=>request.get('/api/admin/info',{params:{admin_id}})



