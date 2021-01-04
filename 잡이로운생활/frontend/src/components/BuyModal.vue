<template>
  <transition name="modal">
    <div class="buy-search-modal-mask">
      <div class="buy-search-modal-wrap">
        <div class="buy-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='buy-search-modal-header'>영상을</div>
          <div class='buy-search-modal-header'>구매하시겠습니까?</div>
          <div class="buy-modal-buy">
            가격 : <p class="price">1000000 (ETH)</p>
          </div>
          <div class="buy-modal-buy">
            수수료 : <p class="price">121000 (gas)</p>
          </div>
          <div class="buy-modal-buy">
            내 잔액 : <p class="price-eth">{{ eth }} (ETH)</p>
          </div>
          <div class="buyVideoActive" v-if="eth>1000000+121000" @click="isShow=true">구매하기</div>
          <div class="buyVideoNoactive" v-else>구매하기</div>
        </div>
      </div>
      <SignModal v-if="isShow" @close="isShow=false" :videoName="videoName"/>
    </div>
  </transition>
</template>

<script>
import './css/buymodal.css'
import { mapState } from 'vuex';
import axios from 'axios';
import Swal from 'sweetalert2'
import SignModal from '../components/SignModal.vue'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'BuyModal',
  props: {
    videoName: String,
  },
  components: {
    SignModal,
  },
  data() {
    return {
      eth: '',
      password: '',
      private_key: '',
      isShow: false,
      ans : false,
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
  },
  mounted() {
    this.eth = this.UserInfo.balance
  },
  methods: {
    goBuy() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const Data = {
        "password": "qhdrb111",
        "private_key": "0x7cd2b121a879d9f38cde85e37bd3102ee707bd093878e4327ed4c97846445c95",
        "video": this.videoName
      }
      axios.post(`${SERVER_URL}accounts/video/${this.UserInfo.id}/`, Data, config)
      .then(res => {
        if (res.data.result == 'fail') {
          this.ans = true
        } else {
          this.ans = false
        }
      })
      .catch(() => {})
      let timerInterval
          Swal.fire({
            title: '잠시만 기다려주세요!',
            html: '상품을 구매중입니다',
            timer: 8000,
            timerProgressBar: true,
            showConfirmButton: false,
            willOpen: () => {
              Swal.showLoading()
              timerInterval = setInterval(() => {
                const content = Swal.getContent()
                if (content) {
                  const b = content.querySelector('b')
                  if (b) {
                    b.textContent = Swal.getTimerLeft()
                  }
                }
              }, 100)
            },
            onClose: () => {
              clearInterval(timerInterval)
            }
          }).then((result) => {
            /* Read more about handling dismissals below */
            if (result.dismiss === Swal.DismissReason.timer) {
              if (this.ans == true) {
              Swal.fire({
                icon: 'error',
                title: '구매에 실패하였습니다.',
                text: '비밀번호 혹은 서명을 확인해주세요!'
              })} 
              else {
                this.$router.go('/video')
              }
                
            }
            // <int:article_pk>/certificates/create
            // this.createCertificate()
            // this.createLang()
            // this.createCareer()
          })
    }
  },
}
</script>