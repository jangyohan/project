<template>
  <div class='wrap'>
    <div class="wrap-container">
      <div class="schedule-box">
        <div class="recruit-box">
          <p class="recruit-header">추천공고</p>
          <div id="recruit-slider">
            <input type="radio" name='slider' id='recruit-slide1' checked>
            <input type="radio" name='slider' id='recruit-slide2'>
            <input type="radio" name='slider' id='recruit-slide3'>
            <input type="radio" name='slider' id='recruit-slide4'>
            <div id="recruit-controls">
              <label for="recruit-slide1"></label>
              <label for="recruit-slide2"></label>
              <label for="recruit-slide3"></label>
              <label for="recruit-slide4"></label>
            </div>
            <div id="recruit-slides">
              <div id="recruit-overflow">
                <div class="recruit-inner">
                  <div class="recruit-slide slide_1" v-for="(recruitArr1,index1) in recruitList2" :key="`recruitArr1-${index1}`">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card" v-for="recruit in recruitArr1" :key="recruit.id" @click="onModal(recruit.id,'individual')">
                          <div class="recruit-card-img-box">
                            <img v-if="recruitImg2[recruit.user.id]" :src="'https://j3b104.p.ssafy.io'+recruitImg2[recruit.user.id]" alt="">
                            <img v-else src="@/assets/images/company2.png" alt="">
                          </div>
                          <p>{{ recruit.user.last_name }}</p>
                          <p v-if="recruit.title.length<18">{{ recruit.title }}</p>
                          <p v-else>{{ recruit.title.substring(0,18) + '...' }}</p>
                          <p>~ {{recruit.deadline.substring(0,4)}}.{{recruit.deadline.substring(4,6)}}.{{recruit.deadline.substring(6,8)}}
                             {{recruit.deadline.substring(8,10)}}:{{recruit.deadline.substring(10,)}}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>          
        </div>
      </div>
      <div class="schedule-box">
        <div class="test-box">
          <p class="test-header">마감임박 공고</p>
          <div id="test-slider">
            <input type="radio" name='slider2' id='test-slide1' checked>
            <input type="radio" name='slider2' id='test-slide2'>
            <input type="radio" name='slider2' id='test-slide3'>
            <input type="radio" name='slider2' id='test-slide4'>
            <div id="test-controls">
              <label for="test-slide1"></label>
              <label for="test-slide2"></label>
              <label for="test-slide3"></label>
              <label for="test-slide4"></label>
            </div>
            <div id="test-slides">
              <div id="test-overflow">
                <div class="test-inner">
                  <div class="test-slide slide_1" v-for="(recruitArr2,index2) in recruitList" :key="`recruitArr2-${index2}`">
                    <div class="test-slide-content">
                      <div class="test-card-box">
                        <div class="test-card" v-for="recruit in recruitArr2" :key="recruit.id" @click="onModal(recruit.id,'individual')">
                          <div class="test-card-img-box">
                            <img v-if="recruitImg[recruit.user.id]" :src="'https://j3b104.p.ssafy.io'+recruitImg[recruit.user.id]" alt="">
                            <img v-else src="@/assets/images/company2.png" alt="">
                          </div>
                          <p>{{ recruit.user.last_name }}</p>
                          <p v-if="recruit.title.length<18">{{ recruit.title }}</p>
                          <p v-else>{{ recruit.title.substring(0,18) + '...' }}</p>
                          <p>~ {{recruit.deadline.substring(0,4)}}.{{recruit.deadline.substring(4,6)}}.{{recruit.deadline.substring(6,8)}}
                             {{recruit.deadline.substring(8,10)}}:{{recruit.deadline.substring(10,)}}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>          
        </div>
      </div>
    </div>

    <RecruitModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapMutations } from 'vuex';
import RecruitModal from '../components/RecruitModal.vue'
import '../components/css/home.css'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'
// const WORK_API_KEY = process.env.VUE_APP_WORK_API_KEY

export default {
  name: 'Home',
  data() {
    return {
      showModal: false,
      recruitImg: {},
      recruitImg2: {},
      recruitList: [],
      recruitList2: [],
    }
  },
  components: {
    RecruitModal
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  mounted() {
    this.getRecruit()
    this.getRecruit2()
  },
  methods: {
    ...mapMutations(['setUserDivide', 'setRecruitId']),
    onModal(id, type) {
      this.setRecruitId(id)
      this.setUserDivide(type)
      this.showModal = true;
    },
    getRecruit() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/showlist/`, null, config)
      .then(res => {
        for(let k=0; k<res.data.length; k++) {
          this.recruitImg[res.data[k].user.id] = '';
        }
        let cnt = 0
        for(let key in this.recruitImg) {
          axios.get(`${SERVER_URL}articles/${key}/`, null, config)
          .then(response => {
            this.recruitImg[key] = response.data.image
            cnt += 1
            if (cnt === Object.keys(this.recruitImg).length) {
              this.recruitList = tmp
            }
          })
          .catch(() => {})
        }
        let tmp = []
        if(res.data.length>5) {
          for(let j=0; j<res.data.length/5; j++){
            if(j==4) {
              break
            }
            let ARR = []
            for(let i=0; i<5; i++) {
              if(res.data.length<=j*5+i){
                break
              } else {
                ARR.push(res.data[j*5+i])
              }
            }
            tmp.push(ARR)
          }
        } else {
          let ARR = []
          for(let i=0; i<res.data.length; i++) {
              ARR.push(res.data[i])
          }
          tmp.push(ARR)
        }
      })
      .catch(() => {})
    },
    getRecruit2() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/showlist2/`, null, config)
      .then(res => {
        for(let k=0; k<res.data.length; k++) {
          this.recruitImg2[res.data[k].user.id] = '';
        }
        let cnt2 = 0
        for(let key in this.recruitImg2) {
          axios.get(`${SERVER_URL}articles/${key}/`, null, config)
          .then(response => {
            this.recruitImg2[key] = response.data.image
            cnt2 += 1
            if (cnt2 === Object.keys(this.recruitImg2).length) {
              this.recruitList2 = tmp2
            }
          })
          .catch(() => {})
        }
        let tmp2 = []
        if(res.data.length>5) {
          for(let j=0; j<res.data.length/5; j++){
            if(j==4) {
              break
            }
            let ARR = []
            for(let i=0; i<5; i++) {
              if(res.data.length<=j*5+i){
                break
              } else {
                ARR.push(res.data[j*5+i])
              }
            }
            tmp2.push(ARR)
          }
        } else {
          let ARR = []
          for(let i=0; i<res.data.length; i++) {
              ARR.push(res.data[i])
          }
          tmp2.push(ARR)
        }
      })
      .catch(() => {})
    }
    // getRecruitInform() {
    //   console.log(WORK_API_KEY)
    //   axios.get('http://openapi.work.go.kr/opi/opi/opia/wantedApi.do', {
    //     params: {
    //       authKey: WORK_API_KEY,
    //       callTp: 'L',
    //       returnType: 'XML',
    //       startPage: 1,
    //       display: 10,
    //       coTp: '01'
    //     }
    //   }).then(res => {
    //     console.log(res)
    //   })
    //   .catch(err =>{
    //     console.log(err.response)
    //   })
    // }
  }
}
</script>