<template>
  <div class="wrapC">
    <div class="wrap">
      <div class="form-wrap">
        <div class="button-wrap">
          <div id="btn"></div>
          <button type="button" class="togglebtn" @click="login()">
            LOG IN
          </button>
          <button type="button" class="togglebtn" @click="register()">
            REGISTER
          </button>
        </div>
        <div class="login_logo">
          <img class="login_logo_img" src="@/assets/img/근육3.png" alt="">
        </div>
        <form id="login" action class="input-group" v-on:submit.prevent>
          <input
            type="text"
            class="input-field"
            placeholder="User email"
            v-model="useremail"
            required
          />
          <input
            type="password"
            class="input-field"
            placeholder="Enter Password"
            v-model="userpwd"
            required
          />
          <span class="span_login">
            <router-link to="/findpw">Forgot your password?</router-link>
          </span>
          <button class="submit" @click="loginHandler">Login</button>
        </form>
        <form id="register" action class="input-group" v-on:submit.prevent>
          <input
            type="text"
            class="input-field"
            placeholder="User name or Email"
            v-model="U_id"
            required
          />
          <input
            type="email"
            class="input-field"
            placeholder="Your Email"
            v-model="U_email"
            required
          />
          <input
            type="password"
            class="input-field"
            placeholder="Enter Password"
            v-model="U_password1"
            required
          />
          <input
            type="password"
            class="input-field"
            placeholder="Confirmation Password"
            v-model="U_password2"
            required
          />
          <button class="submit mt-4" @click="registerHandler">REGISTER</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      fb: require("../../assets/img/fb.png"),
      gl: require("../../assets/img/gl.png"),
      tw: require("../../assets/img/tw.png"),
      useremail: "",
      userpwd: "",
      U_id: "",
      U_email: "",
      U_password1: "",
      U_password2: "",
      avatarImage: require("../../assets/img/person.png"),
      usercomment: "Hi, Nice to meet you.",
      // usertoken: '',
      item: {},
    };
  },
  computed: {
    ...mapGetters(["token"]),
  },
  methods: {
    login() {
      var x = document.getElementById("login");
      var y = document.getElementById("register");
      var z = document.getElementById("btn");
      x.style.left = "50px";
      y.style.left = "450px";
      z.style.left = "0";
    },
    register() {
      var x = document.getElementById("login");
      var y = document.getElementById("register");
      var z = document.getElementById("btn");
      x.style.left = "-400px";
      y.style.left = "50px";
      z.style.left = "110px";
    },
    loginHandler() {
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/member/login", {
          email: this.useremail,
          password: this.userpwd,
        })
        .then(({ data }) => {
          this.item = data;
          // alert(this.item);
          // alert(this.item.email);
          let msg = "로그인 정보가 정확하지 않습니다.";
          if (this.item.email != null) {
            msg = "로그인이 완료되었습니다.";
          }
          alert(msg);
          if (this.item.email != null) {
            localStorage.setItem("nowUid", this.item.uid);
            localStorage.setItem("nowEmail", this.useremail);
            // 실제 유저프로필 이미지. avatarImage.
            localStorage.setItem("avatarImage", this.item.avatarImage);
            // 유저프로필 이미지의 저장경로. avatarImageSrc.
            localStorage.setItem("avatarImageSrc", this.item.avatarImageSrc);
            localStorage.setItem("usercomment", this.item.usercomment);
            // alert('토큰 정보'+this.item.token);
            // this.usertoken = this.item.token;
            localStorage.setItem("nowToken", this.item.token);
            //alert("토큰 생성이 완료됐습니다.");
            window.location.href = "/main";
          }
        })
        .catch(() => {
          alert("로그인 시 에러가 발생했습니다.");
          window.location.href = "/";
        });
    },
    registerHandler() {
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/member/signUp", {
          uid: this.U_id,
          email: this.U_email,
          password: this.U_password1,
          interest1: "",
          interest2: "",
          interest3: "",
          avatarImage: this.avatarImage,
          imgtype: "image/png",
          usercomment: "Hi, Nice to meet you.",
        })
        .then(({ data }) => {
          this.isok = data;
          // alert(this.isok);
          let msg = "회원가입실패.";
          if (this.isok != null) {
            msg = "회원가입성공.";
          }
          alert(msg);
          if (this.isok != null) {
            window.location.href = "/";
          }
        })
        .catch(() => {
          alert("회원가입 시 에러가 발생했습니다.");
          window.location.href = "/";
        });
    },
  },
};
</script>
<style >
.login_logo{
  width:50px;
  height:50vh;
}
.login_logo_img{
  width:100%;
  margin-left:150px;
}
</style>
