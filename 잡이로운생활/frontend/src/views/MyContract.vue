<template>
  <div class="contract">
    <div class="contract-container" v-for='(items, idx) in data' :key='`items-${idx}`'>
      <div class="contract-in" v-for='(item, index) in items' :key='`item-${index}`'>
        <div v-if="item.from_pk==0"  class="item-comment">
          <p v-if="item.value==1000000">자격증 등록</p>
          <p v-else>회원가입</p>
          <p>블록 No. : {{ item.blockNumber }}</p>
          <p>트랜잭션 : {{ item.tx_hash }}</p>
          <p>거래시간 : {{ item.created_at}}</p>
          <p v-if="item.value==1000000"><span class="money">{{ item.value }}</span>(ETH)을 입금 받았습니다.</p>
          <p v-else><span class="money">{{ item.value }}</span>(ETH)을 입금 받았습니다.</p>
        </div>
        <div v-else-if="item.from_pk==UserInfo.id && item.to_pk==0"  class="item-comment">
          <p>영상구매</p>
          <p>블록 No. : {{ item.blockNumber }}</p>
          <p>트랜잭션 : {{ item.tx_hash }}</p>
          <p>거래시간 : {{ item.created_at}}</p>
          <p><span class="money">{{ item.value }}</span>(ETH)을 입금 하였습니다. </p>
          <p>수수료 : {{item.gas}} (gas)</p>
        </div>
        <div v-else-if="item.from_pk==UserInfo.id && item.to_pk!=0"  class="item-comment">
          <p>이력서 구매</p>
          <p>블록 No. : {{ item.blockNumber }}</p>
          <p>트랜잭션 : {{ item.tx_hash }}</p>
          <p>거래시간 : {{ item.created_at}}</p>
          <p><span class="money">{{ item.value }}</span>(ETH)을 입금 하였습니다. </p>
          <p class="gas">수수료 : {{item.gas}} (gas)</p>
        </div>
        <div v-else-if="item.from_pk!=0 && item.to_pk==UserInfo.id"  class="item-comment">
          <p>이력서 판매</p>
          <p>블록 No. : {{ item.blockNumber }}</p>
          <p>트랜잭션 : {{ item.tx_hash }}</p>
          <p>거래시간 : {{ item.created_at}}</p>
          <p><span class="money">{{ item.value }}</span>(ETH)을 입금 받았습니다. </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '../components/css/login.css'
import '../components/css/mycontract.css'
import { mapState } from 'vuex';
import axios from 'axios'
const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'


export default {
  name: 'MyContract',
  data() {
    return {
      data: [],
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
  },
  mounted() {
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
    axios.post(`${SERVER_URL}accounts/transaction/list/`, null, config)
      .then(res => {
        this.data.push(res.data)
      })
      .catch(() => {})
  },
  methods: {
  } 
}
</script>