import request from "@/utils/request";
//获取图文列表
export const getWorkListAPI = () => request.get('/works/list')
//删除图文
export const deleteWorkByIdAPI = (work_id) => request.delete('/work/delete', { params: { work_id } })
//获取图文详情
export const getWorkDetailByIdAPI = (work_id) => request.get('/work/query', { params: { work_id } })
//对作品评论或点赞收藏 注意request_type字段
export const submitCommentAPI = (data) => request.post('/work/operation', data)
//添加作品
export const addWorkAPI = (data) => request.post('/work/add', data)
//修改作品
export const updateWorkAPI = (data) => request.put('/work/update', data)
//获取最多点赞
export const getMaxLikeAPI = () => request.get('/works/max/like')
//获取最多收藏
export const getMaxMarkAPI = () => request.get('/works/max/mark')

//删除自己发布的评论
export const deleteCommentByIdAPI = ({comment_id,user_id}) => request.delete('/comment/operation', { params: {comment_id, user_id } })
//点赞收藏评论
export const likeMarkCommentByIdAPI = (data) => request.post('/comment/operation', data)









