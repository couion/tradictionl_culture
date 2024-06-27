<script setup>
import {ref} from 'vue'
import titleNav from './components/titleNav.vue'
import containItem from './components/containItem.vue'
import {getWorkListAPI ,getMaxLikeAPI,getMaxMarkAPI} from '@/apis/works'
const workLList=ref([])
//获取图文列表
const getWorkList=async ()=>{
  const res=await getWorkListAPI()
  workLList.value=res.data.data
  console.log(workLList.value);
}
//最多点赞收藏
//最多点赞收藏
const maxLike=ref([])
const maxMark=ref([])
const getMaxLikeList=async ()=>{
  const res=await getMaxLikeAPI()
  maxLike.value=res.data.data
  console.log(maxLike.value);
}
const getMaxMarkList=async ()=>{
  const res=await getMaxMarkAPI()
  maxMark.value=res.data.data
  console.log(maxMark.value);
}
getWorkList()
getMaxLikeList()
getMaxMarkList()
</script>
<template>
  <div class="container">
    <div class="contain">
      <div class="left-contain">
        <titleNav>图&nbsp;文&nbsp;列&nbsp;表</titleNav>
        <containItem v-for="item in workLList" :key="item.id" :data="item"></containItem>

      </div>
      <div class="right-contain">
        <titleNav>最&nbsp;多&nbsp;收&nbsp;藏</titleNav>
        <ul>
          <li v-for="item in maxMark" :key="item.id"><a :href="'/detail/?id=' + item.id">{{item.title}}</a><span>收藏&nbsp;{{item.marks_count}}</span></li>

        </ul>
        <titleNav>最&nbsp;多&nbsp;点&nbsp;赞</titleNav>
        <ul>
          <li v-for="item in maxLike" :key="item.id"><a :href="'/detail/?id=' + item.id">{{item.title}}</a><span>点赞&nbsp;{{item.marks_count}}</span></li>

        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped lang='scss'>
.container {
  width: 80%;
  .banner {
    width: 100%;
    height: 400px;
  }

  .contain {
    margin-top: 10px;
    display: flex;
    height: 200px;

    .left-contain {
      width: 70%;
    }

    .right-contain {
      margin-left: 10px;
      width: 30%;

      // background-color: gray;
      ul {
        margin: 10px;
        font-size: 16px;

        li {
          padding-top: 10px;
          display: flex;
          align-items: center;
          a {
            width: 280px;
            /* 设置宽度 */
            display: inline-block;
            // /* 让链接元素成为块级元素，以便设置宽度 */
            overflow: hidden;
            /* 隐藏溢出内容 */
            white-space: nowrap;
            /* 防止文字换行 */
            text-overflow: ellipsis;
            /* 使用省略号表示溢出部分 */
          }

          span {
            display: inline-block;

          }
        }
      }
    }
  }
}


</style>