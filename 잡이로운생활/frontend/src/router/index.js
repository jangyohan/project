import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Video from '../views/Video.vue'
import Resume from '../views/Resume.vue'
import ResumeEdit from '../views/ResumeEdit.vue'
import RecruitHome from '../views/RecruitHome.vue'
import RecruitWrite from '../views/RecruitWrite.vue'
import Applicant from '../views/Applicant.vue'
import Mypage from '../views/Mypage.vue'
import Search from '../views/Search.vue'
import OtherResume from '../views/OtherResume.vue'
import Mycontract from '../views/MyContract.vue'
import Calendar from '../views/Calendar.vue'
import axios from 'axios';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/';

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('auth-token')) {
        const config = {
          headers: {
            Authorization: `Token ${Vue.$cookies.get('auth-token')}`
          },
        }
        axios.post(`${SERVER_URL}accounts/`, null, config)
        .then((res)=>{
          if(res.data.flag===0) {
            next('/corp/recruit')
          } else {
            next()
          }
        })
        .catch(()=>{
        });
      } else {
        next()
      }    }  
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('auth-token')) {
        next('/')
      } else {
        next()
      }    }
  },
  {
    path: '/resume',
    name: 'Resume',
    component: Resume,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/resume/edit',
    name: 'ResumeEdit',
    component: ResumeEdit,
    props: true,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/video',
    name: 'Video',
    component: Video,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/corp/recruit',
    name: 'RecruitHome',
    component: RecruitHome,
    props: true,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/corp/recruit/write',
    name: 'RecruitWrite',
    component: RecruitWrite,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/corp/recruit/applicant/:recruitID',
    name: 'Applicant',
    component: Applicant,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/otherresume/:id',
    name: 'OtherResume',
    component: OtherResume,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  },
  {
    path: '/mycontract',
    name: 'MyContract',
    component: Mycontract
  },
  {
    path: '/calendar',
    name: 'Calendar',
    component: Calendar,
    beforeEnter(to, from, next) {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/login')
      } else {
        next()
      }    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
