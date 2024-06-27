import { defineStore } from "pinia";
import { loginAPI } from "@/apis/admin";
import { ref } from "vue";
export const useAdminStore = defineStore('admin', () => {
  const adminInfo = ref({})
  //登陆
  const getAdminInfo = async ({ username, password }) => {
    const res = await loginAPI({ username, password })
    console.log(res);
    adminInfo.value = res.data.data
  }
  //退出清除信息
  const clearAdminInfo=()=>{
    adminInfo.value ={}
  }
  // 3. 以对象的格式把state和action return
  return {
    adminInfo,
    getAdminInfo,
    clearAdminInfo
  }
},
{
  persist: true,
})