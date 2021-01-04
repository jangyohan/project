<template>
  <div class="container">
    <h1>영화리스트</h1>
    <div>
      <Paginatedlist :list-array="pageArray" />
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
    allcreate:{
      type:Boolean
    }
  },
  created () {
    if (this.allcreate) {
    axios.get(`${SERVER_URL}/movies/allmovie/`)
    .then(response => {
      this.pageArray = response.data;
    })
    .catch(err => {
      console.log(err);
    });      

    }
  

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