<template>
  <div class="wrap">
    <div class="wrap-container">
      <div class="recruit-write-btn-box">
        <div v-if="!isRecruit" class="recruit-write-btn">작성하기</div>
        <div v-if="isRecruit" class="recruit-write-btn on-write-btn" @click="editRecruit">작성하기</div>
      </div>
      <div class="recruit-write-box">
        <p>기본정보</p>
        <div class="recruit-write-inner-box">
          <label for="">공고명</label><input type="text" v-model="recruit.name" v-on:input="recruit.name = $event.target.value">
          <label for="">구분</label>
          <select name="" id="" v-model='recruit.sort'>
            <option disabled selected>선택</option>
            <option>신입</option><option>경력</option><option>신입/경력</option>
          </select>
        </div>
        <div class="recruit-write-inner-box">
          <label for="">공고자료</label>
          <label for="recruit-write-file" class="recruit-write-file-form">첨부하기</label><input type="file" ccept="image/*" id="recruit-write-file" @change="setImg">
          <span>{{ imgName }}</span>
        </div>
        <div class="recruit-write-inner-box recruit-write-inner-time">
          <label for="">시작시간</label><input type="text" class="long-width" placeholder="YYYY.MM.DD" v-model="recruit.startDate">
          <input type="text" class="short-width" placeholder="HH" v-model="recruit.startHour"><input type="text" class="short-width" placeholder="MM" v-model="recruit.startMin">
          <div></div>
          <label for="">마감시간</label><input type="text" class="long-width" placeholder="YYYY.MM.DD" v-model="recruit.endDate">
          <input type="text" class="short-width" placeholder="HH" v-model="recruit.endHour"><input type="text" class="short-width" placeholder="MM" v-model="recruit.endMin">
        </div>
      </div>
      <div class="recruit-write-box">
        <p>자기소개서</p>
        <div class="recruit-write-certified-box">
          <p v-if="certifiedSelf.length === 0">자기소개서 양식을 입력해주세요.</p>
          <div class='recruit-write-self-list-box' v-for='(self, index) in certifiedSelf' :key='`self-${index}`'>
            <div class="self-detail">{{ index+1 }}.</div>
            <div class="self-detail">{{ self[0] }}</div>
            <div class="self-detail">{{ self[1] }}자</div>
            <div class="self-detail self-del-box" @click="delSelf(index)">x</div>
          </div>
        </div>
        <div class="recruit-write-inner-box recruit-write-selfintro">
          <label for="">제목</label><input type="text" v-model="self.name">
          <label for="">글자수</label><input type="text" v-model="self.length">
        </div>
        <div class="recruit-write-btn-area">
          <div v-if="isSelf" class="recruit-write-self-btn on-write-btn" @click="addSelf">추가하기</div>
          <div v-if="!isSelf" class="recruit-write-self-btn">추가하기</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import '../components/css/recruit-write.css'

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'RecruitWrite',
  data() {
    return {
      imgName: '공고 이미지를 첨부해주세요',
      recruit: {
        name: '',
        sort: '선택',
        img: '',
        startDate: '',
        startHour: '',
        startMin: '',
        endDate: '',
        endHour: '',
        endMin: '',
        id: '',
      },
      self: {
        name: '',
        length: '',
      },
      isSelf: false,
      isRecruit: false,
      certifiedSelf: [],
    }
  },
  components: {
  },
  computed: {
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
  },
  watch: {
    self: {
      handler() {
        this.checkSelfForm();
        this.checkWriteForm();
      }, deep:true
    },
    recruit: {
      handler() {
        this.checkWriteForm();
      }, deep:true
    },
    certifiedSelf() {
      this.checkWriteForm();
    }
  },
  methods: {
    handleScroll() {
      const ORIGIN = -600
      let TOP = window.scrollY
      document.querySelector('.recruit-write-btn').style.bottom = (ORIGIN - TOP) + 'px';
    },
    setImg() {
      const photoFile = document.getElementById("recruit-write-file");
      this.imgName = photoFile.files[0].name
      this.recruit.img = photoFile.files[0]
    },
    editRecruit() {
      this.splitDate()
      let data = new FormData();
      data.append('image', this.recruit.img);
      data.append('division', this.recruit.sort);
      data.append('title', this.recruit.name);
      data.append('startdate', this.recruit.startDate + this.recruit.startHour + this.recruit.startMin)
      data.append('deadline', this.recruit.endDate + this.recruit.endHour + this.recruit.endMin)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}recruitments/create/`, data, config)
      .then(() => {
        axios.get(`${SERVER_URL}recruitments/`, null, config)
        .then(res => {
          this.recruit.id = res.data[res.data.length-1].id
          // 리스트에서 마지막 배열의 id를 받아와야함
          for (let i=0; i<this.certifiedSelf.length; i++) {
            axios.post(`${SERVER_URL}recruitments/${this.recruit.id}/introductions/create/`, {
              title : this.certifiedSelf[i][0],
              number : this.certifiedSelf[i][1],
              recruitment : this.recruit.id
            }, config)
            .then(() => {
              this.$router.push('/corp/recruit').catch(()=>{})
            })
            .catch(() => {})
          }
        })
        .catch(() => {})
      })
      .catch(() => {})
    },
    checkSelfForm() {
      if (this.self.name && this.self.length) {
        this.isSelf = true
      } else {
        this.isSelf = false
      }
    },
    checkWriteForm() {
      if (this.recruit.name && (this.recruit.sort && this.recruit.sort != '선택') && this.recruit.img
      && this.recruit.startDate && this.recruit.startHour && this.recruit.startMin
      && this.recruit.endDate && this.recruit.endHour && this.recruit.endMin && this.certifiedSelf[0]) {
        this.isRecruit = true
      } else {
        this.isRecruit = false
      }
    },
    addSelf() {
      let ARR = []
      ARR.push(this.self.name); ARR.push(this.self.length);
      this.certifiedSelf.push(ARR)
      this.self.name = ''; this.self.length = '';
    },
    delSelf(idx) {
      this.certifiedSelf.splice(idx, 1);
    },
    splitDate() {
      const arr = this.recruit.startDate.split('.')
      const arr2 = this.recruit.endDate.split('.')
      this.recruit.startDate = ''
      this.recruit.endDate = ''
      for(let i=0; i<arr.length; i++) {
        this.recruit.startDate += arr[i]
      }
      for(let j=0; j<arr.length; j++) {
        this.recruit.endDate += arr2[j]
      }
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>