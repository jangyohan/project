<template>
  <div>
    <button @click="test">test</button>
    <b-form-select v-model="selected" :options="options" @onchange="filter"></b-form-select>
    <br>
    <br>     
    <table>
      <tr >
        <th>NO</th>
        <th>POST</th>
        <th>TITLE</th>
        <th>GENRE</th>
      </tr>
      <tr  v-for="movie in paginatedData" :key="movie.id">
        <td>{{ movie.id }}</td>
        <td><img :src=movie.post alt=""></td>
        <td><router-link :to="{name:'MovieDetail', params:{movie_id:movie.id, movie:movie}}">{{ movie.title }}</router-link></td>
        <td>{{ movie.genre }}</td>
      </tr>
    </table>
  
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Paginatedlist',
  data () {
    return {
      pageNum: 0,
        selected: '전체',
        options: [
          { value: '전체', text: '전체' },
          { value: '액션', text: '액션' },
          { value: '코미디', text: '코미디' },
          { value: '드라마/모험', text: '드라마/모험' },
          { value: '멜로/로맨스', text: '멜로/로맨스' },
          // 공포랑 스릴러 병합해서 처리하기
          { value: '공포/스릴러', text: '공포/스릴러' },
          // SF랑 판타지 병합래서 처리하기
          { value: 'SF/판타지', text: 'SF/판타지' },
          { value: '애니메이션', text: '애니메이션' },
          { value: '다큐멘터리', text: '다큐멘터리' },
          { value: '서부', text: '서부' },
        ],

    }
  },
  props: {
    listArray: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 10
    },
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    filter() {
      console.log(this.selected)
    },
    test() {
      console.log(this.paginatedData)
      console.log(this.listArray)
    }

  },
  computed: {
    pageCount () {
      let listLeng = this.listArray.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    //categorizedData () {
    // 밑에다가 listArray를 categorizedDate로 치환
    //},
    categorizedData () {
      if (this.selected == '전체') {
        return this.listArray
      }
      else {
        let FilterData = []
        for (var i=0; i<this.listArray.length; i++) {
          if (this.selected.includes(this.listArray[i]['genre'] )) {
            FilterData.push(this.listArray[i])
          }
        }
        return FilterData
      }
    },
    paginatedData () {


      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.categorizedData.slice(start, end);
    }
  },
}
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}
table th {
  font-size: 1.2rem;
}
table tr {
  height: 2rem;
  text-align: center;
  border-bottom: 1px solid #505050;
}
table tr:first-of-type {
  border-top: 2px solid #404040;
}
table tr td {
  padding: 1rem 0;
  font-size: 1.1rem;
}
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
img {
  height: 100px;
  width: 100px;
}
</style>


