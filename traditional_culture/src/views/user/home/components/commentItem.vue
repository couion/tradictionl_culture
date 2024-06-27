<script setup>
import { defineProps } from 'vue'
import { deleteCommentByIdAPI ,likeMarkCommentByIdAPI} from '@/apis/works'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
console.log(userStore.userInfo.id);
//获取父传来的数据
const props = defineProps({
  data: Object // 接收父组件传递的作品对象
})
//删除评论
const emits = defineEmits(['delete','edit']) // 声明删除事件
const deleteComment = async () => {
  await deleteCommentByIdAPI({ comment_id: props.data.comment_id, user_id: userStore.userInfo.id })
  emits('deleteComment', props.item)
}
//点赞收藏评论
const markComment=async ()=>{
  await likeMarkCommentByIdAPI({comment_id: props.data.comment_id, user_id: userStore.userInfo.id ,request_type:'mark'})
  emits('markComment', props.item)
}
const likeComment=async ()=>{
  await likeMarkCommentByIdAPI({comment_id: props.data.comment_id, user_id: userStore.userInfo.id ,request_type:'like'})
  emits('likeComment', props.item)
}
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>
<template>
  <div class="comment-item">
    <div class="comment-publisher">
      <div class="publisher-img">
        <img :src="data.photo_url ||defaultImagePath" alt="">
      </div>
      <div class="publisher-name">{{ data.username }}</div>
    </div>
    <div class="comment-contain">
      {{ data.content }}
    </div>
    <div class="comment-create-time">发布时间&nbsp;&nbsp;&nbsp;{{ data.created_at }}</div>
    <div class="comment-handle">
      <van-icon name="star-o" :badge=data.comment_mark_count style="margin-right: 20px;" @click="markComment" />
      <van-icon name="like-o" :badge=data.comment_like_count style="margin-right: 20px;" @click="likeComment" />
      <van-icon name="delete-o" @click="deleteComment" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.comment-item {
  margin-bottom: 20px;

  .comment-publisher {
    display: flex;
    align-items: center;

    .publisher-img {
      img {
        width: 30px;
        height: 30px;
        border-radius: 50% 50%;
      }
    }

    .publisher-name {
      margin-left: 20px;
      font-size: 16px;
      font-weight: 550;
    }
  }

  .comment-contain {
    padding-top: 10px;
    padding-left: 50px;
    font-size: 16px;
    width: 600px;
    // display: -webkit-box;
    // -webkit-line-clamp: 3;
    // /* 设置行数，这里假设显示3行 */
    // -webkit-box-orient: vertical;
    // overflow: hidden;
    // text-overflow: ellipsis;
    // white-space: pre-wrap;
    // word-wrap: break-word;
  }

  .comment-create-time {
    padding-top: 10px;
    padding-left: 50px;
    font-size: 16px;
  }

  .comment-handle {
    padding-top: 4px;
    padding-left: 50px;
    font-size: 16px;
  }
}
</style>