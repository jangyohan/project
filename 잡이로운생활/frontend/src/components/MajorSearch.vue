<template>
  <transition name="modal">
    <div class="major-search-modal-mask">
      <div class="major-search-modal-wrap">
        <div class="major-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='major-search-modal-header'>전공검색</div>
          <div class='major-search-modal-body'>
            <input v-model="name" class='major-search-valid-input' type="text" v-on:input="name = $event.target.value" @keydown.enter="getMajor(name)">
            <div class="major-submit-btn" @click="getMajor(name)">검색</div>
          </div>
          <div class="major-search-modal-footer">
            <span class='major-search-list' v-for='(major, index) in majorList' :key='`major-${index}`' @click="setMajor(major, majorType, majorType2)">
              {{ major }}
            <br>
            </span>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import './css/major-search.css'
import axios from 'axios'

// const SERVER_URL = 'http://127.0.0.1:8000/'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'MajorSearch',
  data() {
    return {
      name: '',
      majorList: [],
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['majorName', 'majorType', 'majorType2']),
  },
  created() {
    this.name = this.majorName
    this.getMajor(this.majorName)
  },
  mounted() {
    
  },
  methods: {
    ...mapMutations(['selectMajor', 'selectMajorType', 'selectMajorType2']),
    getMajor(name) {
        axios.get('https://www.career.go.kr/cnet/openapi/getOpenApi', {
        params: {
          apiKey: API_KEY,
          svcType: 'api',
          svcCode: 'MAJOR',
          gubun: 'univ_list',
          contentType: 'json',
          searchTitle: name,
        }
      }).then(res => {
        let ARR = []
        for (let i=0; i<res.data.dataSearch.content.length ; i++) {
          ARR.push(res.data.dataSearch.content[i].mClass)
        }
        this.majorList = Array.from(new Set(ARR))
      })
      .catch(() =>{
      })
    },
    setMajor(name, type, type2) {
      this.selectMajor(name)
      this.selectMajorType(type)
      this.selectMajorType2(type2)
      this.$emit('close')
    }
  }
}
</script>