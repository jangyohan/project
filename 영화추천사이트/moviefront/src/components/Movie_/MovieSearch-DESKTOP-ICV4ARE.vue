<template>
    <div class='container'>
        <div class='container'>
          <div class='container d-flex justify-content-center'>
            <div>
              <label for="Search">영화 정보를 검색해 보세요</label>     
              <div>              
                <input @keypress.enter="InputMovie"   v-model='keyWord'  id="Search" type="text">
                <button @click='InputMovie' class='btn btn-success'> 검색</button>
              </div>                         
            </div>
            <br>

            

          </div>
          <br>
          <p v-if="keyWord"><strong>{{ keyWord }}</strong>에 대한 검색 결과입니다</p>
          <hr>
        </div>
        <br>
        <!-- Button trigger modal -->
        
  


        <div class='contents container'>
          <tr class="row row-cols-8">
            <td class='col' v-for="movie in movieList" :key="movie.key_id">
              <p  class="" data-toggle="modal" :data-target="'#' + 'modal' +  movie.key_id " @click="WordCloud(movie.link)"  v-if="movie.image" ><img :src="movie.image" alt=""></p> 
              <p class="" data-toggle="modal" :data-target="'#' + 'modal' + movie.key_id"  @click="WordCloud(movie.link)"  v-else ><img src="@/assets/noImg.png" alt=""></p>     
              

              <!-- Modal -->
              <div class="modal fade" :id="'modal' + movie.key_id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <div class="">
                        <h5 class="modal-title" id="exampleModalLabel" v-html="movie.title" ></h5>
                      </div>
                      
                      
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                    <br>
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
                        <img  class="wordcloud container d-flex justify-content-center" v-if="IsImage" :src="imgUrl" alt="WordCloud">                        
                      </div>
                    
                      
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    </div>
                  </div>
                </div>
              </div>                                      
            </td>
          </tr>          
        </div>   
        
        <Recommendation :IsAdmin="IsAdmin" />
        
 
    </div>  
</template>

<script>

import axios from 'axios'
import Recommendation from '@/components/Movie_/Recommendation.vue'

const SERVER_URL = 'http://127.0.0.1:8000'
export default {
    name: 'MovieView',
    components: {
      Recommendation,
   
    },
    data(){
        return {
            keyWord: '',
            movieList: [],
            imgUrl: '',
            IsImage:false,

  
        }
    },
    props: {
      IsAdmin: {
        type:Object
      }
    },
    methods: {
        InputMovie() {
            axios.post(`${SERVER_URL}/movies/${this.keyWord}/search/`)
                .then(res =>{
                    this.movieList = res.data
                    console.log(res.data)
                })
                .catch(err => {
                    console.log(err.response)
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
    }
}
</script>

<style scoped>
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
  li {
    list-style: none;
  }



</style>