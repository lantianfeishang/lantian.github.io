import { createRouter,createWebHistory } from "vue-router";
import Home from '../components/Home.vue';
import DiaryWeb from '../components/Diary/Web.vue';
import DiaryLearn from '../components/Diary/Learn.vue';
import DiaryTouhou from '../components/Diary/Touhou.vue'

const routes=[
    {
        path:'/',
        component:Home
    },
    {
        path:'/DiaryWeb',
        component:DiaryWeb
    },
    {
        path:'/DiaryLearn',
        component:DiaryLearn
    },
    {
        path:'/DiaryTouhou',
        component:DiaryTouhou
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router