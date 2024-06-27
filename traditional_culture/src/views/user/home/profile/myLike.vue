<script setup>
import {ref} from 'vue'
import containItem from '../components/containItem.vue'
import {getUserLikeListAPI} from '@/apis/user'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const workLList=ref([])
const getUserLikeList=async()=>{
  const res=await getUserLikeListAPI(userStore.userInfo.id)
  workLList.value=res.data.data
  console.log(workLList.value);
}
getUserLikeList()
</script>
<template>
  <div class="container">
    <containItem v-for="item in workLList" :key="item.id" :data="item"></containItem>
  </div>
</template>

<style lang="scss" scoped>
.container{
  display: block;
  width: 70%;

}
</style>