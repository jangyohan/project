<template>
  <div class="wrapC">
    <div class="wrap">
      <div class="form-wrap">
        <div class="p-wrap">
          <p>
            이메일을 통해 받으신 Code 번호와 <br />
            새로운 비밀번호를 입력하세요.
          </p>
        </div>
        <form id="changepw" action="" class="input-group2">
          <input
            type="code"
            v-model="code"
            class="input-field"
            placeholder="Enter code"
            required
          />
          <input
            type="password"
            v-model="password1"
            class="input-field"
            placeholder="Enter Password"
            required
          />
          <input
            type="password"
            v-model="password2"
            class="input-field"
            placeholder="Confirmation Password"
            required
          />
          <input
            type="submit"
            class="submit mt-5"
            value="submit"
            @click="resetPassword"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Changepw",
  data() {
    return {
      code: null,
      password1: null,
      password2: null,
      isok: false,
    };
  },
  methods: {
    resetPassword() {
      if (localStorage.getItem("code") != this.code) {
        alert("code do not match");
      } else {
        if (this.password1 != this.password2) {
          alert("Passwords do not match");
        } else {
          // 데이터 베이스에 변경한 패스워드 저장 로직 작성해야함
          axios
            .post("https://i3b305.p.ssafy.io/muscleloss/api/member/updateMemPw", {
              email: localStorage.getItem("email"),
              password: this.password2,
            })
            .then(({ data }) => {
              let msg = "비밀번호 변경 실패.";
              if (data == 1) {
                this.isok = true;
                msg = "비밀번호 변경 완료.";
              }
              alert(msg);
              window.location.href = "/";
              localStorage.clear();
            })
            .catch(() => {
              alert("비밀번호 변경 시 에러가 발생했습니다.");
              window.location.href = "/";
              localStorage.clear();
            });
        }
      }
    },
  },
};
</script>

<style></style>
