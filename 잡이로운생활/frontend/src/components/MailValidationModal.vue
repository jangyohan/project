<template>
  <transition name="modal">
    <div class="mail-modal-mask">
      <div class="mail-modal-wrap">
        <div class="mail-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='mail-modal-header'>계정을 <br> 인증하세요.</div>
          <div class='mail-modal-footer'>{{ email }}으로 <br>전송된 인증번호를 입력하세요.</div>
          <input v-model="validInput" class='mail-valid-input' type="text">
          <div v-if="!isSubmit" class='mail-valid-btn'>제출</div>
          <div v-if="isSubmit" class='mail-valid-btn mail-modal-submit' @click='codeValidation'>제출</div>
          <div class='mail-valid-btn mail-modal-re' @click='reSubmit'>다시보내기</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import './css/mail-validation-modal.css'
import axios from 'axios'
import Swal from 'sweetalert2'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'MailValidationModal',
  data() {
    return {
      email: "default@ssafy.com",
      validInput: '',
      isSubmit: false,
    }
  },
  watch: {
    validInput() {
      this.onSubmit()
    },
  },
  computed: {
    ...mapState(['signUpInput', 'mailCode']),
  },
  created() {
    this.email = this.signUpInput
  },
  methods: {
    ...mapMutations(['setMailCode', 'setMailValid']),
    onSubmit() {
      if (this.validInput) {
        this.isSubmit = true
      } else {
        this.isSubmit = false
      }
    },
    codeValidation() {
      if (this.validInput == this.mailCode) {
        Swal.fire({
          icon: 'success',
          title: '인증번호가 일치합니다.',
          confirmButtonText: '확인'
        }).then((result) => {
          if (result.value) {
            this.setMailValid(true)
            this.$emit('close')
          }
        })
      } else {
        this.setMailValid(false)
        Swal.fire({
          icon: 'error',
          title: '인증번호가 일치하지 않습니다.',
          confirmButtonText: '확인'
        })
      }
    },
    reSubmit() {
      axios.post(SERVER_URL + `accounts/${this.email}/`)
        .then(res => {
          this.setMailCode(res.data.result)
          console.log(res.data.result)
        })
        .catch(() =>
          {})
    }
  }
}
</script>