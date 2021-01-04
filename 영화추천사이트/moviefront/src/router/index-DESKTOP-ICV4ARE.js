import Vue from 'vue'
import VueRouter from 'vue-router'
// import MovieView from '@/components/Movie_/MovieView.vue'
import MovieSearch from '@/components/Movie_/MovieSearch.vue'

import LoginView from '@/components/Account/LoginView.vue'
import SignupView from '@/components/Account/SignupView.vue'
import Test from '@/components/Test/Test.vue'
import Test2 from '@/components/Test/Test2.vue'
import AllMovie from '@/components/Movie/AllMovie.vue'


import ArticleList from '@/components/Article/ArticleList.vue'
import ArticleCreate from '@/components/Article/ArticleCreate.vue'
import ArticleDetail from '@/components/Article/ArticleDetail.vue'

import MovieCreate from '@/components/Movie/MovieCreate.vue'
import MovieDetail from '@/components/Movie/MovieDetail.vue'

Vue.use(VueRouter)

  const routes = [
    {
      path: '/test',
      name: 'Test',
      component: Test
    },    
    {
      path: '/test2',
      name: 'Ttest2',
      component: Test2
    },      
  {
    path: '/index',
    name: 'MovieView',
    component: MovieSearch
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
    path: '/all',
    name: 'AllMovie',
    component: AllMovie
  },  
  {
    path: '/article',
    name: 'ArticleList',
    component: ArticleList,
    props : true
  },
  {
    path: '/article/create',
    name: 'ArticleCreate',
    component: ArticleCreate,
    props : true
    
  },
  {
    path: '/article/detail/:article_id',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props : true
  },
  {
    path: '/movie/create',
    name: 'MovieCreate',
    component: MovieCreate
  },
  {
    path: '/movie/detail/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true
  }      
         

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
