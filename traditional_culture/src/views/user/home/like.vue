<script setup>
import titleNav from './components/titleNav.vue'
import containItem from './components/containItem.vue'
import {ref} from 'vue'
import {getMaxMarkAPI,getMaxLikeAPI} from '@/apis/works'
const workLList=ref([])
//获取最多点赞图文列表
const getMaxLike=async ()=>{
  const res=await getMaxLikeAPI()
  workLList.value=res.data.data
  console.log(workLList.value);
}
getMaxLike()

//最多点赞收藏
const maxMark=ref([])

const getMaxMarkList=async ()=>{
  const res=await getMaxMarkAPI()
  maxMark.value=res.data.data
  console.log(maxMark.value);
}
getMaxMarkList()
</script>
<template>
  <div class="container">
    <div class="contain">
      <div class="left-contain">
        <titleNav>最&nbsp;多&nbsp;点&nbsp;赞</titleNav>
        <containItem v-for="item in workLList" :key="item.id" :data="item"></containItem>
      </div>
      <div class="right-contain">
        <titleNav>最&nbsp;多&nbsp;收&nbsp;藏</titleNav>
        <ul>
          <li v-for="item in maxMark" :key="item.id"><a :href="'/detail/?id=' + item.id">{{item.title}}</a><span>收藏&nbsp;{{item.mark_count}}</span></li>

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