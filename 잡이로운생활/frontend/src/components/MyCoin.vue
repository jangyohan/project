<template>
  <div class="coin-container">
    <div class="coin-container-in">
      <div class="ether-img">
        <img src="../assets/images/ETHEREUM-ICON_Black_small.png" alt="" class="ether-img-in">
      </div>
    </div>
    <div class="coin-detail-under">
      <div class="coin-name-title">
        <p class="coin-name-on">사용자</p>
      </div>
      <div class="coin-balance-title">
        <p class="coin-balance-on">잔액</p>
      </div>
      <div class="coin-email-title">
        <p class="coin-email-on">이메일</p>
      </div>
    </div>
    <div class="coin-detail">
      <div class="coin-name">
        <p class="coin-name-in">{{ last_name }}{{ name }}</p>
      </div>
      <div class="coin-balance">
        <p class="coin-balance-in">{{ money }} (ETH)</p>
      </div>
      <div class="coin-email">
        <p class="coin-email-in">{{ email }}</p>
      </div>
    </div>
    <div class="coin-address">
      <p class="coin-address-in">내 주소 : </p>
      <p class="coin-address-under">{{ addr }}</p>
      <div class="coin-btn"><p class="coin-contract" @click="goMycontract">구매내역 보러가기</p></div>
    </div>
  </div>
</template>

<script>
import '../components/css/login.css'
import '../components/css/mycoin.css'
import axios from 'axios'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'MyCoin',
  data() {
    return {
      money: 0,
      name: '',
      email: '',
      addr: '',
      last_name: '',
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
    axios.post(`${SERVER_URL}accounts/`, null, config)
        .then((res) => {
          this.money = res.data.balance
          this.name = res.data.first_name
          this.email = res.data.email
          this.addr = res.data.wallet_addr
          this.last_name = res.data.last_name
        })
        .catch(() => {
        })
  },
  watch: {
  },
  methods: {
    goMycontract() {
      this.$router.push('/mycontract')
    }
  },
}
</script>