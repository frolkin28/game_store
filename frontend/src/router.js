import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'

Vue.use(Router)

let router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Main
        },
        {
            path: '/login',
            component: () => import('@/components/SignIn.vue')
        },
        {
            path: '/sign_up',
            component: () => import('@/components/SignUp.vue')
        },
        {
            path: '/game/:uuid',
            component: () => import('@/components/GamePage.vue')
        },
        {
            path: '/card',
            component: () => import('@/components/Card.vue')
        }
    ]
})

// router.beforeEach((to, from, next) => {

// }_
// )

export default router;