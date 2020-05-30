import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'

Vue.use(Router)


export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Main
        },
        {
            path: '/login',
            component: () => import('@/components/SignIn.vue')
        }
    ]
})