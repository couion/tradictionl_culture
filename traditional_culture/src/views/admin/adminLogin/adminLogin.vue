<script setup>
import { ref } from 'vue';
import {useRouter} from 'vue-router'
import {useAdminStore} from '@/stores/admin'
const adminStore=useAdminStore()

//formt表单数据
const form = ref({
  username: '',
  password: '',
  agree: true
})
//准备规则对象
const rules = {
  username: [
    { required: true, message: '用户名不能为空', trigger: 'blur' },
  ],
  password: [
    { required: true, message: '密码不能为空' },
    { min: 2, max: 24, message: '密码长度要求6-14个字符' }
  ],
  agree:[
    {
      validator: (rule, val, callback) =>{
        if(val){callback()}
        else{callback(new Error('请先同意协议'))}
      }
    }
  ]
}
const formRef=ref(null)
const router=useRouter()
const login=()=>{
  formRef.value.validate(async (valid)=>{
    const {username,password}=form.value
    //校验成功则执行
    if(valid){
      await adminStore.getAdminInfo({username,password})
      //跳转
      router.push({ path: '/admin' })

     
    }
  })
  }
</script>


<template>
  <div class="admin-login">
    <div class="left-img">
      <img src="@/assets/images/admin_login.jpg" alt="">
    </div>
    <div class="right-login-form">
      <div class="right-login-form-msg">
        <div class="title">后台管理系统登陆</div>
        <div class="login-form">
          <div style="text-align: center;padding: 30px 0; font-size: 20px;font-weight: 600;">管理员登陆</div>
          <el-form ref="formRef" label-position="right" label-width="60px" :model="form" :rules="rules" status-icon>
              <el-form-item label="账户" prop="username">
                <el-input v-model="form.username"/>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input v-model="form.password"/>
              </el-form-item>
              <el-form-item label-width="22px" prop="agree">
                <el-checkbox size="large" v-model="form.agree">
                  我已同意隐私条款和服务条款
                </el-checkbox>
              </el-form-item>
              <el-button size="large" class="subBtn" @click="login">点击登录</el-button>
            </el-form>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped lang='scss'>
.admin-login {
  display: flex;
  height: 100vh;

  .left-img {
    height: 100%;
    width: 50%;
    
    img {
      max-width: 100%;
      border-top-right-radius: 50px;
    }
  }

  .right-login-form {
    width: 50%;
    padding: 100px;

    .right-login-form-msg {

      .title {
        text-align: center;
        font-size: 30px;
        font-weight: 600;
      }

      .login-form {
        margin-top: 40px;
        height: 500px;
        .el-form{
          padding: 0 100px;
          .el-button{
            background-color: #2752FB;
            color: white;
            width: 200px;
            margin-left: 84px;
          }
        }
      }
    }

  }
}
</style>