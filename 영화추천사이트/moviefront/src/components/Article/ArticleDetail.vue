<template>
    <div>
        <div class="container" v-if="NotModifing">
            <h1>{{ article.title }}</h1>
            <h2>{{ article.content }}</h2>
            <h3>{{ article.created_at }}</h3>
            <button :id="article.id" v-if="user == article.user.username" class="btn btn-danger" @click="DeleteArticle(article.id)">삭제</button>
            <button :id="article.id" v-if="user == article.user.username"  class="btn btn-danger" @click="Update(article.id)">수정</button>        
            <Comment v-if="WriteView" :ArticleId="article.id" />
            <br>
            <br>
            <CommentList :user="user" :article="article" />
        </div>
        <div class="container" v-else>
            <ArticleUpdate :ArticleTitle="article.title" :ArticleContent="article.content" :ArticleId="article.id"  />
        </div>

    </div>
</template>

<script>

import axios from 'axios'
import Vue from 'vue'

const SERVER_URL = 'http://127.0.0.1:8000'

import Comment from '@/components/Article/Comment.vue'
import CommentList from '@/components/Article/CommentList.vue'
import ArticleUpdate from '@/components/Article/ArticleUpdate.vue'

export default {
    name: "ArticleDetail",
    data() {
        return {
            NotModifing: true,
            WriteView: false,
        }
    },
    components: {
        Comment,
        CommentList,
        ArticleUpdate
    },
    methods: {
        DeleteArticle(Id) {
            if (Id) {
                const config = {
                    headers: {
                        Authorization: `Token ${this.$cookies.get('auth-token')}`
                    },
                }            
                axios.delete(`${SERVER_URL}/articles/${Id}/delete/`,config)
                    .then(() =>{
                    this.$router.push('/article')
                    })
                    .catch(err => {
                        console.log(err.response)
                    })                
            }
        },         
        Update() {
           this.NotModifing = !this.NotModifing
        },
    },
    props: {
        article: {
            type:Object
        },
        user: {
            type:String
        }
    },
    created() {
        // 로그인일 때 작성 가능
       if (Vue.$cookies.isKey('auth-token')) {
            this.WriteView = true
        }
       else {
            this.WriteView = false
        }
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