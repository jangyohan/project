<template>
  <div class="wrap">
    <div class="wrap-container search-container">
      <img src="../assets/logo/B104_logo_border.png" alt="#" class="search-logo">
      <div class="search-user-box">
        <input type="text" class="search-input" placeholder="유저이름을 검색하세요" v-model="username" v-on:input="username = $event.target.value">
          <transition-group v-show="username" name='fade' tag="div" class="search-user-group" mode="in-out">
            <p v-if="userList.length===0" key='-1'>검색결과가 없습니다.</p>
            <div class='search-user-item' v-for='user in userList' :key='user.user.id' @click="onModal(user.user.id, 'search')">
              <div class="search-user-img">
                <img v-show="user.image" :src="'https://j3b104.p.ssafy.io/' + user.image" alt="#">
                <img v-show="!user.image" src="../assets/images/default-user.png" alt="#">
              </div>
              <div class="search-user-content">
                <div class="search-user-name">{{ user.name }}</div>
              </div>
            </div>
            <!-- <div v-show="userListLength > 0" class='search-user-more' key='0'>{{ userListLength }}개 더보기</div> -->
          </transition-group>
      </div>
    </div>

    <UserModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios';
import UserModal from '../components/UserModal.vue';
import '../components/css/search.css';
import { mapMutations } from 'vuex';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'Search',
  data() {
    return {
      username: '',
      userList: [],
      userListLength: 0,
      showModal: false,
    }
  },
  components: {
    UserModal,
  },
  computed: {
  },
  mounted() {
  },
  watch: {
    username() {
      if (this.username) {
        this.searchUser()
      }
    }
  },
  methods: {
    ...mapMutations(['setUserModalId', 'setUserDivide']),
    searchUser() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}articles/search/${this.username}/`, null, config)
      .then(res => {
        if(res.data) {
          this.userList = res.data
        } else {
          this.userList = []
        }
      })
      .catch(() => {})
    },
    onModal(id, type) {
      this.setUserModalId(id);
      this.setUserDivide(type)
      this.showModal = true;
    },
  },
}
</script>