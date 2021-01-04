<template>
  <div id="app">
    <div id="nav">
      <!-- <router-link to="/test" >Test</router-link> | -->
      <router-link v-if="IsAdmin" to="/movie/create" >Create</router-link> |
      <router-link :to="{name:'ArticleList', params:{user:user}}" >Article</router-link> |
      <router-link @click="Movie" :IsMovie="IsMovie" to="/all" >Movie</router-link> |
      <router-link to="/index" :IsAdmin="IsAdmin" >Home</router-link> |
      <span v-if="!isLoggedIn">
        <router-link to="/signup">Signup</router-link> |
        <router-link to="/login">Login</router-link>
      </span>
      <span v-else>
        <router-link to="/logout" @click.native="logout">Logout</router-link>
      </span>
    </div>
    <router-view @login="onLogin" @signup="onSignup" />
  </div>
</template>

<script>

import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
    name: 'App',
    data() {
        return {
          isLoggedIn: false,
          IsAdmin : false,
          user: null,
          userid: null,
          IsMovie: false
        }
    },
    methods: {

      onLogin(loginData) {
        axios.post(`${SERVER_URL}/rest-auth/login/`,loginData)
          .then(res => {
            
            this.$cookies.set('auth-token',res.data.key)
            this.isLoggedIn = true
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

            this.$router.push('/index')
            

          })
          .catch(err => {
            console.log(err.response)
          })
      },
      logout() {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          },
        }
        axios.post(`${SERVER_URL}/rest-auth/logout/`, null, config)
          .then(() => {
            this.$cookies.remove('auth-token')
            this.isLoggedIn = false
            this.IsAdmin = false,
            this.$router.push('/'),
            this.user = null
          })
          .catch(err => {
            console.log(err.response)
          })
      },
      onSignup(signupData) {
        axios.post(`${SERVER_URL}/rest-auth/signup/`,signupData)
          .then(res => {
            this.$cookies.set('auth-token', res.data.key)
            this.isLoggedIn = true
            this.$router.push('/')
            console.log('성공')
          })
          .catch(err => {
            console.log(err.response)
          })
      },
      Movie() {
        this.IsMovie = true
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
     
    },
    mounted() {
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
