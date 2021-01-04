<template>
  <div>
    <p v-if="data.length == 0" class="mylist-buy">아직 구매한 이력서가 없습니다!</p>
    <div class="list-container"  v-for='(items, idx) in data' :key='`items-${idx}`'>
      <div class="list-box" v-for='(item, index) in items' :key='`item-${index}`'>
        <div class="list-box-in">
          <img v-if="item.image" :src="'https://j3b104.p.ssafy.io/'+item.image" alt="" class="list-box-img">
          <img v-if="!item.image" src="@/assets/images/default-user.png" alt="#" class="list-box-img">
        </div>
        <p class="list-ment">{{ item.name }}님의 이력서</p>
        <div class="list-go" @click="goResume(item.user.id)">보러가기</div>
      </div>
    </div>
  </div>
</template>

<script>
import '../components/css/login.css'
import '../components/css/mylist.css'
import axios from 'axios'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'MyList',
  data() {
    return {
      data: [],
    }
  },
  components: {
  },
  computed: {
  },
  created() {
  },
  mounted() {
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
    axios.post(`${SERVER_URL}accounts/item/list/`, null, config)
        .then((res) => {
          if (res.data.length != 0 ){
            this.data.push(res.data)
          }
        })
        .catch(() => {
        })
  },
  watch: {
  },
  methods: {
    goResume(pk) {
      this.$router.push(`/otherresume/${pk}`)
    }
  },
}
</script>