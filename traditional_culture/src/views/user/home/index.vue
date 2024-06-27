<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user'
import { getUserInfoByIdAPI } from '@/apis/user'
const route = useRoute();
const userStore = useUserStore()
const userInfoId = ref({})
userInfoId.value = userStore.userInfo.id
const userInfo = ref({})
//获取用户信息
const getUserInfoById = async () => {
  console.log(userInfoId.value);
  const res = await getUserInfoByIdAPI(userInfoId.value)
  userInfo.value = res.data.data
  console.log(res.data.data);
}
onMounted(() => {
  getUserInfoById()
})

const logout = async () => {
  await userStore.clearAdminInfo()
  window.location.reload();
}
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>
<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <div class="top">
          <div class="logo">
            <img src="https://cn.chinaculture.org/portal/site/wenhua/images/logo.jpg" alt="">
          </div>
          <div class="userLogin" v-if="userInfoId">
            <div class="user-username">{{ userInfo.username }}</div>
            <div class="user-photo"><img
                :src="userInfo.photo_url || defaultImagePath" alt=""></div>
            <div class="admin-logout"><el-icon style="font-size: 24px;cursor:pointer" @click="logout" title="退出登录">
                <SwitchButton />
              </el-icon>
            </div>
          </div>
          <div class="no-login" v-else><router-link to="/user/login">请先登录</router-link></div>

        </div>
      </el-header>
      <div class="menu">
        <div class="container">
          <ul>
            <li :class="{ active: route.path === '/home' }"><router-link to="/home">首页</router-link></li>
            <li :class="{ active: route.path === '/article' }"><router-link to="/article">图文列表</router-link></li>
            <li :class="{ active: route.path === '/like' }"><router-link to="/like">最多点赞</router-link></li>
            <li :class="{ active: route.path === '/favorite' }"><router-link to="/favorite">最多收藏</router-link></li>
            <li
              :class="{ active: route.path === '/profile' || route.path === '/profile/myMark' || route.path === '/profile/myLike' || route.path === '/profile/userInfo' }">
              <router-link to="/profile">个人中心</router-link>
            </li>
          </ul>
        </div>
      </div>
      <el-main>

        <RouterView />
 
      </el-main>
    </el-container>
  </div>


</template>

<style scoped lang='scss'>
.common-layout {
  height: 100vh;

  .el-container {
    height: 100%;

    .el-header {
      width: 80%;
      margin: 0 auto;
      margin-bottom: 10px;

      .top {
        display: flex;
        justify-content: space-between;

        .logo {
          img {
            max-height: 100%;
          }
        }

        .userLogin {
          margin-left: auto;
          display: flex;

          .user-username {
            padding-top: 20px;
            margin-right: 30px;
            font-size: 18px;
          }

          .user-photo {
            width: 60px;
            height: 60px;

            img {
              width: 100%;
              height: 100%;
              border-radius: 30px;

            }
          }
        }

        .no-login {
          text-align: center;
          line-height: 70px;
          font-size: 16px;
        }

        .admin-logout {
          padding: 20px;
        }
      }
    }

    .menu {
      border-top: 1px solid #cdcccc;
      border-bottom: 1px solid #cdcccc;
      height: 40px;

      .container {
        width: 76%;
        height: 100%;

        ul {
          height: 100%;
          padding-top: 4px;

          li {
            position: relative;
            top: 0;
            left: 0;
            display: inline-block;
            width: 20%;
            text-align: center;
            height: 30px;
            cursor: pointer;
            font-size: 20px;
            height: 100%;
          }
        }
      }
    }

    .el-main {
      overflow: visible;
    }
  }
}


.active {
  border-bottom: 2px solid red;
}
</style>