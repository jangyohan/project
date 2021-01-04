<template>
  <!--관리자만 볼수있는 페이지 설정을 따로 해야함.-->
  <div class="container">
    <h1 style="text-align: center">User List</h1>
    <hr />
    <div class="column">
      <div v-for="(user, index) in users" v-bind:key="index" class="user-wrap">
        <h2 style="color:blue">No. {{ index + 1 }}</h2>
        <!--       
        <table border="3" style="text-align: center">
          <tr>
            <th>아이디(닉네임)</th>
            <th>이메일</th>
            <th>비밀번호</th>
            <th>가입날짜</th>
            <th>관심키워드1</th>
            <th>관심키워드2</th>
            <th>관심키워드3</th>
          </tr>
          <tr>
            <td>{{ user.uid }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.password }}</td>
            <td>{{ user.create_date }}</td>
            <td>{{ user.interest1 }}</td>
            <td>{{ user.interest2 }}</td>
            <td>{{ user.interest3 }}</td>
          </tr>
        </table>
        -->
        <dl>
          <dt>유저아이디(닉네임)</dt>
          <dd>{{ user.uid }}</dd>
          <dt>유저이메일</dt>
          <dd>{{ user.email }}</dd>
          <dt>관심키워드1</dt>
          <dd>{{ user.interest1 }}</dd>
          <dt>관심키워드2</dt>
          <dd>{{ user.interest2 }}</dd>
          <dt>관심키워드3</dt>
          <dd>{{ user.interest3 }}</dd>
        </dl>
        <hr />
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "UserList",
  data() {
    return {
      users: {},
    };
  },
  created() {
    axios
      .get("https://i3b305.p.ssafy.io/muscleloss/api/member/userlist", {})
      .then(({ data }) => {
        this.users = data;

        let msg = "데이터베이스에서 유저리스트를 가져오지 못했습니다.";
        if (this.users != null) {
          msg = "데이터베이스에서 유저리스트를 가져왔습니다.";
        }
        //alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/";
      });
  },
};
</script>
<style></style>
