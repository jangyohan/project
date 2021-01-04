<template>
  <div class="container">
    <b-badge style="width: 100%;"  @click="Recommend" variant="success">추천</b-badge>
<!-- Button trigger modal -->

      <div class='contents'>
        <ul class="row row-cols-8">
          <li class='col' v-for="movie in movielist" :key="movie.id">
            <a type="button" class="" data-toggle="modal" :data-target="'#' + 'modal' +  movie.id"  @click="WordCloud(movie.link)"  v-if="movie.image" ><img class="recommend" :src="movie.image" alt=""></a>              
            <a type="button" class="" data-toggle="modal" :data-target="'#' + 'modal' +  movie.id" @click="WordCloud(movie.link)"  v-else ><img class="recommend" src="@/assets/noImg.png" alt=""></a>
            <div class="modal fade" :id="'modal' + movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel" v-html="movie.title"></h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                    <div class="modal-body ">
                      <img class="modal-image container d-flex justify-content-center" :src="movie.image" alt="">
                      <br>
                      <p><strong>감독</strong> : {{ movie.director }}</p>
                      <br>
                      <p><strong>배우</strong> : {{ movie.actor }}</p>
                      <br>
                      <p><strong>개봉년도</strong> : {{ movie.pubDate }}</p>
                      <br>
                      <p><strong>평점</strong> : {{ movie.userRating }}</p>

                      <div>
                        <a :href="imgUrl"><img  class="wordcloud container d-flex justify-content-center" v-if="IsImage" :src="imgUrl" alt="WordCloud"></a>
                        <!-- <img  class="wordcloud container d-flex justify-content-center" v-if="IsImage" :src="imgUrl" alt="WordCloud">                         -->
                      </div>
                    
                      
                    </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                  </div>
                </div>
              </div>
            </div>                                       
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
      slide: 0,
      sliding: null,
      imgUrl: '',
      IsImage:false,            
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
                  const unlist = response.data
   
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
    },
    WordCloud(link) {
      var beforeStr = link
      var afterStr = beforeStr.split('=');
      var key = afterStr[1]
      axios.get(`${SERVER_URL}/movies/info/${key}/`)
        .then(() => {
          axios.get(`${SERVER_URL}/media/image/${key}.jpg/`)
            .then(res => {
              this.imgUrl = res.config.url
              this.IsImage = true
            })
            .catch(err => {
              console.log(err.response)
            })
        })
    },     
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
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

<style scoped>
  li {
    list-style: none;
  }
  img.recommend {
    height: 100%;
    width:  100%;
    max-width:600px; 
    min-width:100px; 
    max-height:300px; 
    min-height:100px;    
  }
  img.modal-image {
    height: 70%;
    width:  100%;
    max-width:400px; 
    min-width:100px; 
    max-height:300px; 
    min-height:100px;


  }
  img.wordcloud {
    height: 90%;
    width:  100%;
    max-width:400px; 
    min-width:100px; 
    max-height:300px; 
    min-height:100px;


  }    

</style>