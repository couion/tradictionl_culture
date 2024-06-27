import { defineStore } from "pinia";
import { loginAPI } from "@/apis/user";
import { ref } from "vue";
export const useUserStore = defineStore('user', () => {
  const userInfo = ref({})
  //登陆
  const getUserInfo = async ({ username, password }) => {
    const res = await loginAPI({ username, password })
    // console.log(res);
    userInfo.value = res.data.data
  }
  //退出清除信息
  const clearAdminInfo=()=>{
    userInfo.value ={}
  }
  // 3. 以对象的格式把state和action return
  return {
    userInfo,
    getUserInfo,
    clearAdminInfo
  }
},
{
  persist: true,
})