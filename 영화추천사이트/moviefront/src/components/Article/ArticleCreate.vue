<template>
    <div>
        <br>
        <br>
        <h1>커뮤니티</h1>
        <label for="">Title</label>
        <br>
        <input v-model="Article.title" type="text">
        <p>영화와 관련된 자유로운 의견을 남겨주세요.</p>
        <br>
        <br>
        <label for="">Content</label>
        <br>
        <textarea v-model="Article.content" name="" id="" cols="30" rows="10"></textarea>
        <br>
        <br>
        <button  @click="onArticle"  @mouseup="$emit('onWrite')"   class="btn btn-primary">작성하기</button>

    </div>
</template>

<script>

import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleCreateView',
    data() {
        return {
            Article: {
                title: null,
                content: null,  
               
            }
        }
    },
    props: {
        isViewList: {
            type:Boolean
        }
    },
    methods: {
        onArticle() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            console.log(config)
            axios.post(`${SERVER_URL}/articles/create/`, this.Article, config)
                .then(() => {
                    console.log(this.Article)

                })
                .catch(err => {
                    console.log(err.response)
                })
        }
    }



}
</script>

<style>

</style>