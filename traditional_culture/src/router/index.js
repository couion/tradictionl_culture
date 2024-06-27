import { createRouter, createWebHistory } from 'vue-router'
// 
import {useAdminStore} from '@/stores/admin'
import {useUserStore} from '@/stores/user'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/user/login',
      name: 'login',
      component: () => import('@/views/user/login/index.vue'),
    },
    {
      path: '/',
      name: '',
      redirect: '/home', // 添加重定向规则
      component: () => import('@/views/user/home/index.vue'),
      children: [
        {
          path: '/home',
          name: 'home',
          component: () => import('@/views/user/home/home.vue'),
        },
        {
          path: '/article',
          name: 'article',
          component: () => import('@/views/user/home/article.vue'),
        },
        {
          path: '/like',
          name: 'like',
          component: () => import('@/views/user/home/like.vue'),
        },
        {
          path: '/favorite',
          name: 'favorite',
          component: () => import('@/views/user/home/favorite.vue'),
        },
        {
          path: '/profile',
          name: 'profile',
          component: () => import('@/views/user/home/profile/profile.vue'),
          children: [
            {
              path: '/profile/myLike',
              name: 'myLike',
              component: () => import('@/views/user/home/profile/myLike.vue'),
            },
            {
              path: '/profile/myMark',
              name: 'myMark',
              component: () => import('@/views/user/home/profile/myMark.vue'),
            },
            {
              path: '/profile/userInfo',
              name: 'userInfo',
              component: () => import('@/views/user/home/profile/userInfo.vue'),
            },
          ],
          beforeEnter: (to, from, next) => {
            const userStore = useUserStore()
            // 在这里检查用户是否登录
            const isLoggedIn = userStore.userInfo.id/* 这里检查用户是否登录的逻辑，例如从 store 中获取登录状态 */
            if (!isLoggedIn) {
              // 如果用户未登录，重定向到用户登录页面
              next('/user/login');
            } else {
              // 如果用户已经登录，继续正常导航
              next();
            }
          }
        },
        {
          path: '/detail',
          name: 'detail',
          component: () => import('@/views/user/home/detail.vue'),
        },
      ]
    },
    {
      path: '/admin/login',
      name: 'adminLogin',
      component: () => import('@/views/admin/adminLogin/adminLogin.vue'),
    },
    {
      path: '/admin',
      name: 'adminPage',

      component: () => import('@/views/admin/home/index.vue'),
      children: [
        {
          path: '/admin/adminList',
          name: 'adminList',
          component: () => import('@/views/admin/home/main/adminList.vue'),
        },
        {
          path: '/admin/userList',
          name: 'userList',
          component: () => import('@/views/admin/home/main/userList.vue'),
        },
        {
          path: '/admin/graphicList',
          name: 'graphicList',
          component: () => import('@/views/admin/home/main/graphicList.vue'),
        },
      ],
      beforeEnter: (to, from, next) => {
        const adminStore = useAdminStore()
        // 在这里检查用户是否登录
        const isLoggedIn = adminStore.adminInfo.id/* 这里检查用户是否登录的逻辑，例如从 store 中获取登录状态 */
        if (!isLoggedIn) {
          // 如果用户未登录，重定向到用户登录页面
          next('/admin/login');
        } else {
          // 如果用户已经登录，继续正常导航
          next();
        }
      }
    },

  ]
})

export default router
