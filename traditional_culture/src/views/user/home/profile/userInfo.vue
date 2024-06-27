<script setup>
import { ref } from 'vue';
// import { useRoute } from 'vue-router';
// import { RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user'
import { getUserInfoByIdAPI,updateUserPasswordAPI } from '@/apis/user'
import { updateImgAPI, updateUserInfoAPI } from '@/apis/admin'


//获取用户信息
const userStore = useUserStore()
const userInfoId = ref({})
userInfoId.value = userStore.userInfo.id
const userInfo = ref({})
const getUserInfoById = async () => {
  console.log(userInfoId.value);
  const res = await getUserInfoByIdAPI(userInfoId.value)
  userInfo.value = res.data.data
  console.log(res.data.data);
}
// onMounted(() => {
getUserInfoById()
// })
//上传头像
const updateImgFormVisible = ref(false)
const updateUserId = ref()
const handelUpdateImg = () => {
  updateUserId.value = userInfo.value.id
  console.log(updateUserId.value);
  updateImgFormVisible.value = true
}
const fileName = ref(null);
let file = null;
const beforeImageUpload = (fileObj) => {
  fileName.value = fileObj.name;
  file = fileObj;
  return false; // 阻止上传到服务器
};
const changeUserImg = async () => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('user_id', updateUserId.value);
  formData.append('request_type', 'user_photo_url');
  const res = await updateImgAPI(formData)
  alert(res.data.message)
  fileName.value = ''
  updateImgFormVisible.value = false
  window.location.reload();
};
//编辑用户信息
//编辑用户表单数据
const updateId = ref(null);
const updateform = ref({
  user_id: null,
  request_type: "user_info",
  username: '',
  phone: '',
  personal_info: ''
});
const editUser = () => {
  updateFormVisible.value = true;
  updateId.value = userInfo.value.id;
  updateform.value = {
    user_id: userInfo.value.id,
    request_type: "user_info",
    username: '',
    phone: '',
    personal_info: ''
  };
};

//编辑用户信息
const updateFormVisible = ref(false)
const updateUserInfo = async () => {
  const res = await updateUserInfoAPI(updateform.value)
  updateFormVisible.value = false
  alert(res.data.message)
  window.location.reload();
}
//修改用户密码
const updatePasswordVisible = ref(false)

const updatePassword = ref({
  user_id: null,
  request_type: "user_password",
  password: '',
  new_password: ''
});
const editUserPassword = () => {
  updatePasswordVisible.value = true;
  updateId.value = userInfo.value.id;
  updatePassword.value = {
    user_id: userInfo.value.id,
    request_type: "user_password",
    password: '',
    new_password: ''
  };
}
const updateUserPassword = async () => {
  const res = await updateUserPasswordAPI(updatePassword.value)
  updateFormVisible.value = false
  alert(res.data.message)
  window.location.reload();
}
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>
<template>
  <div class="container">
    <div class="img-name">
      <img :src="userInfo.photo_url ||defaultImagePath" alt="">
      <div class="user-info">
        <div class="user-name">{{ userInfo.username }}</div>
        <div class="user-personal-info">{{ userInfo.personal_info }}</div>
        <div class="user-phone">手机号码：{{ userInfo.phone }}</div>
        <!-- <div class="user-banner">账号状态：{{ userInfo.is_banned }}</div> -->
        <div class="user-banner">账号状态：
          <div style="width: 60px;text-align: center; display: inline-block; background-color: #e8ffe8; border-radius: 4px;" v-if="userInfo.is_banned===1">正常</div>
          <div style="width: 60px;text-align: center; display: inline-block; background-color: #808080;color: white; border-radius: 4px;" v-else>禁止</div>

        </div>

      </div>

    </div>
    <div class="handle">
      <div class="changImg"><el-button round @click="handelUpdateImg">修改头像</el-button></div>
      <div class="update-user-info"><el-button type="primary" plain @click="editUser">编辑信息</el-button></div>
      <div class="update-user-password"><el-button type="primary" plain @click="editUserPassword">修改密码</el-button></div>
    </div>
    <!-- 编辑用户信息 -->
    <el-dialog v-model="updateFormVisible" title="编辑用户信息" width="500">
      <el-form :model="updateform">
        <el-form-item label="用户名称" :label-width="formLabelWidth">
          <el-input v-model="updateform.username" autocomplete="off" placeholder="请输入用户名称" />
        </el-form-item>
        <el-form-item label="手机号码" :label-width="formLabelWidth">
          <el-input v-model="updateform.phone" autocomplete="off" oninput="value=value.replace(/^\d{12}$/,'')"
            placeholder="请输入11位手机号码" />
        </el-form-item>
        <el-form-item label="个人简介" :label-width="formLabelWidth">
          <el-input v-model="updateform.personal_info" autocomplete="off" placeholder="请输入个人简介" />
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="updateFormVisible = false">取消</el-button>
          <el-button type="primary" @click="updateUserInfo">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
    <!-- 编辑用户密码 -->
    <el-dialog v-model="updatePasswordVisible" title="修改用户密码" width="500">
      <el-form :model="updatePassword">
        <el-form-item label="原密码" :label-width="formLabelWidth">
          <el-input v-model="updatePassword.password" autocomplete="off" placeholder="请输入原密码" />
        </el-form-item>
        <el-form-item label="新密码" :label-width="formLabelWidth">
          <el-input v-model="updatePassword.new_password" autocomplete="off" placeholder="请输入新密码" />
        </el-form-item>

      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="updateFormVisible = false">取消</el-button>
          <el-button type="primary" @click="updateUserPassword">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
    <!-- 修改用户头像 -->
    <el-dialog v-model="updateImgFormVisible" title="修改用户头像" width="500">
      <el-upload class="dl-avatar-uploader-min square" :action="uploadUrl" :show-file-list="false"
        :on-success="handleUpImage" :before-upload="beforeImageUpload" list-type="picture" accept="image/*">
        <template v-if="!fileName">
          <el-icon>
            <Plus />
          </el-icon>
        </template>
        <div v-else>{{ fileName }}</div>
        <template #tip>
          <div class="el-upload__tip">只能上传图片,且单张图片大小不能超过10MB</div>
        </template>
      </el-upload>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="updateImgFormVisible = false">取消</el-button>
          <el-button type="primary" @click="changeUserImg">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>

  </div>
</template>

<style lang="scss" scoped>
.container {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  padding: 20px;
  margin-top: 20px;
  display: block;

  .img-name {
    display: flex;

    img {
      width: 100px;
      height: 100px;
    }

    .user-info {
      color: rgb(118, 116, 116);
      margin-left: 20px;
      // line-height: 180px;
      font-size: 18px;

      .user-name {
        font-weight: 600;
      }

      .user-personal-info {
        font-size: 16px;
      }
    }
  }

  .handle {
    margin-top: 10px;
    display: flex;

    .changImg {
      padding-left: 4px;
      padding-right: 20px;
    }
  }
}
</style>