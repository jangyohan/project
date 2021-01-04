<template>
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
      <div v-if="isBtn && videoName != ''" class="video-more-btn" @click="moreVideo(videoName)">
        <span>더보기</span>
        <i class="fas fa-caret-down"></i>
      </div>
      <p v-if="videoName == ''" class="myVideo-buy">아직 구매한 영상이 없습니다!</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import '../components/css/video.css'
import { mapState } from 'vuex';

const YOUTUBE_KEY = process.env.VUE_APP_API_KEY_YOUTUBE
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MyVideo',
  data() {
    return { 
      videoList: [],
      videoName: '',
      isBtn: true,
      isVideo: true,
    }
  },
  components: {
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
  },
  mounted() {
    if (this.UserInfo.it == 1) {
        this.videoName = 'IT'
        this.onVideo('it 강의')
      } 
    else if (this.UserInfo.electric == 1) {
      this.videoName = '전자'
      this.onVideo('전자')
    }
    else if (this.UserInfo.semiconductor == 1) {
      this.videoName = '반도체'
      this.onVideo('반도체')
    }
    else if (this.UserInfo.design == 1) {
      this.videoName = '디자인'
      this.onVideo('디자인')
    }
    else if (this.UserInfo.eng == 1) {
      this.videoName = '영어'
      this.onVideo('영어')
    }
  },
  watch: {
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
        
      })},
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
      })}

  },
}
</script>