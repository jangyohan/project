<template>
  <transition name="modal">
    <div class="mail-modal-mask">
      <div class="mail-modal-wrap">
        <div class="mail-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div>
            <h2>비밀번호를 입력하세요</h2>
            <input type="password" class='mail-valid-input' v-model="password" placeholder="비밀번호를 입력하세요">
            <h2>서명을 해주세요</h2>
            <input class='mail-valid-input' v-model="key" placeholder="개인키를 입력하세요">
          </div>
          <div class='mail-valid-btn mail-modal-submit' @click="goBuy">확인</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import './css/mail-validation-modal.css'
import Swal from 'sweetalert2'
import axios from 'axios'
import { mapState } from 'vuex';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'SignResume.vue',
  data(){
    return {
      password: '',
      key: '',
    }
  },
  props: {
    id: String,
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  mounted() {
  },
  methods: {
        goBuy() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const Data = {
        "password": this.password,
        "private_key": this.key
      }
      axios.post(`${SERVER_URL}accounts/item/${this.id}/`, Data, config)
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
          timer: 10000,
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
              this.$emit('close')

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