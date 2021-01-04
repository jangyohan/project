<template>
  <div class="wrap">
    <div class="wrap-container">
      <div class="profile-nav">
        <div @click="goMyCoin" class="profile-coin profile-select"><p class="name">코인 정보</p></div>
        <div @click="goMyList" class="profile-my"><p class="name">구매 이력서</p></div>
        <div @click="goMyVideo" class="profile-video"><p class="name">구매 비디오</p></div>
     </div>
      <MyCoin v-if="isMyCoin"></MyCoin>
      <MyList v-if="isMyList"></MyList>
      <MyVideo v-if="isMyVideo"></MyVideo>
    </div>
  </div>
</template>

<script>
import '../components/css/login.css'
import '../components/css/mypage.css'
import MyCoin from '../components/MyCoin.vue'
import MyList from '../components/MyList.vue'
import MyVideo from '../components/MyVideo.vue'

export default {
  name: 'Mypage',
  components: { 
    MyCoin,
    MyList,
    MyVideo,
  },
  data() {
    return { 
      isMyCoin: true,
      isMyList: false,
      isMyVideo: false,
    }
  },
  computed: {
  },
  created() {
  },
  mounted() {
  },
  watch: {
  },
  methods: {
    goMyCoin() {
      this.isMyCoin = true
      this.isMyList = false
      this.isMyVideo = false
      const Select = document.querySelector('.profile-select')
      Select.classList.remove('profile-select')
      const Here = document.querySelector('.profile-coin')
      Here.classList.add('profile-select')
    },
    goMyList() {
      this.isMyCoin = false
      this.isMyList = true
      this.isMyVideo = false
      const Select = document.querySelector('.profile-select')
      Select.classList.remove('profile-select')
      const Here = document.querySelector('.profile-my')
      Here.classList.add('profile-select')
    },
    goMyVideo() {
      this.isMyCoin = false
      this.isMyList = false
      this.isMyVideo = true
      const Select = document.querySelector('.profile-select')
      Select.classList.remove('profile-select')
      const Here = document.querySelector('.profile-video')
      Here.classList.add('profile-select')
    },
  },
}
</script>