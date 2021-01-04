<template>
  <div class="wrap resume-wrap">
    <div class="wrap-container resume-container">
      <div class="resume-user-box">
        <div class="resume-user-content">
          <img v-if="!getData.image" src="@/assets/images/default-user.png" alt="#">
          <img v-if="getData.image" :src="'https://j3b104.p.ssafy.io' + getData.image" alt="#">
          <p class="resume-user-name">{{ getData.name }}</p>
          <p class="resume-user-birth">{{ getData.date_of_birth }}</p>
          <p class="resume-user-email">{{ getData.email }}</p>
          <p class="resume-user-number">{{ getData.phone_number }}</p>
          <div class="resume-user-btn" @click="goResumeEdit">수정하기</div>
        </div>
      </div>
      <div class="resume-data-box">
        <div class="resume-data-content-box">
          <p>병역사항</p>
          <div class="resume-data-content">
            <p v-if="!getData.military_classification">인증된 병력사항이 없습니다.</p>
            <div v-if="getData.military_classification" class="resume-license-certified-list">
              <div class="resume-detail resume-type">{{ getData.military_classification }}</div>
              <div class="resume-detail">{{ getData.military_branch }}</div>
              <div class="resume-detail">{{ getData.military_rank }}</div>
              <div class="resume-detail">{{ getData.military_completed }}</div>
              <div v-if="getData.military_completed_reason" class="resume-detail">{{ getData.military_completed_reason }}</div>
              <div class="resume-detail resume-detail-non-margin">{{ getData.military_start }}</div>
              <div class="resume-detail resume-detail-non-margin">~</div>
              <div class="resume-detail">{{ getData.military_end }}</div>
              <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>학력사항</p>
          <div class="resume-data-content">
            <p v-if="(certifiedSchool[0].length+certifiedSchool[1].length+certifiedSchool[2].length
            +certifiedSchool[3].length+certifiedSchool[4].length)===0">인증된 학력사항이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(certified, index) in certifiedSchool' :key='`certified-${index}`'>
              <div class="resume-license-certified-list" v-if="certified[0]">
                <div class="resume-detail resume-type">{{ certified[0] }}</div>
                <div class="resume-detail">{{ certified[1] }}</div><div class="resume-detail">{{ certified[2] }}</div>
                <div class="resume-detail">{{ certified[3] }}</div><div class="resume-detail resume-detail-non-margin">{{ certified[4] }}</div>
                <div class="resume-detail resume-detail-non-margin">~</div><div class="resume-detail">{{ certified[5] }}</div>
                <div v-if="certified[6]" class="resume-detail resume-detail-non-margin">{{ certified[6] }}</div>
                <div v-if="certified[6]" class="resume-detail resume-detail-non-margin">/</div>
                <div v-if="certified[7]" class="resume-detail">{{ certified[7] }}</div>
                <div v-if="certified[8]" class="resume-detail resume-detail-non-margin">{{ certified[8] }}</div>
                <div v-if="certified[8]" class="resume-detail resume-detail-non-margin">/</div><div v-if="certified[9]" class="resume-detail">{{ certified[9] }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>자격사항</p>
          <div class="resume-data-content">
            <p v-if="getLicense.length===0">인증된 자격증이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(license, index) in getLicense' :key='`license1-${index}`'>
              <div class="resume-license-certified-list" v-if="license.name">
                <div class="resume-detail resume-type">{{ license.name }}</div>
                <div class="resume-detail">{{ license.publisher }}</div><div class="resume-detail">{{ license.date }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>어학사항</p>
          <div class="resume-data-content">
            <p v-if="getLang.length===0">인증된 어학성적이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(lang, index) in getLang' :key='`lang1-${index}`'>
              <div class="resume-license-certified-list" v-if="lang.classification">
                <div class="resume-detail resume-type">{{ lang.classification }}</div>
                <div class="resume-detail">{{ lang.name }}</div><div class="resume-detail">{{ lang.score }}</div>
                <div class="resume-detail">{{ lang.date }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>경력사항</p>
          <div class="resume-data-content">
            <p v-if="getCareer.length===0">인증된 경력이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(career, index1) in getCareer' :key='`career1-${index1}`'>
              <div class="resume-license-certified-list" v-if="career.name">
                <div class="resume-detail resume-type">{{ career.name }}</div>
                <div class="resume-detail resume-detail-non-margin">{{ career.start_term }}</div>
                <div class="resume-detail resume-detail-non-margin">~</div>
                <div class="resume-detail">{{ career.end_term }}</div>
                <div class="resume-detail">{{ career.retirement_reason }}</div><div class="resume-detail">{{ career.department }}</div>
                <div class="resume-detail">{{ career.rank }}</div><div class="resume-detail">{{ career.duty }}</div>
                <div class="resume-detail resume-detail-career-text" @click="onModal(career.statement)">
                  경력기술서
                </div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>기타</p>
          <div class="resume-data-content">
            <p v-if="(certifiedEtc[0].length+certifiedEtc[1].length)===0">인증된 기타사항이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(etc, index) in certifiedEtc' :key='`etc-${index}`'>
              <div class="resume-license-certified-list" v-if="(etc[0] || etc[1])">
                <div class="resume-detail resume-type">{{ etc[0] }}</div>
                <div class="resume-detail">{{ etc[1] }}</div><div class="resume-detail">{{ etc[2] }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <CareerModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState, mapMutations } from 'vuex';
import '../components/css/resume.css'
import CareerModal from '../components/CareerModal.vue';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'Resume',
  data() {
    return {
      showModal: false,
      getData: [],
      getLicense: [],
      getLang: [],
      getCareer: [],
      certifiedSchool: [[],[],[],[],[]],
      certifiedEtc: [[],[]],
      isCareerText: [],
    }
  },
  components: {
    CareerModal,
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
    setTimeout(() => {
      this.getResume()
    }, 1000);
  },
  watch: {
  },
  methods: {
    ...mapMutations(['setCareerDetail']),
    goResumeEdit() {
      this.$router.push('/resume/edit').catch(()=>{})
    },
    handleScroll() {
      const ORIGIN = 0
      let TOP = window.scrollY
      document.querySelector('.resume-user-content').style.top = (ORIGIN + TOP) + 'px';
    },
    onCareerText(text, idx) {
      if (text === 'on') {
        this.isCareerText[idx] = true
      } else {
        this.isCareerText[idx] = false
      }
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
        this.sortSchool()
        this.sortEtc()
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/certificates/`, null, config)
      .then(res => {
        this.getLicense = res.data
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/languages/`, null, config)
      .then(res => {
        this.getLang = res.data
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/careers/`, null, config)
      .then(res => {
        this.getCareer = res.data
        for(let i=0; i<res.data.length; i++) {
          this.isCareerText.push(false)
        }
      })
      .catch(() => {})
    },
    sortSchool() {
      if(this.getData.highschool_name) {
        let ARR = ['고등학교']
        ARR.push(this.getData.highschool_name); ARR.push(this.getData.highschool_classification); ARR.push(this.getData.highschool_location);
        ARR.push(this.getData.highschool_entrance_year); ARR.push(this.getData.highschool_graduation_year);
        this.certifiedSchool[0] = ARR
      }
      if(this.getData.college_name) {
        let ARR = ['전문대학']
        ARR.push(this.getData.college_name); ARR.push(this.getData.college_classification); ARR.push(this.getData.college_location);
        ARR.push(this.getData.college_entrance_year); ARR.push(this.getData.college_graduation_year); ARR.push(this.getData.college_major);
        if (this.getData.college_minor) { ARR.push(this.getData.college_minor) } else { ARR.push('X') } ARR.push(this.getData.college_grade); ARR.push(this.getData.college_total)
        this.certifiedSchool[1] = ARR
      }
      if(this.getData.university_name) {
        let ARR = ['대학교']
        ARR.push(this.getData.university_name); ARR.push(this.getData.university_classification); ARR.push(this.getData.university_location);
        ARR.push(this.getData.university_entrance_year); ARR.push(this.getData.university_graduation_year); ARR.push(this.getData.university_major);
        if (this.getData.university_minor) { ARR.push(this.getData.university_minor) } else { ARR.push('X') } ARR.push(this.getData.university_grade); ARR.push(this.getData.university_total)
        this.certifiedSchool[2] = ARR
      }
      if(this.getData.master_name) {
        let ARR = ['석사']
        ARR.push(this.getData.master_name); ARR.push(this.getData.master_classification); ARR.push(this.getData.master_location);
        ARR.push(this.getData.master_entrance_year); ARR.push(this.getData.master_graduation_year); ARR.push(this.getData.master_major);
        if (this.getData.master_minor) { ARR.push(this.getData.master_minor) } else { ARR.push('X') } ARR.push(this.getData.master_grade); ARR.push(this.getData.master_total)
        this.certifiedSchool[3] = ARR
      }
      if(this.getData.doctor_name) {
        let ARR = ['박사']
        ARR.push(this.getData.doctor_name); ARR.push(this.getData.doctor_classification); ARR.push(this.getData.doctor_location);
        ARR.push(this.getData.doctor_entrance_year); ARR.push(this.getData.doctor_graduation_year); ARR.push(this.getData.doctor_major);
        if (this.getData.doctor_minor) { ARR.push(this.getData.doctor_minor) } else { ARR.push('X') } ARR.push(this.getData.doctor_grade); ARR.push(this.getData.doctor_total)
        this.certifiedSchool[4] = ARR
      }
    },
    sortEtc() {
      if(this.getData.veterans_classification) {
        let ARR = ['보훈']
        ARR.push(this.getData.veterans_classification); ARR.push(this.getData.veterans_number);
        this.certifiedEtc[0] = ARR
      }
      if(this.getData.obstacle_classification) {
        let ARR = ['장애']
        ARR.push(this.getData.obstacle_classification); ARR.push(this.getData.obstacle_grade);
        this.certifiedEtc[1] = ARR
      }
    },
    onModal(detail) {
      this.setCareerDetail(detail)
      this.showModal = true;
    },
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>