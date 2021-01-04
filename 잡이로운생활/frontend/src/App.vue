<template>
  <div id="app">
    <div v-show="!isLogin">
      <div class="nav" v-if="UserInfo.flag===0">
        <div class="logo-box" @click="goCorpHome">
          <img class="logo-img" src="./assets/logo/B104_logo_basic_skyblue.png" alt="">
        </div>
        <div class="menu-bar-box">
          <div v-show="isLoggedIn" class="menu-bar" @click="goRecruit">공고관리</div>
        </div>
        <div class="user-box">
          <div v-show="isLoggedIn" class="user-name-bar">{{ UserInfo.last_name }}님 환영합니다</div>
          <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('login')">로그인</div>
          <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('signup')">회원가입</div>
          <div v-show="isLoggedIn" class="user-bar" @click="goLogout">로그아웃</div>
        </div>
      </div>
      <div class="nav" v-else>
        <div class="logo-box" @click="goHome">
          <img class="logo-img" src="./assets/logo/B104_logo_basic_skyblue.png" alt="">
        </div>
        <div class="menu-bar-box">
          <div v-show="isLoggedIn" class="menu-bar" @click="goResume">이력서</div>
          <div v-show="isLoggedIn" class="menu-bar" @click="goCalendar">취업달력</div>
          <div v-show="isLoggedIn" class="menu-bar" @click="goVideo">교육</div>
          <div v-show="isLoggedIn" class="menu-bar" @click="goSearch">검색</div>
        </div>
        <div class="user-box">
          <div v-show="isLoggedIn" class="user-name-bar" @click="goMypage">{{ UserInfo.last_name }}{{ UserInfo.first_name }}님 환영합니다</div>
          <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('login')">로그인</div>
          <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('signup')">회원가입</div>
          <div v-show="isLoggedIn" class="user-bar" @click="goLogout">로그아웃</div>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import "../public/css/common.css";
import { mapState, mapMutations, mapActions } from 'vuex';
import axios from 'axios';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/';

export default {
  name: 'App',
  data() {
    return {

    }
  },
  mounted() {
    if (this.$cookies.isKey('auth-token')) {
      this.setIsLoggedIn(true);
      this.setToken(this.$cookies.get('auth-token'));
      this.setUserInfo();
    }
    else {
      this.setIsLoggedIn(false);
    }
  },
  methods: {
    ...mapMutations(['setIsLoggedIn', 'setToken', 'setLoginPath', 'setUser']),
    ...mapActions(['setUserInfo']),
    goHome() {
      this.$router.push('/').catch(()=>{})
    },
    goCorpHome() {
      this.$router.push('/corp/recruit').catch(()=>{})
    },
    goResume() {
      this.$router.push('/resume').catch(()=>{})
    },
    goVideo() {
      this.$router.push('/video').catch(()=>{})
    },
    goCalendar() {
      this.$router.push('/calendar').catch(()=>{})
    },
    goSearch() {
      this.$router.push('/search').catch(()=>{})
    },
    goRecruit() {
      this.$router.push('/corp/recruit').catch(()=>{})
    },
    goLogin(path) {
      if(path === 'login') {
        this.setLoginPath(path)
      } else {
        this.setLoginPath(path)
      }
      this.$router.push('/login').catch(()=>{})
    },
    goMypage() {
      this.$router.push('/mypage').catch(()=>{})
    },
    goLogout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(`${SERVER_URL}rest-auth/logout/`, null, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.setToken(null)
          this.setIsLoggedIn(false)
          this.setUserInfo()
          // if (this.$route.name === 'Home') {
          //   this.$router.go(this.$router.currentRoute)
          // } else {
          //   this.$router.push('/')
          // }
          this.$router.push('/').catch(()=>{})
        })
        .catch(() => {
        })
    }
  },
  computed: {
    ...mapState(['isLogin', 'isLoggedIn', 'UserInfo']),
  }
}
</script>