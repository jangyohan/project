<template>
  <transition name="modal">
    <div class="buy-search-modal-mask">
      <div class="buy-search-modal-wrap">
        <div class="buy-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='buy-search-modal-header'>이력서를</div>
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
          <div class="buyVideoActive" v-if="eth>1000000+121000" @click="goBuy">구매하기</div>
          <div class="buyVideoNoactive" v-else>구매하기</div>
        </div>
      </div>
      <SignResume :id="id" v-if="isShow" @close="$emit('close');isShow=false"/>
    </div>
  </transition>
</template>

<script>

import './css/buymodal.css'
import { mapState } from 'vuex';
import axios from 'axios';
import SignResume from '../components/SignResume.vue'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'BuyResume',
  data() {
    return {
      eth: '',
      password: '',
      private_key: '',
      ans : false,
      isShow: false,
    }
  },
  watch: {
  },
  props: {
    id: String,
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
  },
  components: {
    SignResume,
  },
  mounted() {
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
    axios.post(`${SERVER_URL}accounts/`, null, config)
        .then((res) => {
          this.eth = res.data.balance
        })
        .catch(() => {
        })
  },
  methods: {
    goBuy() {
      this.isShow = true
    },
  },
}
</script>