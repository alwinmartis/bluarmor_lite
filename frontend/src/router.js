import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Master',
    component: () => import('@/pages/layout/master/master.vue'),
    children: [
      {
        path: '/new-target',
        name: 'CreateTarget',
        component: () => import('@/pages/Target.vue'),
      },
      {
        path: '/home',
        name: 'Home',
        component: () => import('@/pages/home.vue'),
      },
      {
        path: '/sales',
        name: 'Sales',
        component: () => import('@/pages/Sales.vue'),
      },
      {
        path: '/Dashboard',
        name: 'Dashboard',
        component: () => import('@/pages/Dashboard.vue'),
      },
      {
        path: '/add-target',
        name: 'NewTarget',
        component: () => import('@/pages/Newtarget.vue'),
      },
    ],
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }
  if (!isLoggedIn) {
    window.location.href = '/login?redirect-to=/store'
  }
  next()
})

export default router
