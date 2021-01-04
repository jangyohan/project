<template>
  <transition name="modal">
    <div class="school-search-modal-mask">
      <div class="school-search-modal-wrap">
        <div class="school-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='school-search-modal-header'>학교검색</div>
          <div class='school-search-modal-body'>
            <input v-model="name" class='school-search-valid-input' type="text" v-on:input="name = $event.target.value" @keydown.enter="getSchool(schoolType, name, schoolDetail)">
            <div class="school-submit-btn" @click="getSchool(schoolType, name, schoolDetail)">검색</div>
          </div>
          <div class="school-search-modal-footer">
            <span class='school-search-list' v-for='(school, index) in schoolList' :key='`school-${index}`' @click="setSchool(school, schoolType2)">
              {{ school }}
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
import './css/school-search.css'
import axios from 'axios'

// const SERVER_URL = 'http://127.0.0.1:8000/'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'SchoolSearch',
  data() {
    return {
      name: '',
      schoolList: [],
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['schoolType', 'schoolType2', 'schoolName', 'schoolDetail']),
  },
  created() {
    this.name = this.schoolName
    this.getSchool(this.schoolType, this.schoolName, this.schoolDetail)
  },
  mounted() {
    
  },
  methods: {
    ...mapMutations(['selectSchool', 'selectSchoolType']),
    getSchool(type, name, num) {
      if (num === 0) {
        axios.get('https://www.career.go.kr/cnet/openapi/getOpenApi', {
        params: {
          apiKey: API_KEY,
          svcType: 'api',
          svcCode: 'SCHOOL',
          gubun: type,
          searchSchulNm: name,
          contentType: 'json'
        }
      }).then(res => {
        let ARR = []
        for (let i=0; i<res.data.dataSearch.content.length ; i++) {
          ARR.push(res.data.dataSearch.content[i].schoolName)
        }
        this.schoolList = Array.from(new Set(ARR))
      })
      .catch(() =>{
      })
    } else {
      axios.get('https://www.career.go.kr/cnet/openapi/getOpenApi', {
        params: {
          apiKey: API_KEY,
          svcType: 'api',
          svcCode: 'SCHOOL',
          gubun: type,
          searchSchulNm: name,
          sch1: num,
          contentType: 'json'
        }
      }).then(res => {
        let ARR = []
        for (let i=0; i<res.data.dataSearch.content.length ; i++) {
          ARR.push(res.data.dataSearch.content[i].schoolName)
        }
        this.schoolList = Array.from(new Set(ARR))
      })
      .catch(() =>{
      })
    }
      
    },
    setSchool(name, type) {
      this.selectSchool(name)
      this.selectSchoolType(type)
      this.$emit('close')
    }
  }
}
</script>