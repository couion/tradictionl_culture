<script setup>
import graphicItem from './components/graphicItem.vue'
import { ref } from 'vue'
import { getWorkListAPI, addWorkAPI } from '@/apis/works'
import { updateImgAPI } from '@/apis/admin'

const data = ref([])
const getWorkList = async () => {
  const res = await getWorkListAPI()
  // console.log(res.data.data);
  data.value = res.data.data
  console.log(data.value);
}
getWorkList()
const handleDelete = (deletedItem) => {
  console.log('Deleted item:', deletedItem)
  getWorkList()
  // 在这里处理删除的作品对象
}
const handleEdit = () => {
  getWorkList()
  // 在这里处理删除的作品对象
}

//新增图文
const addGraphicVisible = ref(false)
//新增图文表单数据
const addGraphicform = ref({
  work_type: '',
  title: '',
  worker: '',
  description: '',
  image_url: '',
  content: '',
  video_url: '',
})
const reset=()=>{
  addGraphicform.value.work_type=''
  addGraphicform.value.title=''
  addGraphicform.value.worker=''
  addGraphicform.value.description=''
  addGraphicform.value.image_url=''
  addGraphicform.value.content=''
  addGraphicform.value.video_url=''
}
const handleInput = () => {
      // 将换行符转换为 <br> 标签
      addGraphicform.value.description = addGraphicform.value.description.replace(/\n/g, '<br>');
      addGraphicform.value.content = addGraphicform.value.content.replace(/\n/g, '<br>');

    };
//管理员新增图文
const addWork = async () => {
  const res = await addWorkAPI(addGraphicform.value)
  addGraphicVisible.value = false//dialog隐藏
  getWorkList()
  reset()
  alert(res.data.message)
}
//上传文件路径
const imgFileName = ref(null);
let imgFile = null;
const beforeImageUpload = (fileObj) => {
  imgFileName.value = fileObj.name;
  imgFile = fileObj;
  return true; // 阻止上传到服务器
};
const uploadImgFile = async () => {
  const formData = new FormData();
  await formData.append('file', imgFile);
  await formData.append('user_id', '');
  await formData.append('request_type', '');
  const res = await updateImgAPI(formData)
  addGraphicform.value.image_url=res.data.data.file_url
}
const videoFileName = ref(null);
let videoFile = null;
const beforeVideoUpload = (fileObj) => {
  videoFileName.value = fileObj.name;
  videoFile = fileObj;
  return true; // 阻止上传到服务器
};
const uploadVideoFile = async () => {
  const formData = new FormData();
  await formData.append('file', videoFile);
  await formData.append('user_id', '');
  await formData.append('request_type', '');
  const res = await updateImgAPI(formData)
  addGraphicform.value.video_url=res.data.data.file_url
}



</script>


<template>
  <div>
    <div style="margin-right:40vw;margin-bottom: 10px;"><el-button type="primary"
        @click="addGraphicVisible = true">新增图文</el-button></div>
    <div style="display: flex;flex-wrap: wrap;">
      <graphicItem v-for="item in data" :key="item.id" :item="item" @delete="handleDelete" @edit="handleEdit"></graphicItem>
    </div>
    <el-dialog v-model="addGraphicVisible" title="新增图文" width="500">
      <el-form :model="addGraphicform">
        <el-form-item label="类别" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="addGraphicform.work_type" autocomplete="off"
            placeholder="请输入类别" />
        </el-form-item>
        <el-form-item label="标题" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="addGraphicform.title" autocomplete="off" placeholder="请输入标题" />
        </el-form-item>
        <el-form-item label="作者" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="addGraphicform.worker" autocomplete="off" placeholder="请输入作者" />
        </el-form-item>
        <el-form-item label="描述" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="addGraphicform.description" autocomplete="off"
            placeholder="请输入描述" type="textarea" @input="handleInput"/>
        </el-form-item>
        <el-form-item label="内容" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="addGraphicform.content" autocomplete="off"
            placeholder="请输入内容" type="textarea" @input="handleInput"/>
        </el-form-item>
        <el-form-item label="封面" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-show="false" v-model="addGraphicform.image_url" autocomplete="off"
            placeholder="请输入封面网址" />
          <el-upload class="dl-avatar-uploader-min square" action="#" :show-file-list="false"
            :on-success="handleUpImage" :before-upload="beforeImageUpload" @change="uploadImgFile" list-type="picture"
            accept="image/*">
            <template v-if="!imgFileName">
              <el-icon>
                <Plus />
              </el-icon>
            </template>
            <div v-else>{{ imgFileName }}</div>
          </el-upload>
        </el-form-item>
        <el-form-item label="视频" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-show="false" v-model="addGraphicform.video_url" autocomplete="off"
            placeholder="请输入视频网址" />
            <el-upload class="dl-avatar-uploader-min square" action="#" :show-file-list="false"
            :on-success="handleUpImage" :before-upload="beforeVideoUpload" @change="uploadVideoFile" list-type="picture"
            accept="image/*">
            <template v-if="!videoFileName">
              <el-icon>
                <Plus />
              </el-icon>
            </template>
            <div v-else>{{ videoFileName }}</div>
          </el-upload>
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="addGraphicVisible = false">取消</el-button>
          <el-button type="primary" @click="addWork">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>


</template>

<style scoped lang='scss'></style>