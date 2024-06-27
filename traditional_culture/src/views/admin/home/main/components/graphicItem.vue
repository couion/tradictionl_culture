<script setup>
import { Delete, Edit } from '@element-plus/icons-vue'
import { defineProps } from 'vue'
import { deleteWorkByIdAPI, updateWorkAPI } from '@/apis/works'
import { updateImgAPI } from '@/apis/admin'

import { ref } from 'vue'
//获取父传来的数据
const props = defineProps({
  item: Object // 接收父组件传递的作品对象
})
//删除图文
const emits = defineEmits(['delete', 'edit']) // 声明删除事件
const handleDelete = async () => {
  await deleteWorkByIdAPI(props.item.id)
  emits('delete', props.item)
}
//修改图文
const editGraphicVisible = ref(false)

//修改图文表单数据
const editGraphicform = ref({
  work_id: props.item.id,
  work_type: props.item.work_type,
  title: props.item.title,
  worker: props.item.worker,
  description: props.item.description,
  image_url: props.item.img_url,
  content: props.item.content,
  video_url: props.item.video_url,
})
const handleInput = () => {
  // 将换行符转换为 <br> 标签
  editGraphicform.value.description = editGraphicform.value.description.replace(/\n/g, '<br>');
  editGraphicform.value.content = editGraphicform.value.content.replace(/\n/g, '<br>');

};
const handleEdit = () => {
  editGraphicVisible.value = true
  editGraphicform.value.work_id = props.item.id
}


//管理员修改图文
const editWork = async () => {
  const res = await updateWorkAPI(editGraphicform.value)
  editGraphicVisible.value = false//dialog隐藏
  emits('edit', props.item)
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
  editGraphicform.value.image_url=res.data.data.file_url
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
  editGraphicform.value.video_url=res.data.data.file_url
}
//默认图片
const defaultImagePath = '/src/assets/images/default.jpg'
</script>
<template>
  <div class="graphic-item">
    <div class="title">{{ item.title }}</div>
    <div class="msg">
      <div class="left-info" v-html="item.description"></div>
      <div class="right-img"><img :src="item.img_url|| defaultImagePath" alt=""></div>
    </div>
    <div class="handle">
      <el-button type="danger" :icon="Delete" circle @click="handleDelete()" />
      <el-button type="primary" :icon="Edit" circle @click="handleEdit()" />
    </div>
    <el-dialog v-model="editGraphicVisible" title="修改图文信息" width="500">
      <el-form :model="editGraphicform">
        <el-form-item label="类别" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="editGraphicform.work_type" autocomplete="off"
            placeholder="请输入类别" />
        </el-form-item>
        <el-form-item label="标题" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="editGraphicform.title" autocomplete="off" placeholder="请输入标题" />
        </el-form-item>
        <el-form-item label="作者" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="editGraphicform.worker" autocomplete="off"
            placeholder="请输入作者" />
        </el-form-item>
        <el-form-item label="描述" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="editGraphicform.description" autocomplete="off"
            placeholder="请输入描述" type="textarea" @input="handleInput" />
        </el-form-item>
        <el-form-item label="内容" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-model="editGraphicform.content" autocomplete="off" placeholder="请输入内容"
            type="textarea" @input="handleInput" />
        </el-form-item>
        <el-form-item label="封面" :label-width="formLabelWidth">
          <el-input style="margin-left: 14px;" v-show="false" v-model="editGraphicform.image_url" autocomplete="off"
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
          <el-input style="margin-left: 14px;" v-show="false" v-model="editGraphicform.video_url" autocomplete="off"
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
          <el-button @click="editGraphicVisible = false">取消</el-button>
          <el-button type="primary" @click="editWork">
            提交
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>
<style scoped lang='scss'>
.graphic-item {

  width: 360px;
  height: 200px;
  margin-right: 30px;
  margin-bottom: 20px;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;

  .title {
    padding: 10px;
    height: 20%;
    font-size: 18px;
  }

  .msg {
    display: flex;
    padding: 10px;
    height: 60%;

    .left-info {
      width: 50%;
      height: 100px;
      overflow: hidden;
    }

    .right-img {
      margin-left: 10px;
      width: 50%;

      img {
        height: 100%;
        width: 100%;
      }
    }
  }

  .handle {
    padding: 10px;
    height: 20%;
  }
}

.graphic-item:hover {

  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}
</style>