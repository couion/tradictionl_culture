
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PiniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import { Icon } from 'vant';
import App from './App.vue'
import router from './router'
import 'vant/lib/index.css';
//注册图标主件
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
//引入初始化样式文件
import '@/assets/styles/common.scss'
// 导入视频播放组件
import VueVideoPlayer from '@videojs-player/vue'
import 'video.js/dist/video-js.css'
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.use(Icon);
const pinia = createPinia()

app.use(pinia)
pinia.use(PiniaPluginPersistedstate)
app.use(pinia)
app.use(VueVideoPlayer)
app.use(router)

app.mount('#app')
