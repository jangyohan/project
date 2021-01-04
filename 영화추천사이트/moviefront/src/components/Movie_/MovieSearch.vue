<template>
    <div class='container'>
        <div class='container'>
          <div class='container d-flex justify-content-center'>
            <label for="Search">영화 정보를 검색해 보세요</label>
            <br>
            <input @keypress.enter="InputMovie"   v-model='keyWord'  id="Search" type="text">
            <button @click='InputMovie' class='btn btn-success'> 검색</button>
          </div>
          <br>
          <p v-if="keyWord"><strong>{{ keyWord }}</strong>에 대한 검색 결과입니다</p>
          <hr>
        </div>
        <br>
        <div class='contents'>
          <ul class="row row-cols-8">
            <li class='col' v-for="movie in movieList" :key="movie.id">
              <!-- :href="movie.link" -->
              <a @click="WordCloud(movie.link)"  v-if="movie.image" ><img :src="movie.image" alt=""></a>              
              <a @click="WordCloud(movie.link)"  v-else ><img  src="@/assets/noImg.png" alt=""></a>                           
            </li>
          </ul>          
        </div>   
        
        <img v-if="IsImage" :src="imgUrl" alt="WordCloud">
        <Recommendation :IsAdmin="IsAdmin" />
      <div>
        <b-carousel
          id="carousel-1"
          v-model="slide"
          :interval="4000"
          controls
          indicators
          background="#ababab"
          img-width="1024"
          img-height="480"
          style="text-shadow: 1px 1px 2px #333;"
          @sliding-start="onSlideStart"
          @sliding-end="onSlideEnd"
        >
          <!-- Text slides with image -->
          <b-carousel-slide
            caption="First slide"
            text="Nulla vitae elit libero, a pharetra augue mollis interdum."
            img-src="https://picsum.photos/1024/480/?image=52"
          ></b-carousel-slide>

          <!-- Slides with custom text -->
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
            <h1>Hello world!</h1>
          </b-carousel-slide>

          <!-- Slides with image only -->
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

          <!-- Slides with img slot -->
          <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
          <b-carousel-slide>
            <template v-slot:img>
              <img
                class="d-block img-fluid w-100"
                width="1024"
                height="480"
                src="https://picsum.photos/1024/480/?image=55"
                alt="image slot"
              >
            </template>
          </b-carousel-slide>

          <!-- Slide with blank fluid image to maintain slide aspect ratio -->
          <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
              a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
            </p>
          </b-carousel-slide>
        </b-carousel>

        <p class="mt-4">
          Slide #: {{ slide }}<br>
          Sliding: {{ sliding }}
        </p>
      </div>
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
            slide: 0,
            sliding: null
  
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
                    this.movieList = res.data.items
                    console.log(res.data.items)
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
    }
}
</script>

<style>
  li {
    list-style: none;
    margin-top: 10px;
  }
  li.col {
    padding: 0rem;
    width: 100px;
  }  
  a:hover {
    color: red;
  }



</style>