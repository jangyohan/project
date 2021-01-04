<template>
  <div class="wrap apply-wrap">
    <div class="wrap-container apply-container">
      <div class="apply-header">
        <div class="apply-header-text-box">
          <span>{{ RecruitDetail.title }}</span>
          <span v-if="RecruitDetail.applicants" >( {{ RecruitDetail.applicants.length }}명 )</span>
          <!-- <span v-if="isSome">(3 명)</span> -->
        </div>
        <!-- <div class="apply-header-toggle-box">
          <div @click='applyInfoChange(false)' class="all-apply-btn apply-toggle-btn on-apply-btn">전체</div>
          <div @click='applyInfoChange(true)' class="some-apply-btn apply-toggle-btn">저장</div>
        </div> -->
      </div>
      <div v-if="!isSome" class="apply-body">
        <p v-if="userList.length===0">현재 지원자가 없습니다.</p>
        <div class="applicant-card" v-for="user in userList" :key="user.user.id" @click="onModal(user.user.id, 'corp')">
          <div class="applicant-img-box">
            <img v-if="!user.image" src="@/assets/images/default-user.png" alt="#">
            <img v-if="user.image" :src="user.image" alt="#">
          </div>
          <div class="applicant-text-box">
            <p>{{ user.name }}</p>
            <p>{{ user.date_of_birth }}</p>
            <p>{{ user.email }}</p>
            <p>{{ user.phone_number }}</p>
          </div>
        </div>
      </div>
      <!-- <div v-if="isSome" class="apply-body">
        <div class="applicant-card">
          <div class="applicant-img-box">
            <img src="@/assets/images/default-user.png" alt="#">
          </div>
          <div class="applicant-text-box">
            <p>이싸피</p>
            <p>2003. 01. 01</p>
            <p>ssafy0101@naver.com</p>
            <p>010-0101-0101</p>
          </div>
        </div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
      </div> -->
    </div>

    <UserModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios'
import UserModal from '../components/UserModal.vue';
import '../components/css/applicant.css'
import { mapMutations } from 'vuex';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'Applicant',
  data() {
    return {
      showModal: false,
      test: '',
      isSome: '',
      recruitID: '',
      RecruitDetail: [],
      userList: [],
    }
  },
  components: {
    UserModal,
  },
  computed: {
  },
  created() {
    this.recruitID = this.$route.params.recruitID
  },
  mounted() {
    this.getRecruitDetail();
  },
  watch: {
  },
  methods: {
    ...mapMutations(['setUserModalId', 'setUserDivide', 'setRecruitId']),
    applyInfoChange(bool) {
      const ALLBTN = document.querySelector('.all-apply-btn')
      const SOMEBTN = document.querySelector('.some-apply-btn')
      if (bool) {
        SOMEBTN.classList.add('on-apply-btn')
        ALLBTN.classList.remove('on-apply-btn')
      } else {
        ALLBTN.classList.add('on-apply-btn')
        SOMEBTN.classList.remove('on-apply-btn')
      }
      this.isSome = bool
    },
    getRecruitDetail() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/${this.recruitID}`, null, config)
      .then(res => {
        this.RecruitDetail = res.data
        for (let i=0; i<res.data.applicants.length; i++) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.get(`${SERVER_URL}articles/${res.data.applicants[i]}/`, null, config)
          .then(res => {
            this.userList.push(res.data) 
          })
          .catch(() => {})
        }
      })
      .catch(() => {})
    },
    onModal(id, type) {
      this.setUserModalId(id);
      this.setUserDivide(type)
      this.setRecruitId(this.recruitID)
      this.showModal = true;
    },
  },
  beforeDestroy () {
    this.setRecruitId('')
    this.setUserDivide('')
  },
}
</script>