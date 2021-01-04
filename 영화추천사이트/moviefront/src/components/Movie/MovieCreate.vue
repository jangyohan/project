<template>
  <div class="container">
    <label for="">title </label>
    <input v-model="Data.title" type="text" required>
    <br>
    <label for="">content </label>
    <input v-model="Data.content" type="text" required>
    <br>
    <label for="">post </label>
    <input v-model="Data.post" type="text" required>
    <br>
    <label for="">score </label>
    <input v-model="Data.score" type="text" required>
    <br>
    <label for="">genre </label>
    <input v-model="Data.genre" type="text" required>
    <br>
    <label for="">time </label>
    <input v-model="Data.time" type="text" required>
    <br>
 
    
    <button @click="onCreate">제출</button>
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


