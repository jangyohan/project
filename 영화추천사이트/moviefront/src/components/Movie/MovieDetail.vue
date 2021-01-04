<template>
  <div class="container">
    <div class="card container" style="width: 25rem;" v-if="NotModifing">
      <img :src= movie.post class="card-img-top" alt="...">
      <div class="card-body">
        <h3 class="card-title">{{ movie.title }}</h3>
        <h5 class="card-title text-warning">{{ movie.genre }}</h5>
        <p class="card-text">{{ movie.content }}</p>
        <button v-if="IsAdmin" :id="movie.id" class="btn btn-danger mr-3" @click="Update(movie.id)">수정</button>
        <button v-if="IsAdmin" :id="movie.id" class="btn btn-danger" @click="DeleteMovie(movie.id)">삭제</button>
      </div>
    </div>
    <div class="container" v-else>
      <MovieUpdate :MovieTitle="movie.title" :MovieGenre="movie.genre" :MovieContent="movie.content" :MovieId="movie.id" :MovieScore="movie.score" :MoviePost="movie.post" :MovieTime="movie.time"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieUpdate from '@/components/Movie/MovieUpdate.vue'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetail',
  props: {
    movie: Object,
    user: String,
  },
  data() {
    return {
      NotModifing: true,
      IsAdmin: false,
      isLoggedIn: false
    }
  },
  components: {
    MovieUpdate,
  },
  methods: {
    DeleteMovie(Id) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}` 
        },
      }
      axios.delete(`${SERVER_URL}/movies/${Id}/delete/`, config)
        .then(() => {
          this.$router.push('/all')
        })
        .catch(err => {
          console.log(err.response)
        })
    },
    Update() {
      this.NotModifing = !this.NotModifing
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
          this.IsAdmin = response.data.is_staff
        })
    }
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
    if (this.isLoggedIn) {
      const token = this.$cookies.get('auth-token')
      axios.get(SERVER_URL + '/accounts/profile/', { headers: {
        Authorization: `Token ${token}`
      }})
        .then(response => {
          this.IsAdmin = response.data.is_staff
        })
    }
  }    
}  
</script>

<style scoped>
img {
  width: 100%;
  height: 20%;
}

</style>
