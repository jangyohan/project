<template>
  <div class="container">
    <label for="">title </label>
    <b-form-input v-model="Data.title" type="text" required>
    </b-form-input>
    <br>
    <label for="">content </label>
    <b-form-input v-model="Data.content" type="text" required>
    </b-form-input> 
    <br>
    <label for="">post </label>
    <b-form-input v-model="Data.post" type="text" required>
    </b-form-input>      
    <br>
    <label for="">score </label>
    <b-form-input v-model="Data.score" type="text" required>
    </b-form-input>
    <br>
    <label for="">genre </label>
    <b-form-input v-model="Data.genre" type="text" required>
    </b-form-input>  
    <br>
    <label for="">time </label>
    <b-form-input v-model="Data.time" type="text" required>
    </b-form-input>
    <br>
 
    
    <button class="btn btn-success container d-flex justify-content-center" @click="onCreate">제출</button>
  </div>

</template>

<script>

import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCreate',
  data() {
    return {
      Data : {
        title:'',
        content:'',
        post:'',
        score:'',
        genre:'',
        time : '',

      }
    }
  },
  methods: {
    onCreate() {
      const config = {
          headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      console.log(config)
      // ??
      axios.post(`${SERVER_URL}/articles/create/`, this.Data, config)
          .then(() => {
              
              this.$router.push('/article')
          })
          .catch(err => {
              console.log(err.response)
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
    
  }  
}
</script>

<style>

</style>


