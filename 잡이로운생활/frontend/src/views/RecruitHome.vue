<template>
  <div class="wrap recruit-wrap">
    <div class="wrap-container recruit-container">
      <div class="recruit-user-box">
        <div class="recruit-user-content">
          <label for="recruit-user-img-edit">
            <div class="recruit-user-img-box">
              <img v-if='!getData.image' class="default-img" src="@/assets/images/company2.png" alt="#">
              <img v-if='getData.image' :src="getData.image" alt="#">
              <p v-if='!getData.image'>회사로고를 등록해 주세요</p>
              <input type="file" id="recruit-user-img-edit" accept="image/*" @change="setProfileImg">
            </div>
          </label>
          <p class="recruit-user-name">{{ UserInfo.last_name }}</p>
          <p class="recruit-user-email">{{ UserInfo.email }}</p>
          <div class="recruit-user-btn" @click="goRecruitWrite">공고 작성하기</div>
        </div>
      </div>
      <div class="recruit-data-box">
        <div class="recruit-data-content-box">
          <p>작성한공고</p>
          <p v-if="RecruitList.length===0">작성한 공고가 없습니다.</p>
          <div v-for="recruit in RecruitList" :key="recruit.id" @click="onModal(recruit.id)">
            <div class="recruit-data-content" v-if="(recruit.user.email === UserInfo.email)&&(recruit.deadline>nowTime)">
              <div class="recruit-data-head">
                <span class="recruit-data-sort">{{ recruit.division }}</span>
                <span class="recruit-data-name">{{ recruit.title }}</span>
              </div>
              <div class="recruit-data-footer">
                <span>마감일</span>
                <span>{{recruit.deadline.substring(0,4)}}.{{recruit.deadline.substring(4,6)}}.{{recruit.deadline.substring(6,8)}}</span>
                <span>{{ recruit.deadline.substring(8,10) }}:{{ recruit.deadline.substring(10,) }}</span>
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
import axios from 'axios';
import swal from 'sweetalert';
import { mapState, mapMutations } from 'vuex';
import RecruitModal from '../components/RecruitModal.vue'
import '../components/css/recruit-home.css'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'RecruitHome',
  props: {
    first: {
      type: Boolean,
    },
    private_key: {
      type: Object,
    }
  },
  data() {
    return {
      showModal: false,
      test: '',
      getData: [],
      RecruitList: [],
      profileImg: '',
      nowTime: '',
    }
  },
  components: {
    RecruitModal,
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
    this.setNowTime()
    this.getRecruit()
    setTimeout(() => {
      this.getResume()
    }, 1000);
    if (this.first === true){
      swal(`warning\n`, `${this.private_key.result}\n\n1. 지갑 비밀키를 잃어버리지 마세요! 한 번 잃어버리면 복구 할 수 없습니다.\n2. 공유하지 마세요! 비밀키가 악위적인 사이트에 노출되면 당신의 자산이 유실될 수 있습니다.\n3. 백업을 만들어 두세요! 종이에 적어서 오프라인으로 관리하세요.`, "warning")
    }
  },
  watch: {
  },
  methods: {
    ...mapMutations(['setRecruitId']),
    handleScroll() {
      const ORIGIN = 0
      let TOP = window.scrollY
      document.querySelector('.recruit-user-content').style.top = (ORIGIN + TOP) + 'px';
    },
    goRecruitWrite() {
      this.$router.push('/corp/recruit/write').catch(()=>{})
    },
    setProfileImg() {
      const photoFile = document.getElementById("recruit-user-img-edit");
      this.getData.image = URL.createObjectURL(photoFile.files[0]);
      this.profileImg = photoFile.files[0]
      this.editResume()
    },
    getResume() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/`, null, config)
      .then(res => {
        this.getData = res.data
        if(this.getData.image) {
          this.getData.image = 'https://j3b104.p.ssafy.io' + this.getData.image
        }
      })
      .catch(() => {})
    },
    getRecruit() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/`, null, config)
      .then(res => {
        this.RecruitList = res.data
      })
      .catch(() => {})
    },
    editResume() {
      let data = new FormData();
      data.append('image', this.profileImg);
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if (this.profileImg) {
        axios.put(`${SERVER_URL}articles/${this.UserInfo.id}/`, data, config)
        .then(() => {
        })
        .catch(() => {})
      }
    },
    onModal(id) {
      this.setRecruitId(id)
      this.showModal = true;
    },
    setNowTime() {
      let today = new Date();   
      let year = today.getFullYear()
      let month = today.getMonth()+1
      let date = ''+today.getDate()
      let hours = today.getHours()
      let minutes = today.getMinutes()
      if(month.length === 1) {
        month = '0' + month
      }
      if (date.length === 1) {
        date = '0' + date
      }
      this.nowTime = year + '' + month + '' + date + '' + hours + '' + minutes
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>