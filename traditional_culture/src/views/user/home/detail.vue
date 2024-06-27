<script setup>
import commentItem from './components/commentItem.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router';
import { getWorkDetailByIdAPI } from '@/apis/works'
import { useUserStore } from '@/stores/user'
import { getUserInfoByIdAPI } from '@/apis/user'
import { submitCommentAPI } from '@/apis/works'

const route = useRoute()
//视频路径
//
const videoSrc = ref();
//获取用户信息
const userStore = useUserStore()
const userInfoId = ref({})
userInfoId.value = userStore.userInfo.id
const userInfo = ref({})
const getUserInfoById = async () => {
  console.log(userInfoId.value);
  const res = await getUserInfoByIdAPI(userInfoId.value)
  userInfo.value = res.data.data

  // console.log(res.data.data);
}
onMounted(() => {
  getUserInfoById()
})
const workDetail = ref({})
//获取地址参数 
const work_id = ref(null);
work_id.value = route.query.id
console.log(work_id.value);
//获取详情
const getWorkDetailById = async () => {
  const res = await getWorkDetailByIdAPI(work_id.value)
  workDetail.value = res.data.data[0]
  videoSrc.value = res.data.data[0]
  console.log(res.data.data[0]);
  console.log(workDetail.value);
}

getWorkDetailById()
//发送评论
const commentText = ref()
const submitCommentText = ref({
  work_id: work_id.value,
  user_id: userInfoId.value,
  comment_content: commentText,
  request_type: "comment"
})
const subminComment = async () => {
  console.log(submitCommentText.value);
  const res = await submitCommentAPI(submitCommentText.value)
  console.log(res);
  getWorkDetailById()
}
//视频播放
let playerOptions = ref({
  // height: 200,
  // width: document.documentElement.clientWidth, //播放器宽度
  playbackRates: [0.7, 1.0, 1.5, 2.0], // 播放速度
  autoplay: 'any', // 如果true,浏览器准备好时开始回放。
  muted: true, // 默认情况下将会消除任何音频。
  loop: true, // 导致视频一结束就重新开始。
  preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
  language: 'zh-CN',
  aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
  fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
  notSupportedMessage: '此视频暂无法播放，请稍后再试', // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
  controls: true,
  controlBar: {
    timeDivider: true,
    durationDisplay: true,
    remainingTimeDisplay: false,
    fullscreenToggle: true // 全屏按钮
  }
})
//收藏
const starWork = async () => {
  submitCommentText.value = {
    work_id: work_id.value,
    user_id: userInfoId.value,
    comment_content: '',
    request_type: "mark"
  }
  await submitCommentAPI(submitCommentText.value)
  getWorkDetailById()
}
//点赞
const likeWork = async () => {
  submitCommentText.value = {
    work_id: work_id.value,
    user_id: userInfoId.value,
    comment_content: '',
    request_type: "like"
  }
  await submitCommentAPI(submitCommentText.value)
  getWorkDetailById()
}
//处理删除评论事件  点赞   收藏
const handleDeleteComment = () => {
  getWorkDetailById()
}
const handleLikeComment=()=>{
  getWorkDetailById()
}
const handleMarkComment=()=>{
  getWorkDetailById()
}
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>
<template>
  <div class="container">
    <div class="contain">
      <div class="title">
        {{ workDetail.title }}
      </div>
      <div class="article-info">
        <div class="publisher"><el-icon>
            <User />
          </el-icon>{{ workDetail.worker }}</div>
        <div class="publish-time"><el-icon>
            <Clock />
          </el-icon>{{ workDetail.updated_at }}</div>
        <div class="like-mark"><el-icon>
            <View />
          </el-icon>{{ workDetail.view_count }}&nbsp;&nbsp;<el-icon>
            <Star @click="starWork" />
          </el-icon>{{ workDetail.mark_count }}&nbsp;&nbsp;<el-icon>
            <ChatDotRound />
          </el-icon>{{ workDetail.comment_count }}&nbsp;&nbsp;</div>
        <van-icon name="like-o" style="line-height: 40px;" @click="likeWork">{{ workDetail.like_count }}</van-icon>
      </div>
      <div class="article-contain">
        <div class="img" style="margin-bottom: 10px;" v-if="workDetail.img_url"><img :src=workDetail.img_url alt="" style="width: 100%;height: 300px;"></div>
        <div class="video" v-if="workDetail.video_url">
          <video-player :src=workDetail.video_url :options="playerOptions" :volume="0.6" />
        </div>
        <div class="article" v-html="workDetail.content">
        </div>
      </div>
    </div>
    <div class="comment">
      <div class="user-comment">
        <img :src=userInfo.photo_url||defaultImagePath alt="">
        <input type="text" v-model="commentText" placeholder="欢迎您参加评论"><el-button round style="height: 100%;"
          @click="subminComment">发送</el-button>
      </div>
      <div class="comment-list">
        <commentItem v-for="item in workDetail.comment" :key="item" :data="item" @deleteComment="handleDeleteComment"
          @likeComment="handleLikeComment" @markComment="handleMarkComment"></commentItem>
      </div>
    </div>
  </div>
</template>

<style scoped lang='scss'>
.container {
  width: 80%;

  .contain {
    margin: 0 auto;
    width: 90%;
    padding: 30px;
    margin-top: 10px;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;

    .title {
      font-size: 20px;
      font-weight: 600;
    }

    .article-info {
      display: flex;

      .publish-img {
        width: 40px;
        height: 40px;
      }

      .publisher {
        display: flex;
        align-items: center;
        font-size: 14px;
      }

      .publish-time {
        display: flex;
        align-items: center;
        margin-left: 20px;
        font-size: 14px;
      }

      .like-mark {
        display: flex;
        align-items: center;
        margin-left: 20px;
        font-size: 14px;
      }

    }

    .article-contain {
      margin-top: 20px;

      .img {
        // height: 300px;
        width: 400px;
      }

      .video {
        margin-top: 4px;
        width: 70%;
        margin: 0 auto;
        // height: 400px;

        video {
          height: 80%;
          width: 100%;
        }
      }

      .article {
        width: 700px;
      }
    }
  }

  .comment {
    margin: 0 auto;
    width: 90%;
    padding: 30px;
    margin-top: 10px;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;

    .user-comment {
      height: 40px;
      // width: 40px;
      display: flex;

      img {
        width: 40px;
        height: 40px;
        border-radius: 10px;
      }

      input {
        margin-left: 20px;
        width: 300px;
        border: 1px #babcbe solid;
        border-radius: 10px;
      }
    }

    .comment-list {
      margin-top: 20px;
    }
  }
}
</style>