<script setup>
import { onMounted, ref, reactive } from 'vue'
import { getAdminListAPI, addAdminAPI, deleteAdminAPI, updateAdminInfoAPI, updateImgAPI } from '@/apis/admin';
import { Edit, Delete,  } from '@element-plus/icons-vue'

const adminList = ref([])
//获取管理员列表
const getAdiminList = async () => {
  const res = await getAdminListAPI()
  adminList.value = res.data.data.results
  // console.log(res.data.data.results);
  console.log(adminList.value);
}
onMounted(() => getAdiminList())
//新增管理员弹出框
const addFormVisible = ref(false)
//新增管理员表单数据
const addform = reactive({
  username: '',
  password: '',
  register_username:'admin',
  request_type: 'register',
})
//管理员新增用户
const addAdmin = async () => {
  const res = await addAdminAPI(addform)
  addFormVisible.value = false//dialog隐藏
  getAdiminList()
  alert(res.data.message)
}
//编辑管理员表单数据
const updateId = ref(null);
const updateform = ref({
  user_id: null,
  request_type: "admin_info",
  username: '',
  phone: '',
  personal_info: ''
});
const editAdmin = (row) => {
  updateFormVisible.value = true;
  updateId.value = row.id;
  updateform.value = {
    admin_id: row.id,
    request_type: "admin_info",
    username: row.username,
    phone: row.phone,
    personal_info: row.personal_info
  };
};

//编辑管理员信息
const updateFormVisible = ref(false)
const updateAdminInfo = async () => {
  const res = await updateAdminInfoAPI(updateform.value)
  getAdiminList()
  updateFormVisible.value = false
  alert(res.data.message)
}

//删除管理员
const deleteAdmin = async (id) => {
  const res = await deleteAdminAPI(id)
  getAdiminList()
  alert(res.data.message)
}
//上传头像
const updateImgFormVisible = ref(false)
const updateAdminId = ref()
//点击头像事件
const updateAdminImg = (id) => {
  updateImgFormVisible.value = true
  updateAdminId.value = id
  console.log(id);
}
const fileName = ref(null);
let file = null;
const beforeImageUpload = (fileObj) => {
  fileName.value = fileObj.name;
  file = fileObj;
  return false; // 阻止上传到服务器
};
const changeAdminImg = async () => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('admin_id', updateAdminId.value);
  formData.append('request_type', 'admin_photo_url');
  const res = await updateImgAPI(formData)
  alert(res.data.message)
  fileName.value=''
  updateImgFormVisible.value = false
  getAdiminList()
};
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>


<template>
  <div>
    <div class="util">
      <div class="util-item">
        <div style="margin-right:40vw ;"><el-button type="primary" @click="addFormVisible = true">新增管理员</el-button>
        </div>
        <el-dialog v-model="addFormVisible" title="新增管理员账户" width="500">
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
              <el-button type="primary" @click="addAdmin">
                提交
              </el-button>
            </div>
          </template>
        </el-dialog>
        <div>
        </div>
      </div>
    </div>
    <el-table :data="adminList" style="width: 100%">
      <el-table-column prop="photo_url" label="头像" width="100">
        <template v-slot="{ row }">
          <div style="border-radius: 50%; overflow: hidden; width: 50px; height: 50px;"
            @click="updateAdminImg(row.id)">
            <img :src="row.photo_url ||defaultImagePath" alt="头像" style="width: 100%;height: 100%" />
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="username" label="用户名" width="100" />
      <el-table-column prop="personal_info" label="个人简介" width="200" />
      <el-table-column prop="phone" label="手机号码" width="180" />
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button type="primary" :icon="Edit" @click="editAdmin(row)" circle />
          <el-button type="danger" @click="deleteAdmin(row.id)" :icon="Delete" circle />
          <!-- <el-button type="info" @click="banUser(row.id)" :icon="Lock" circle /> -->
        </template>
      </el-table-column>
    </el-table>
    <el-dialog v-model="updateFormVisible" title="编辑管理员信息" width="500">
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
          <el-button type="primary" @click="updateAdminInfo">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
    <el-dialog v-model="updateImgFormVisible" title="修改管理员头像" width="500">
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
          <el-button type="primary" @click="changeAdminImg">
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