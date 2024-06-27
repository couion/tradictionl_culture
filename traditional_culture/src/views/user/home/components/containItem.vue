<script setup>
import { defineProps } from 'vue'
//获取父传来的数据
 defineProps({
  data: Object // 接收父组件传递的作品对象
})
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>
<template>
  <div class="contain-item">
    <div class="left-msg">
      <div class="title"><a :href="'/detail/?id=' + data.id">{{ data.title }}</a></div>
      <div class="create-time">{{ data.created_at }}</div>
      <div class="info" v-html="data.description">
      </div>
      <div class="comment">
        点赞&nbsp;{{ data.like_count }}&nbsp;&nbsp;收藏&nbsp;{{ data.mark_count }}&nbsp;&nbsp;观看量&nbsp;{{ data.view_count }}</div>
    </div>
    <div class="right-img">
      <img :src="data.img_url ||defaultImagePath" alt="">
    </div>
  </div>
</template>

<style lang="scss" scoped>
.contain-item {
  margin-top: 10px;
  height: 180px;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  display: flex;
  padding: 10px;

  .left-msg {
    width: 70%;
    height: 100%;

    .title {
      font-size: 18px;
      font-weight: 600;
    }

    .info {
      height: 80px;
      display: -webkit-box;
      -webkit-line-clamp: 4;
      /* 设置行数，这里假设显示3行 */
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: pre-wrap;
      word-wrap: break-word;
    }
  }

  .right-img {
    width: 30%;
    height: 100%;
    margin-left: 10px;

    img {
      width: 100%;
      height: 100%;
    }
  }


}

.contain-item:hover {

  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}
</style>