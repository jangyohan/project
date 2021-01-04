<template>
    <div class="container">
    <b-form-textarea
          id="textarea"
          v-model="Comment.content"
          placeholder="Enter something..."
          rows="3"
          max-rows="6"
        ></b-form-textarea>
        <br>
        <br>
        <button @click="OnWriteComment"  class="btn btn-success">작성</button>
    </div>
</template>

<script>

import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000'


export default {
    name: 'Comment',
    data() {
      return {
        Comment: {
          content: '',
        },
      }
    },
    props: {
      ArticleId: {
        type:Number
      },
    },
    methods: {
      OnWriteComment() {
        const config = {
            headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
        }
        console.log(this.Comment.content)
        console.log(this.ArticleId)
        axios.post(`${SERVER_URL}/articles/${this.ArticleId}/comments/`, this.Comment, config)
            .then(() => {
                
                this.$router.push('/article/')
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