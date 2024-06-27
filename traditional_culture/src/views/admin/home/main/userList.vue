<script setup>
import { onMounted, ref, reactive } from 'vue'
import { getUserListAPI, addUserAPI, deleteUserAPI, banUserAPI, updateImgAPI,updateUserInfoAPI, serachUserAPI } from '@/apis/admin';
import { Edit, Delete, Lock } from '@element-plus/icons-vue'

const userList = ref([])
//获取用户列表
const getUserList = async () => {
  const res = await getUserListAPI()
  userList.value = res.data.data.results
  // console.log(res.data.data.results);
  console.log(userList.value);
}
onMounted(() => getUserList())
//新增用户弹出框
const addFormVisible = ref(false)
//新增用户表单数据
const addform = reactive({
  username: '',
  password: '',
  request_type: 'register',
})
//管理员新增用户
const addUser = async () => {
  const res = await addUserAPI(addform)
  addFormVisible.value = false//dialog隐藏
  getUserList()
  alert(res.data.message)
}
//编辑用户表单数据
const updateId = ref(null);
const updateform = ref({
  user_id: null,
  request_type: "user_info",
  username: '',
  phone: '',
  personal_info: ''
});
const editUser = (row) => {
  updateFormVisible.value = true;
  updateId.value = row.id;
  updateform.value = {
    user_id: row.user_id,
    request_type: "user_info",
    username:row.username,
    phone: row.phone,
    personal_info: row.personal_info
  };
};

//编辑用户信息
const updateFormVisible = ref(false)
const updateUserInfo = async () => {
  const res = await updateUserInfoAPI(updateform.value)
  getUserList()
  updateFormVisible.value = false
  alert(res.data.message)
}

//删除用户
const deleteUser = async (id) => {
  const res = await deleteUserAPI(id)
  getUserList()
  alert(res.data.message)
}
//禁用/解锁账户
const banUser = async (id) => {
  console.log(id);
  const res = await banUserAPI(id)
  getUserList()
  alert(res.data.message)
}

//上传头像
const updateImgFormVisible = ref(false)
const updateUserId = ref()
//点击头像事件
const updateUserImg = (id) => {
  updateImgFormVisible.value = true
  updateUserId.value = id
  console.log(id);
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
  fileName.value=''
  updateImgFormVisible.value = false
  getUserList()
};
//搜索功能
const query_keyword = ref()
const searchUser = async () => {
  const res = await serachUserAPI(query_keyword.value)
  userList.value = res.data.data.results
  alert(res.data.message)
}
// 默认图片路径
const defaultImagePath = '/src/assets/images/default.jpg'
</script>


<template>
  <div>
    <div class="util">
      <div class="util-item">
        <div style="margin-right:40vw ;"><el-button type="primary" @click="addFormVisible = true">新增用户</el-button>
        </div>
        <el-dialog v-model="addFormVisible" title="新增用户" width="500">
          <el-form :model="addform">
            <el-form-item label="用户名" :label-width="formLabelWidth">
              <el-input v-model="addform.username" autocomplete="off" placeholder="请输入用户名称" />
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth">
              <el-input style="margin-left: 14px;" v-model="addform.password" autocomplete="off" placeholder="请输入密码" />
            </el-form-item>
          </el-form>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="addFormVisible = false">取消</el-button>
              <el-button type="primary" @click="addUser">
                提交
              </el-button>
            </div>
          </template>
        </el-dialog>
        <div>
          <el-form :model="query_keyword" label-width="auto" style="max-width: 600px">
            <el-form-item>
              <el-input v-model="query_keyword" />
            </el-form-item>
          </el-form>
        </div>
        <el-button type="primary" @click="searchUser"><el-icon>
            <Search />
          </el-icon>搜索用户</el-button>
      </div>
    </div>
    <el-table :data="userList" style="width: 100%">
      <el-table-column prop="photo_url" label="头像" width="100">
        <template v-slot="{ row }">
          <div style="border-radius: 50%; overflow: hidden; width: 50px; height: 50px;"
            @click="updateUserImg(row.user_id)">
            <img :src="row.photo_url || defaultImagePath" alt="头像" style="width: 100%;height: 100%" />
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="username" label="用户名" width="100" />
      <el-table-column prop="personal_info" label="个人简介" width="200" />
      <el-table-column prop="phone" label="手机号码" width="180" />
      <el-table-column prop="created_at" label="创建时间" width="180" />
      <el-table-column prop="is_banned" label="账号状态" width="100">
        <template v-slot="{ row }">
          <span v-if="row.is_banned === '1'"
            style="padding: 0 10px;background-color: gray;border-radius: 10px;color: white;">禁用</span>
          <span v-else style="padding: 0 10px;background-color: #E8FFE8;border-radius: 10px;">正常</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button type="primary" :icon="Edit" @click="editUser(row)" circle />
          <el-button type="danger" @click="deleteUser(row.user_id)" :icon="Delete" circle />
          <el-button type="info" @click="banUser(row.user_id)" :icon="Lock" circle />
        </template>
      </el-table-column>
    </el-table>
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

<style scoped lang='scss'>
.util {
  display: flex;
  align-items: center;
  height: 50px;

  .util-item {
    display: flex;
    padding-right: 200px;
  }
}
</style>