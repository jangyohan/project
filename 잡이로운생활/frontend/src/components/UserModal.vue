<template>
  <transition name="modal">
    <div class="user-modal-mask">
      <div @mousedown.self="$emit('close')">
        <div class="user-modal-wrap">
          <div class="user-modal-content">
            <i class="fas fa-times" @click.self="$emit('close')"></i>
            <div class='user-modal-header'>
              <div class="user-modal-img-box">
                <img v-if="getData.image" :src="getData.image" alt="#">
                <img v-if="!getData.image" src="@/assets/images/default-user.png" alt="#">
              </div>
              <div class="user-modal-text-box">
                <p>{{ getData.name }}</p>
                <p>{{ getData.date_of_birth }}</p>
                <p>{{ getData.email }}</p>
                <p>{{ getData.phone_number }}</p>
              </div>
            </div>
            <div class='user-modal-body'>
              <div class="user-modal-content-box">
                <p>병역사항</p>
                <div class="user-modal-data-content">
                  <p v-if="!getData.military_classification">인증된 병력사항이 없습니다.</p>
                  <div v-if="getData.military_classification" class="user-modal-license-certified-list">
                    <div class="user-modal-detail user-modal-type">{{ getData.military_classification }}</div>
                    <div class="user-modal-detail">{{ getData.military_branch }}</div>
                    <div class="user-modal-detail">{{ getData.military_rank }}</div>
                    <div class="user-modal-detail">{{ getData.military_completed }}</div>
                    <div v-if="getData.military_completed_reason" class="user-modal-detail">{{ getData.military_completed_reason }}</div>
                    <div class="user-modal-detail user-modal-detail-non-margin">{{ getData.military_start }}</div>
                    <div class="user-modal-detail user-modal-detail-non-margin">~</div>
                    <div class="user-modal-detail">{{ getData.military_end }}</div>
                    <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>학력사항</p>
                <div class="user-modal-data-content">
                  <p v-if="(certifiedSchool[0].length+certifiedSchool[1].length+certifiedSchool[2].length
                  +certifiedSchool[3].length+certifiedSchool[4].length)===0">인증된 학력사항이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(certified, index) in certifiedSchool' :key='`certified-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="certified[0]">
                      <div class="user-modal-detail user-modal-type">{{ certified[0] }}</div>
                      <div class="user-modal-detail">{{ certified[1] }}</div><div class="user-modal-detail">{{ certified[2] }}</div>
                      <div class="user-modal-detail">{{ certified[3] }}</div><div class="user-modal-detail user-modal-detail-non-margin">{{ certified[4] }}</div>
                      <div class="user-modal-detail user-modal-detail-non-margin">~</div><div class="user-modal-detail">{{ certified[5] }}</div>
                      <div v-if="certified[6]" class="user-modal-detail user-modal-detail-non-margin">{{ certified[6] }}</div>
                      <div v-if="certified[6]" class="user-modal-detail user-modal-detail-non-margin">/</div>
                      <div v-if="certified[7]" class="user-modal-detail">{{ certified[7] }}</div>
                      <div v-if="certified[8]" class="user-modal-detail user-modal-detail-non-margin">{{ certified[8] }}</div>
                      <div v-if="certified[8]" class="user-modal-detail user-modal-detail-non-margin">/</div><div v-if="certified[9]" class="user-modal-detail">{{ certified[9] }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>자격사항</p>
                <div class="user-modal-data-content">
                  <p v-if="getLicense.length===0">인증된 자격증이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(license, index) in getLicense' :key='`license1-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="license.name">
                      <div class="user-modal-detail user-modal-type">{{ license.name }}</div>
                      <div class="user-modal-detail">{{ license.publisher }}</div><div class="user-modal-detail">{{ license.date }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>어학사항</p>
                <div class="user-modal-data-content">
                  <p v-if="getLang.length===0">인증된 어학성적이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(lang, index) in getLang' :key='`lang1-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="lang.classification">
                      <div class="user-modal-detail user-modal-type">{{ lang.classification }}</div>
                      <div class="user-modal-detail">{{ lang.name }}</div><div class="user-modal-detail">{{ lang.score }}</div>
                      <div class="user-modal-detail">{{ lang.date }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>경력사항</p>
                <div class="user-modal-data-content">
                  <p v-if="getCareer.length===0">인증된 경력이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(career, index1) in getCareer' :key='`career1-${index1}`'>
                    <div class="user-modal-license-certified-list" v-if="career.name">
                      <div class="user-modal-detail user-modal-type">{{ career.name }}</div>
                      <div class="user-modal-detail user-modal-detail-non-margin">{{ career.start_term }}</div>
                      <div class="user-modal-detail user-modal-detail-non-margin">~</div>
                      <div class="user-modal-detail">{{ career.end_term }}</div>
                      <div class="user-modal-detail">{{ career.retirement_reason }}</div><div class="user-modal-detail">{{ career.department }}</div>
                      <div class="user-modal-detail">{{ career.rank }}</div><div class="user-modal-detail">{{ career.duty }}</div>
                      <div class="user-modal-detail user-modal-detail-career-text" @click="onModal(career.statement)">
                        경력기술서
                      </div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>기타</p>
                <div class="user-modal-data-content">
                  <p v-if="(certifiedEtc[0].length+certifiedEtc[1].length)===0">인증된 기타사항이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(etc, index) in certifiedEtc' :key='`etc-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="(etc[0] || etc[1])">
                      <div class="user-modal-detail user-modal-type">{{ etc[0] }}</div>
                      <div class="user-modal-detail">{{ etc[1] }}</div><div class="user-modal-detail">{{ etc[2] }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="UserDivide==='individual'" class="user-modal-content-box">
                <p>자기소개서</p>
                <div class="user-modal-self-box" v-for="(self,index) in selfList" :key='`self-${index}`'>
                  <div class="user-modal-self-head">
                    <p>{{ index+1 }}. {{ self.title }} <span>({{ self.number }}자)</span></p>
                    <p>{{mySelfList[index].content.length}}/{{self.number}}</p>
                  </div>
                  <textarea v-model="mySelfList[index].content" v-on:input="mySelfList[index].content = $event.target.value" name="" id="" cols="30" rows="10"></textarea>
                </div>
              </div>
              <div v-if="UserDivide==='corp'" class="user-modal-content-box">
                <p>자기소개서</p>
                <div class="user-modal-self-box" v-for="(self,index) in selfList" :key='`self-${index}`'>
                  <div class="user-modal-self-head">
                    <p>{{ index+1 }}. {{ self.title }} <span>({{ self.number }}자)</span></p>
                    <p v-if="mySelfList[index].content">{{mySelfList[index].content.length}}/{{self.number}}</p>
                  </div>
                  <div v-if="mySelfList[index].content" class="user-modal-self-area">{{ mySelfList[index].content }}</div>
                </div>
              </div>
            </div>
            <div class="user-modal-footer">
              <div class="user-modal-btn user-modal-btn-on" @click="goBuy" v-if="(UserModalId != UserInfo.id) && !isBuy && (UserDivide==='search')">구매하기</div>
              <div class="user-modal-btn" @click="goBuy" v-if="(UserModalId != UserInfo.id) && isBuy && (UserDivide==='search')">보러가기</div>
              <div v-if="UserDivide==='individual'" class="user-modal-btn user-modal-btn-on" @click="saveSelf">저장하기</div>
              <div v-if="(UserDivide==='individual')&&!isSameUser" class="user-modal-btn user-modal-btn-on" @click="applySelf">지원하기</div>
              <div v-if="(UserDivide==='individual')&&isSameUser" class="user-modal-btn" @click="applySelf">취소하기</div>
              <div class="user-modal-btn" @click.self="$emit('close')">닫기</div>
            </div>
          </div>
        </div>
      </div>

      <CareerModal v-if="showModal" @close="showModal= false"/>
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import './css/user-modal.css'
import axios from 'axios';
import CareerModal from '../components/CareerModal.vue';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'UserModal',
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
      selfListTmp: [],
      selfList: [],
      selfLength: 0,
      isMySelf: false,
      isSameUser: false,
      mySelfList: [],
      isBuy: false,
    }
  },
  watch: {
    mySelfList() {
    }
  },
  components: {
    CareerModal,
  },
  computed: {
    ...mapState(['UserInfo', 'UserModalId', 'UserDivide', 'recruitId']),
  },
  created() {
  },
  mounted() {
    const Lock = document.querySelector('.user-modal-body')
    if(this.UserDivide === 'search') {
      Lock.classList.add('user-modal-unlock')
    }
    this.getResume()
    if(this.UserDivide !== 'search') {
      this.getSelfList();
      this.getApplicant();
      this.getMySelf()
    }
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}accounts/item/list/${this.UserModalId}/`, null, config)
      .then(res => {
        if (res.data.result == 1) {
          this.isBuy = true
          Lock.classList.remove('user-modal-unlock')
        }
        else {
          this.isBuy = false
        }
      })
      .catch(() => {})
  },
  methods: {
    ...mapMutations(['setCareerDetail']),
    goBuy() {
      this.$router.push(`/otherresume/${this.UserModalId}`)
    },
    getResume() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}articles/${this.UserModalId}/`, null, config)
      .then(res => {
        this.getData = res.data
        this.sortSchool()
        this.sortEtc()
        if(this.getData.image) {
          this.getData.image = 'https://j3b104.p.ssafy.io' + this.getData.image
        }
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserModalId}/certificates/`, null, config)
      .then(res => {
        this.getLicense = res.data
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserModalId}/languages/`, null, config)
      .then(res => {
        this.getLang = res.data
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserModalId}/careers/`, null, config)
      .then(res => {
        this.getCareer = res.data
        for(let i=0; i<res.data.length; i++) {
          this.isCareerText.push(false)
        }
      })
      .catch(() => {})
    },
    getSelfList() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/${this.recruitId}/introductions/`, null, config)
      .then(res => {
        this.selfListTmp = res.data
        this.selfLength = res.data.length
        this.getMySelf();
      })
      .catch(() => {})
    },
    getMySelf() {
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.get(`${SERVER_URL}articles/${this.UserModalId}/selfintroductions/${this.recruitId}/`, null, config)
        .then(res => {
          if(res.data.length>0) {
            this.isMySelf = true
            this.mySelfList = res.data
            this.selfList = this.selfListTmp
          } else {
            this.isMySelf = false
            this.mySelfList = []
            for(let i=0; i<this.selfLength; i++) {
              this.mySelfList.push({content:''})
            }
            this.selfList = this.selfListTmp
          }
        })
        .catch(() => {})
    },
    getApplicant() {
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.get(`${SERVER_URL}recruitments/${this.recruitId}/`, null, config)
        .then(res => {
          for(let i=0; i<res.data.applicants.length; i++) {
            if (res.data.applicants[i] == this.UserModalId) {
              this.isSameUser = true
            }
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
    onCareerText(text, idx) {
      if (text === 'on') {
        this.isCareerText[idx] = true
      } else {
        this.isCareerText[idx] = false
      }
    },
    saveSelf() {
      if(this.isMySelf) {
        for(let i=0; i<this.mySelfList.length; i++) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.put(`${SERVER_URL}articles/${this.UserModalId}/selfintroductions/${this.recruitId}/${this.mySelfList[i].id}/`, {
            article: this.UserModalId,
            recruitment: this.recruitId,
            content: this.mySelfList[i].content
          }, config)
          .then(() => {
          })
          .catch(() => {})
        }
      } else {
        for(let i=0; i<this.mySelfList.length; i++) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          setTimeout(() => {
            axios.post(`${SERVER_URL}articles/${this.UserModalId}/selfintroductions/${this.recruitId}/create/`, {
              article: this.UserModalId,
              recruitment: this.recruitId,
              content: this.mySelfList[i].content
            }, config)
            .then(() => {
            })
            .catch(() => {})
          }, 100 + i*100);
        } 
      }
      this.$emit('close')
    },
    applySelf() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if(this.isMySelf) {
        for(let i=0; i<this.mySelfList.length; i++) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.put(`${SERVER_URL}articles/${this.UserModalId}/selfintroductions/${this.recruitId}/${this.mySelfList[i].id}/`, {
            article: this.UserModalId,
            recruitment: this.recruitId,
            content: this.mySelfList[i].content
          }, config)
          .then(() => {
            if (i===this.mySelfList.length-1) {
              axios.get(`${SERVER_URL}recruitments/${this.recruitId}/apply/${this.UserModalId}`, null, config)
              .then(() => {
                this.$emit('close')
              })
              .catch(() => {})
            }
          })
          .catch(() => {})
        }
        
      } else {
        for(let i=0; i<this.mySelfList.length; i++) {
          setTimeout(() => {
            axios.post(`${SERVER_URL}articles/${this.UserModalId}/selfintroductions/${this.recruitId}/create/`, {
              article: this.UserModalId,
              recruitment: this.recruitId,
              content: this.mySelfList[i].content
            }, config)
            .then(() => {
              if (i===this.mySelfList.length-1) {
                axios.get(`${SERVER_URL}recruitments/${this.recruitId}/apply/${this.UserModalId}`, null, config)
                .then(() => {
                  this.$emit('close')
                })
                .catch(() => {})
              }
            })
            .catch(() => {})
          }, 100 + 100*i);
        }
      }
    },
    onModal(detail) {
      this.setCareerDetail(detail)
      this.showModal = true;
    },
  }
}
</script>