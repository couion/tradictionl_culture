<script setup>
import { ref } from 'vue';
import { RouterView } from 'vue-router'
import leftMenu from "@/views/admin/home/leftMenu/index.vue"
import { useRouter } from 'vue-router'
import { useAdminStore } from '@/stores/admin'
import {getAdminInfoByIdAPI} from '@/apis/admin.js'
const adminStore = useAdminStore()
const router = useRouter()
const adminInfo=ref({})
//获取登陆的管理员信息
const getAdminInfoById=async()=>{
  const res=await getAdminInfoByIdAPI(adminStore.adminInfo.id)
  adminInfo.value=res.data.data
  console.log(res.data.data);
}
getAdminInfoById()
//管理员退出
const logout = () => {
  //清空pinia数据
  adminStore.clearAdminInfo()
  router.push('/admin/login')
}
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>


<template>
  <div class="admin-home">
    <el-container style="height: 100vh;">
      <el-header style="
        box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);display: flex;">
        <div class="top-head">后台管理系统</div>
        <div class="top-head-msg">
          <div class="admin-name">{{adminInfo.username}}</div>
          <div class="admin-img"><img :src="adminInfo.photo_url || defaultImagePath" alt=""></div>
          <div class="admin-logout"><el-icon style="font-size: 24px;cursor:pointer" @click="logout" title="退出登录">
              <SwitchButton />
            </el-icon></div>
        </div>
      </el-header>
      <el-container style="height:80vh">
        <el-aside width="200px" style="border-right: 1px solid var(--el-menu-border-color);padding-top: 20px;">
          <leftMenu></leftMenu>
        </el-aside>
        <el-main style="background-color: #f5f6fa;">
          <RouterView />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped lang='scss'>
.admin-home {
  .top-head {
    width: 180px;
    border-right: 1px solid #dcdfe6;
    text-align: center;
    padding-top: 14px;
    color: #c9c9c9;
    font-size: 20px;
  }

  .top-head-msg {
    display: flex;
    align-items: center;
    margin-left: auto;

    .admin-name {
      margin: 0 10px;
      font-size: 16px;
    }

    .admin-img {
      width: 50px;
      height: 50px;
      margin: 0 10px;
      border-radius: 50% 50%;

      img {
        width: 100%;
        height: 100%;
        border-radius: 50% 50%;
      }
    }

    .admin-logout {
      margin: 0 10px;
    }
  }
}
</style>