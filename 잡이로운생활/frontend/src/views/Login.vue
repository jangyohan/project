<template>
  <div class="login-container">
    <div class="login-form-box">
      <div class="login-button-box">
        <div id="login-btn"></div>
        <div class="login-toggle-btn login-toggle" @click="onLogin">Login</div>
        <div class="login-toggle-btn signup-toggle" @click="onSignup">Signup</div>
      </div>
      <div class="login-logo-img" @click="goHome">
        <img src="@/assets/logo/KakaoTalk_20201007_204737312.png" alt="">
      </div>
      <p class='login-logo-text' @click="goHome">JOB이로운세상</p>
      <form id="login" class="login-input-group">
        <p v-if="!isLoginValid" class='signup-err-msg'>이메일 또는 비밀번호를 확인하세요.</p>
        <input v-model="loginMail" type="email" class="login-input-field" placeholder="이메일" required @keydown.enter="goLogin">
        <input v-model="loginPassword" type="password" class="login-input-field" placeholder="비밀번호" required @keydown.enter="goLogin">
        <div v-show="!isLoginBtn" class="login-submit-btn">Login</div>
        <div v-show="isLoginBtn" class="login-submit-btn on-login-btn" @click="goLogin">Login</div>
      </form>
      <form id="signup" class="login-input-group">
        <p v-if='!passwordSchema.validate(signUpPassword) && (signUpPassword.length>0)' class='signup-err-msg'>비밀번호는 영문, 숫자 포함 8자리 이상이어야 합니다.</p>
        <p v-if='(passwordSchema.validate(signUpPassword)) && (signUpPassword != signUpPasswordConfirm)' class='signup-err-msg'>비밀번호가 일치하지 않습니다.</p>
        <div class="sigup-sort-box">
          <input type="radio" name="signup-sort" id="individual-user" checked @click="signupSort('individual')"><label for="individual-user" class='individual-user-label'>개인회원</label>
          <input type="radio" name="signup-sort" id="corporation-user" @click="signupSort('corporation')"><label for="corporation-user" class="corporation-user-label">기업회원</label>
        </div>
        <div class="signup-email">
          <input v-model="signUpMail" type="email" class="login-input-field login-input-email" placeholder="이메일" required>
          <span @click="onModal">인증받기</span>
        </div>
        <div v-if="isIndiv" class='signup-name'>
          <input v-model="signUpFirst" type="text" class="login-input-field login-input-first" placeholder="이름" required>
          <input v-model="signUpLast" type="text" class="login-input-field login-input-last" placeholder="성" required>
        </div>
        <div v-if="!isIndiv" class='signup-name'>
          <input v-model="signUpCorpNum" type="text" class="login-input-field" placeholder="사업자번호" required>
          <input v-model="signUpCorpName" type="text" class="login-input-field login-input-corp" placeholder="기업이름" required>
        </div>
        <input v-model="signUpPassword" type="password" class="login-input-field" placeholder="비밀번호" required>
        <input v-model="signUpPasswordConfirm" type="password" class="login-input-field" placeholder="비밀번호 확인" required>
        <div v-show="!isSignBtn" class="login-submit-btn">Signup</div>
        <div v-show="isSignBtn" class="login-submit-btn on-login-btn" @click="setSignup">Signup</div>
      </form>
    </div>

    <MailValidationModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';
