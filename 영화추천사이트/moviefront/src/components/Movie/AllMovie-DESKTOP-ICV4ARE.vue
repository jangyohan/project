<template>
  <div class="container">
    <h1>영화리스트</h1>
    <div>
      <Paginatedlist :list-array="pageArray" @filter="filter" />
    </div>

  </div>
</template>

<script>
import axios from 'axios'

import Paginatedlist from '@/components/Movie/Paginatedlist.vue'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'simple-pagination',
  components: {
    Paginatedlist,
  },
  data () {
    return {
      pageArray: [], 

    }
  },
  props:{
    IsMovie:{
      type:Boolean
    }
  },
  method: {
    filter(selected) {
    console.log(selected)
    console.log('들어왔다')
    axios.get(`${SERVER_URL}/movies/allmovie/${selected}`)
    .then(response => {
      this.pageArray = response.data;
    })
    .catch(err => {
      console.log(err);
    });      
    
    }
  },
  created () {
    const selected = '전체'
   
    axios.get(`${SERVER_URL}/movies/allmovie/${selected}`)
    .then(response => {
      this.pageArray = response.data;
    })
    .catch(err => {
      console.log(err);
    });      

        
  },

  mounted() {
    
  }
}
</script>

<style>
h1 {
  color: #454545;
  text-align: center;
}
</style>