<script setup>
// import { useRouter } from 'vue-router'
// const router = useRouter()

</script>


<template>
  <div>
    <el-col :span="12">
      <el-menu :router="true" default-active="/admin/adminList" class="el-menu-vertical-demo" style="border-right: none" >
        <el-menu-item index="/admin/adminList">
          <el-icon><Avatar /></el-icon>
          <span>管理员账户管理</span>
        </el-menu-item>
        <el-menu-item index="/admin/userList">
          <el-icon><User /></el-icon>
          <span>用户管理</span>
        </el-menu-item>
        <el-menu-item index="/admin/graphicList">
          <el-icon><Picture/></el-icon>
          <span>图文管理</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </div>
</template>

<style scoped lang='scss'>
.el-col {
  max-width: 100%;
}
</style>