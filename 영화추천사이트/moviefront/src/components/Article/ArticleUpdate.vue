<template>
    <div>
        <br>
        <br>
        <h1>커뮤니티</h1>
        <label for="">Title</label>
        <br>
        <input type="text" v-model="Article.title">
        <p>영화와 관련된 자유로운 의견을 남겨주세요.</p>
        <br>
        <br>
        <label for="">Content</label>
        <br>
        <textarea v-model="Article.content" name="" id="" cols="30" rows="10" ></textarea>
        <br>
        <br>
        <button  @click="onUpdate(ArticleId)" class="btn btn-primary">작성하기</button>

    </div>
</template>

<script>

import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleUpdate',
    data() {
        return {
            Article: {
                title: this.ArticleTitle,
                content: this.ArticleContent,
            }
        }
    },
    props: {
      ArticleTitle: {
        type:String
      },
      ArticleContent: {
        type:String
      },
      ArticleId: {
        type:Number
      }      
    },
    methods: {
        onUpdate(id) {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            console.log(config)
            axios.put(`${SERVER_URL}/articles/${id}/update/`, this.Article, config)
                .then(() => {
                    
                    this.$router.push('/article/')
                })
                .catch(err => {
                    console.log(err.response)
                })
        },
        onTitleChange(event) {
            console.log(event.target.value)
            this.$emit('title-change', event.target.value)
        }
    }



}
</script>

<style>

</style>