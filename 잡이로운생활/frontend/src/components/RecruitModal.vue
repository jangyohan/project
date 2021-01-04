<template>
  <transition name="modal">
    <div class="recruit-modal-mask">
      <div @mousedown.self="$emit('close')">
        <div class="recruit-modal-wrap">
          <div class="recruit-modal-content">
            <i class="fas fa-times" @click.self="$emit('close')"></i>
            <div class='recruit-modal-header'>
              <p class="recruit-modal-corp-name">{{ RecruitName }}</p>
              <p class="recruit-modal-name"><span>{{ RecruitDetail.division }}</span>{{ RecruitDetail.title }}</p>
              <p v-if="RecruitDetail.startdate" class="recruit-modal-date">
                {{RecruitDetail.startdate.substring(0,4)}}.{{RecruitDetail.startdate.substring(4,6)}}.{{RecruitDetail.startdate.substring(6,8)}} 
                {{ RecruitDetail.startdate.substring(8,10) }}:{{ RecruitDetail.startdate.substring(10,) }}
                ~ {{RecruitDetail.deadline.substring(0,4)}}.{{RecruitDetail.deadline.substring(4,6)}}.{{RecruitDetail.deadline.substring(6,8)}} 
                {{ RecruitDetail.deadline.substring(8,10) }}:{{ RecruitDetail.deadline.substring(10,) }}</p>
            </div>
            <div class='recruit-modal-body'>
              <img :src="'https://j3b104.p.ssafy.io/' + RecruitDetail.image" alt="">
            </div>
            <div class="recruit-modal-footer">
              <div v-if="UserInfo.flag===0" class="recruit-modal-btn" @click="goApplicant">지원자목록</div>
              <div v-if="UserInfo.flag===1" class="recruit-modal-btn" @click="onModal(UserInfo.id, 'individual')">지원하기</div>
            </div>
          </div>
        </div>
      </div>

      <UserModal v-if="showModal" @close="showModal= false"/>
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import './css/recruit-modal.css'
import UserModal from '../components/UserModal.vue';
import axios from 'axios'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'RecruitModal',
  data() {
    return {
      showModal: false,
      name: '',
      RecruitDetail: [],
      RecruitName: '',
    }
  },
  components: {
    UserModal,
  },
  watch: {
  },
  computed: {
    ...mapState(['recruitId', 'UserInfo']),
  },
  created() {
  },
  mounted() {
    this.getRecruitDetail();
  },
  methods: {
    ...mapMutations(['setUserModalId', 'setUserDivide', 'setRecruitId']),
    getRecruitDetail() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/${this.recruitId}/`, null, config)
      .then(res => {
        this.RecruitDetail = res.data
        this.RecruitName = res.data.user.last_name
      })
      .catch(() => {})
    },
    goApplicant() {
      this.$router.push(`/corp/recruit/applicant/${this.recruitId}`).catch(()=>{})
    },
    onModal(id, type) {
      this.setUserModalId(id);
      this.setUserDivide(type)
      this.showModal = true;
    },
  },
  beforeDestroy () {
    this.setRecruitId('')
    this.setUserDivide('')
  },
}
</script>