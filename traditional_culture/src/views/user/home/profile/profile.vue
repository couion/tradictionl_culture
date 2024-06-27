<script setup>
import { useRoute } from 'vue-router';
import { RouterLink } from 'vue-router';

const route = useRoute();
</script>
<template>
  <div class="container">
    <div class="profile">
      <div class="profile-nav">
        <ul>
          <li :class="{ active: route.path === '/profile/userInfo' }"><router-link
              to="/profile/userInfo">个人信息</router-link></li>
          <li :class="{ active: route.path === '/profile/myLike' }"><router-link to="/profile/myLike">我的点赞</router-link>
          </li>
          <li :class="{ active: route.path === '/profile/myMark' }"><router-link to="/profile/myMark">我的收藏</router-link>
          </li>
        </ul>
      </div>
    </div>
    <RouterView />
  </div>
</template>

<style lang="scss" scoped>
.container {
  width: 80%;
  display: flex;
  .profile {
    .profile-nav {
      width: 100%;

      ul {
        justify-content: center;

        li {
          padding: 20px;
          font-size: 18px;
        }

        .active {
          color: aqua;
        }
      }
    }
  }
}
.active {
  border-bottom: 2px solid red;
}
</style>