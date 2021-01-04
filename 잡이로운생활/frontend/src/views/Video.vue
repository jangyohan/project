<template>
  <div class="wrap">
    <div class="wrap-container-video">
      <div class="video-nav-box">
        <div class="video-nav-menu video-nav-bar-0 selected-nav" @click="onNav(0)">IT <span></span></div>
        <div class="video-nav-menu video-nav-bar-1" @click="onNav(1)">전자 <span></span></div>
        <div class="video-nav-menu video-nav-bar-2" @click="onNav(2)">반도체 <span></span></div>
        <div class="video-nav-menu video-nav-bar-3" @click="onNav(3)">디자인 <span></span></div>
        <div class="video-nav-menu video-nav-bar-4" @click="onNav(4)">영어 <span></span></div>
      </div>
      <div class="video-unlock" v-if="isVideo">
        <div class="video-img">
          <img src="../assets/images/nextpng.com.png" alt="" class="video-img-in">
        </div>
        <div class="video-buy">
          <p class="video-buy-ment">현재 교육 영상을 구매하지 않았습니다.</p>
        </div>
        <div class="video-button" @click="goShow">
          구매하기
        </div>
      </div>
      <div class="video-box">
        <div class="video-inner-box" v-for='(videoItems, idx) in videoList' :key='`videoItems-${idx}`'>
          <div class="video-inner" v-for='(video, index) in videoItems' :key='`video-${index}`'>
            <div class="video-box">
              <iframe class="youtube-video" :src="`https://www.youtube.com/embed/${video.id.videoId}`" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="text-box">
              <p>{{ videoName }}</p>
              <p>{{ video.snippet.title }}</p>
            </div>
          </div>
        </div>
        <div class="video-more-btn-box">
          <div v-if="isBtn" class="video-more-btn" @click="moreVideo(videoName)">
            <span>더보기</span>
            <i class="fas fa-caret-down"></i>
          </div>
        </div>
      </div>
    </div>
    <BuyModal :videoName="videoName" v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios'
import '../components/css/video.css'
import { mapState } from 'vuex';
import BuyModal from '../components/BuyModal.vue';

const YOUTUBE_KEY = process.env.VUE_APP_API_KEY_YOUTUBE
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'Video',
  data() {
    return {
      videoList: [],
      videoName: 'IT',
      isBtn: true,
      isVideo: true,
      showModal: false,
    }
  },
  components: {
    BuyModal,
  },
  watch: {
    UserInfo() {
      if (this.UserInfo.it == 1) {
      this.isVideo = false
    }
    }
  },
  mounted() {
    this.onVideo('it 강의')
    if (this.UserInfo.it == 1) {
      this.isVideo = false
    }
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  methods: {
    onVideo(name) {
      this.videoList = []
      this.isBtn = true
      axios.get(API_URL, {
        params: {
          part: 'snippet',
          key: YOUTUBE_KEY,
          q: name,
          type: 'video',
          maxResults: 8,
        }
      })
      .then(res => {
        this.videoList.push(res.data.items.slice(0,4))
        this.videoList.push(res.data.items.slice(4,))
      })
      .catch(() =>{
      })
    },
    moreVideo(name) {
      let num = this.videoList.length * 4 + 10
      if (num > 42) {
        this.isBtn = false;
      }
      axios.get(API_URL, {
        params: {
          part: 'snippet',
          key: YOUTUBE_KEY,
          q: name + ' 강의',
          type: 'video',
          maxResults: num,
        }
      })
      .then(res => {
        this.videoList.push(res.data.items.slice(-8,-4))
        this.videoList.push(res.data.items.slice(-4,))
      })
      .catch(() =>{
      })
    },
    goShow() {
      this.showModal = true
    },
    onNav(num) {
      const NAVBAR1 = document.querySelector('.video-nav-bar-0')
      const NAVBAR2 = document.querySelector('.video-nav-bar-1')
      const NAVBAR3 = document.querySelector('.video-nav-bar-2')
      const NAVBAR4 = document.querySelector('.video-nav-bar-3')
      const NAVBAR5 = document.querySelector('.video-nav-bar-4')

      if(num==0) {
        NAVBAR1.classList.add('selected-nav'); NAVBAR2.classList.remove('selected-nav'); NAVBAR3.classList.remove('selected-nav');
        NAVBAR4.classList.remove('selected-nav'); NAVBAR5.classList.remove('selected-nav');
        this.videoName = 'IT'
        this.onVideo('it 강의')
        if (this.UserInfo.it == 0) {
          this.isVideo = true
        }
        else {
          this.isVideo = false
        }
      } else if(num==1) {
        NAVBAR1.classList.remove('selected-nav'); NAVBAR2.classList.add('selected-nav'); NAVBAR3.classList.remove('selected-nav');
        NAVBAR4.classList.remove('selected-nav'); NAVBAR5.classList.remove('selected-nav');
        this.videoName = '전자'
        this.onVideo('전자 강의')
        if (this.UserInfo.electric == 0) {
          this.isVideo = true
        }
        else {
          this.isVideo = false
        }
      } else if(num==2) {
        NAVBAR1.classList.remove('selected-nav'); NAVBAR2.classList.remove('selected-nav'); NAVBAR3.classList.add('selected-nav');
        NAVBAR4.classList.remove('selected-nav'); NAVBAR5.classList.remove('selected-nav');
        this.videoName = '반도체'
        this.onVideo('반도체 강의')
        if (this.UserInfo.semiconductor == 0) {
          this.isVideo = true
        }
        else {
          this.isVideo = false
        }
      } else if(num==3) {
        NAVBAR1.classList.remove('selected-nav'); NAVBAR2.classList.remove('selected-nav'); NAVBAR3.classList.remove('selected-nav');
        NAVBAR4.classList.add('selected-nav'); NAVBAR5.classList.remove('selected-nav');
        this.videoName = '디자인'
        this.onVideo('디자인 강의')
        if (this.UserInfo.design == 0) {
          this.isVideo = true
        }
        else {
          this.isVideo = false
        }
      } else {
        NAVBAR1.classList.remove('selected-nav'); NAVBAR2.classList.remove('selected-nav'); NAVBAR3.classList.remove('selected-nav');
        NAVBAR4.classList.remove('selected-nav'); NAVBAR5.classList.add('selected-nav');
        this.videoName = '영어'
        this.onVideo('영어 강의')
        if (this.UserInfo.eng == 0) {
          this.isVideo = true
        }
        else {
          this.isVideo = false
        }
      }
    }
  }
}
</script>
