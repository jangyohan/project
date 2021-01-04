template>
  <div>
    <h1>Movie Info</h1>
    <label for="">Title: </label>
    <b-form-input type="text" v-model="Movie.title"></b-form-input>
    <br>
    <br>
    <label for="">Genre: </label>
    <b-form-input type="text" v-model="Movie.genre"></b-form-input>
    <br>
    <br>
    <label for="">Content: </label>
    <b-form-textarea v-model="Movie.content" rows="3" max-rows="6"></b-form-textarea>
    <br>
    <br>
    <button @click="onUpdate(MovieId)" class="btn btn-primary">수정</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieUpdate',
  data() {
    return {
      Movie: {
        title: this.MovieTitle,
        genre: this.MovieGenre,
        content: this.MovieContent,
        post: this.MoviePost,
        score: this.MovieScore,
        time: this.MovieTime
      }
    }    
  },
  props: {
    MovieTitle: String,
    MovieGenre: String,
    MovieContent: String,
    MovieId : Number,
    MoviePost: String,
    MovieScore: String,
    MovieTime: String
  },
  methods: {
    onUpdate(id) {
      const config = {
          headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      axios.put(`${SERVER_URL}/movies/${id}/update/`, this.Movie, config)
          .then(() => {  
              this.$router.push('/all')
          })
          .catch(err => {
              console.log(err.response)
          })
    },
  }
}
</script>

<style scoped>

</style>