import MailValidationModal from '../components/MailValidationModal.vue'
import PasswordValidator from 'password-validator'
import '../components/css/login.css'
import axios from 'axios';
import Swal from 'sweetalert2'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'Login',
  data() {
    return {
      showModal: false,
      loginMail: '',
      loginPassword: '',
      signUpMail: '',
      signUpFirst: '',
      signUpLast: '',
      signUpCorpNum: '',
      signUpCorpName: '',
      signUpPassword: '',
      signUpPasswordConfirm: '',
      isLoginValid: true,
      isSignBtn: false,
      isLoginBtn: false,
      isPasswordValid: false,
      isIndiv: true,
      passwordSchema: new PasswordValidator(),
      private_key: '',
    }
  },
  components: {
    MailValidationModal,
  },
  computed: {
    ...mapState(['mailValid', 'loginPath', 'UserInfo']),
  },
  created() {
    this.passwordSchema
      .is().min(8)
      .is().max(100)
      .has().digits()
      .has().letters();
  },
  mounted() {
    this.setIsLogin(true)
    if (this.loginPath === 'login') {
      this.onLogin()
    } else {
      this.onSignup()
    }
  },
  watch: {
    signUpMail() {
      this.checkSingupForm()
    },
    signUpFirst() {
      this.checkSingupForm()
    },
    signUpLast() {
      this.checkSingupForm()
    },
    signUpPassword() {
      this.checkPassword()
      this.checkSingupForm()
    },
    signUpPasswordConfirm() {
      this.checkPassword()
      this.checkSingupForm()
    },
    mailValid() {
      this.checkSingupForm()
    },
    loginMail() {
      this.checkLoginForm()
    },
    loginPassword() {
      this.checkLoginForm()
    },
  },
  methods: {
    ...mapMutations(['setIsLogin', 'setMailInput', 'setMailCode', 'setIsLoggedIn', 'setToken', 'setMailValid']),
    ...mapActions(['setUserInfo']),
    onLogin() {
      const LOGIN = document.getElementById('login');
      const SIGNUP = document.getElementById('signup');
      const BTN = document.getElementById('login-btn');
      const FORM = document.querySelector('.login-form-box');
      const LOGIN_TOGGLE = document.querySelector('.login-toggle');
      const SIGNUP_TOGGLE = document.querySelector('.signup-toggle');

      LOGIN.style.left = "50px";
      SIGNUP.style.left = "450px";
      BTN.style.left = "0";
      FORM.style.height = "480px";
      LOGIN_TOGGLE.style.color = 'rgba(0,0,0,0.8)'
      SIGNUP_TOGGLE.style.color = 'rgba(0,0,0,0.3)'
    },
    onSignup() {
      const LOGIN = document.getElementById('login');
      const SIGNUP = document.getElementById('signup');
      const BTN = document.getElementById('login-btn');
      const FORM = document.querySelector('.login-form-box');
      const LOGIN_TOGGLE = document.querySelector('.login-toggle');
      const SIGNUP_TOGGLE = document.querySelector('.signup-toggle');

      LOGIN.style.left = "-400px";
      SIGNUP.style.left = "50px";
      BTN.style.left = "50%";
      FORM.style.height = "610px";
      LOGIN_TOGGLE.style.color = 'rgba(0,0,0,0.3)'
      SIGNUP_TOGGLE.style.color = 'rgba(0,0,0,0.8)'
    },
    goHome() {
      this.$router.push('/').catch(()=>{})
    },
    goLogin() {
      const loginData = {
        email: this.loginMail,
        password: this.loginPassword
      }

      axios.post(SERVER_URL + 'rest-auth/login/', loginData)
        .then(res => {
          this.isLoginValid = true
          this.$cookies.set('auth-token', res.data.key)
          this.setToken(res.data.key)
          this.setIsLoggedIn(true)
          this.setUserInfo(this.$cookies.get('auth-token'));
          this.$router.push('/').catch(()=>{})
        })
        .catch(() => this.isLoginValid = false)
    },
    onModal() {
      this.showModal = true;
      this.setMailInput(this.signUpMail)
      axios.post(SERVER_URL + `accounts/${this.signUpMail}/`)
        .then(res => {
          this.setMailCode(res.data.result)
        })
        .catch(() => {}
         )
    },
    checkSingupForm() {
      if(this.signUpMail && ((this.signUpFirst && this.signUpLast) || this.signUpCorpNum ) && this.signUpPassword && 
      this.signUpPasswordConfirm && this.mailValid && this.isPasswordValid) {
        this.isSignBtn = true
      } else {
        this.isSignBtn = false
      }
    },
    checkLoginForm() {
      if(this.loginMail && this.loginPassword) {
        this.isLoginBtn = true
      } else {
        this.isLoginBtn = false
      }
    },
    checkPassword() {
      if((this.signUpPassword == this.signUpPasswordConfirm) && this.passwordSchema.validate(this.signUpPassword)) {
        this.isPasswordValid = true
      } else {
        this.isPasswordValid = false
      }
    },
    setSignup() {
      let signupData = {
        email: this.signUpMail,
        password1: this.signUpPassword,
        password2: this.signUpPasswordConfirm,
        first_name: this.signUpFirst,
        last_name: this.signUpLast
      }
      if(this.isIndiv === false) {
        signupData.first_name = this.signUpCorpNum;
        signupData.last_name = this.signUpCorpName;
      }
      axios.post(SERVER_URL + 'rest-auth/signup/', signupData)
        .then(res => {
          this.$cookies.set('auth-token', res.data.key)
          this.setToken(res.data.key)
          this.setIsLoggedIn(true)
          if(this.isIndiv === false) {
            const config = {
              headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
              }
            }
            axios.post(`${SERVER_URL}accounts/0/`, null, config)
              .then(() => {
                this.setUserInfo();
              })
            .catch(() => {})
          } else {
            this.setUserInfo();
          }
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.post(`${SERVER_URL}articles/create/`, {
            name: this.signUpLast + this.signUpFirst,
            email: this.signUpMail
          }, config)
          .then(() => {
          })
          .catch(() => {})        
          axios.post(SERVER_URL + `accounts/wallet/${this.signUpPassword}/`, {}, {
                        headers: {
                          Authorization: `Token ${this.$cookies.get('auth-token')}`
                        }
                      }
                )
              .then(res => {
                // 개인키 발급 => 향후 이것으로 결제 . 자기 계정인것을 증명
                this.private_key = res.data
              })
          let timerInterval
          Swal.fire({
            title: '잠시만 기다려주세요!',
            html: '현재 지갑을 생성중입니다',
            timer: 15000,
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
              if(this.isIndiv === false) {
                this.$router.push({name:'RecruitHome', params:{first: true, private_key: this.private_key}}).catch(()=>{})
              } else {
                this.$router.push({name:'ResumeEdit', params:{first: true, private_key: this.private_key}}).catch(()=>{})
              }
            }
            // <int:article_pk>/certificates/create
            // this.createCertificate()
            // this.createLang()
            // this.createCareer()
          })
          .catch(() => {})

          
        })
        .catch(err => {
          if(err.response.data.email) {
            Swal.fire({
              icon: 'error',
              title: '다른 이메일을 사용해주세요',
              text: `${err.response.data.email}`,
            })
          }
        })
        let timerInterval
        Swal.fire({
          title: '아이디 생성중입니다!',
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
        }).then(() => {
          /* Read more about handling dismissals below */

        })
    },
    signupSort(type) {
      if (type === 'individual') {
        this.isIndiv = true
        this.signUpCorpNum = ""
      } else {
        this.isIndiv = false
        this.signUpFirst = ""; this.signUpLast = ""
      }
    },
    createCertificate() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      let data = new FormData();
      data.append('article', this.UserInfo.id);
      axios.post(`${SERVER_URL}articles/${this.UserInfo.id}/certificates/create/`, data, config)
      .then(() => {
      })
      .catch(() => {})
    },
    createLang() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      let data = new FormData();
      data.append('article', this.UserInfo.id);
      axios.post(`${SERVER_URL}articles/${this.UserInfo.id}/languages/create/`, data, config)
      .then(() => {
      })
      .catch(() => {})
    },
    createCareer() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      let data = new FormData();
      data.append('article', this.UserInfo.id);
      axios.post(`${SERVER_URL}articles/${this.UserInfo.id}/careers/create/`, data, config)
      .then(() => {
        Swal.fire({
          icon: 'success',
          title: '환영합니다',
          confirmButtonText: '확인'
        }).then((result) => {
          if (result.value) {
            this.$router.push('/resume/edit').catch(()=>{})
          }
        })
      })
      .catch(() => {})
    }
  },
  beforeDestroy() { 
    this.setIsLogin(false)
    this.setMailValid(false)
  }
}
</script>