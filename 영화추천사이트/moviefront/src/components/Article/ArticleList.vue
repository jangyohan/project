<template>
    <div class='container'>
        <button v-if="WriteView" @click="onWrite" class="btn btn-success">글쓰기</button>
        <br>    
        <ArticleCreate v-if="!isViewList" @onWrite="onWrite" />


        <h1 v-if="isViewList">게시판</h1>
        <br>
        <table v-if="isViewList" class="table">
        <thead >
            <tr>
            <th scope="col">No</th>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
            </tr>
        </thead>
        <tbody v-for="article in articles" :key="article.id">
            <tr>
            <th  scope="row">{{ article.id }}</th>
            <td  @click="ListView"><router-link  :to="{name:'ArticleDetail', params:{article_id:article.id,article:article, user:user}}">{{ article.title }}</router-link></td>
            <td >
                {{ article.user.username }}
            </td>

        <router-view/>
            </tr>
        </tbody>

        </table>
        
        
    </div>
</template>

<script>


import ArticleCreate  from '@/components/Article/ArticleCreate.vue'
import Vue from 'vue'
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleListView',
    data() {
        return {
            isViewList: true,
            articles: [],
            WriteView : null,
            IsList: true
            
        }
    },
    components: {
        ArticleCreate 
    },
    props: {
        user: {
            type:String
        },

    },
    methods: {
        onWrite() {
            this.isViewList = !this.isViewList
            console.log('된다')
        },
        ListView() {
            this.IsList = false
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

        axios.get(`${SERVER_URL}/articles/`)
            .then(res =>{
                
                
                this.articles = res.data
  
  
            })
            .catch(err => {
                console.log(err.response)
            })


        }
    }


</script>

<style>

</style>