<template>
    <div class="container">
        <hr>
        <ul>
            <li v-for="comment in comments" :key="comment.id">
                <p v-if="arr == comment.article"><strong>{{ comment.user.username }}</strong> : {{ comment.content }}</p>
                <br>
                <div  v-if="arr == comment.article">
                    <button v-if="user == comment.user.username" @click="DeleteComment(comment.id)" class="btn btn-danger">삭제</button>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>


import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
    name: 'CommentList',
    data() {
        return {
            arr : this.article.id,
            comments : [],
        }
    },
    props: {
        article: {
            type:Object,
        },
        user: {
            type:String
        }        
    },
    methods: {
        DeleteComment(Id) {
            if (Id) {
                const config = {
                    headers: {
                        Authorization: `Token ${this.$cookies.get('auth-token')}`
                    },
                }            
                axios.delete(`${SERVER_URL}/articles/comments/${Id}/`,config)
                    .then(() =>{
                    this.$router.push('/article')
                    })
                    .catch(err => {
                        console.log(err.response)
                    })                
            }
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


        axios.get(`${SERVER_URL}/articles/comment/`)
            .then(res =>{
                
                this.comments = res.data
                console.log(this.comments)
            })
            .catch(err => {
                console.log(err.response)
            }) 

        
        }     
}
</script>


<style>

</style>