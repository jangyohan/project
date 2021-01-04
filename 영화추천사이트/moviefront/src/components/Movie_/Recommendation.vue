<template>
  <div class="container">
    <button @click="Recommend">추천</button>
      <div class='contents'>
        <ul class="row row-cols-8">
          <li class='col' v-for="movie in movielist" :key="movie.id">
            <!-- :href="movie.link" -->
            <a @click="WordCloud(movie.link)"  v-if="movie.image" ><img :src="movie.image" alt=""></a>              
            <a @click="WordCloud(movie.link)"  v-else ><img  src="@/assets/noImg.png" alt=""></a>                           
          </li>
        </ul>          
      </div>
  </div>
</template>

<script>


const SERVER_URL = 'http://127.0.0.1:8000'
import axios from 'axios';

export default {
  name: 'Recommendation',
  data() {
    return {
      year : 2020,
      month : 6,
      count: -1,
      recommendlist: [],
      movielist:[],
    }
  },
  props: {
    IsAdmin: {
      type:Object
    }
  },
  methods:{
    Recommend() {
      this.movielist = []
      this.count += 1
      axios.get(`${SERVER_URL}/movies/recommend/${this.count}`)
        .then(res => {
          // 여기서 데이터 5개를 받음
          this.recommendlist = res.data
          for (let i=0; i<this.recommendlist.length; i++) {
            // 네이버 쪽으로 axios 요청을 보내줌
            const ReTitle = this.recommendlist[i]['title']
            const ReDirector = this.recommendlist[i]['director']

            // 여기까진 문제없음            
            axios.post(`${SERVER_URL}/movies/${ReTitle}/search/`)
              .then(response => {
                // console.log(response.data.items,i,'번째입니다')
                  const unlist = response.data.items
   
                  for (let j=0; j<unlist.length; j++) {

                    const naverTitle = unlist[j]['title']
                    const naverDirector  = unlist[j]['director']

                    // console.log(naverTitle, j, 'second for')
                    // console.log(naverDirector, j ,'seconf for')
                    if (naverTitle.includes(ReTitle) & naverDirector.includes(ReDirector)) {
                      this.movielist.push(unlist[j])
                    }

                  }
                })
              .catch(err => {
                  console.log(err.response)
              })                  
            
            }
            console.log(this.movielist,'마지막이야')
           

            

        })
    }
  },
  created() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
    if (this.isLoggedIn) {
      const token = this.$cookies.get('auth-token')
      axios.get(SERVER_URL + '/accounts/profile/', { headers: {
        Authorization: `Token ${token}`
      }})
        .then(response => {
          this.user = response.data.username
          this.IsAdmin = response.data.is_staff
          this.userid = response.data.id

        })
    }     
    let today = new Date();  
    console.log(today.getFullYear(),today.getMonth())
    let now_year = today.getFullYear()
    // 자바스크립트 월은 0부터 시작
    let now_month = today.getMonth() + 1
    if (this.IsAdmin) {
      if (now_year != this.year || now_month != this.month) {
        console.log('변한게있다')
        axios.post(`${SERVER_URL}/movies/best/`)
          .then(() => {
            console.log('데이터베이스에 새로 커밋했어')
            this.year = now_year
            this.month = now_month
          })
      }
      else {
        console.log('변한게없다')
      }
    }


  }
}
</script>

<style>

</style>