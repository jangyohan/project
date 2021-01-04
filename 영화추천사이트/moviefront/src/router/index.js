import Vue from 'vue'
import VueRouter from 'vue-router'

import Main from '@/views/Main.vue'

import LoginView from '@/components/Account/LoginView.vue'
import SignupView from '@/components/Account/SignupView.vue'
import ArticleDetail from '@/components/Article/ArticleDetail.vue'
import MovieDetail from '@/components/Movie/MovieDetail.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/main',
    name: 'Main',
    component: Main,    
  },  
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('auth-token')) {
        next('/')
      } else {
        next ()
      }
    }
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('auth-token')) {
        next('/')
      } else {
        next ()
      }
    }

  },
  {
    path: '/article/detail/:article_id',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props : true
  },
  {
    path: '/movie/detail/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail,
    props : true
  }

         
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
