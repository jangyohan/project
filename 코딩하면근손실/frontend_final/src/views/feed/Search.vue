<template>
  <div class="search_section">
    <div class="search col-lg-4">
      <h1 class="h3 text-center mt-4">Search</h1>
      <div class="mx-0">
        <span class="green_window mt-3 text-center">
          <input type="text" class="input_text" v-model="content" />
        </span>
        <button type="submit" class="sch_smit mt-3" @click="findFeed">검색</button>
        <section class="main_feed_card py-4">
          <Feed class="main_feed_background" v-for="feed in feeds" :key="feed.feedNo" :feed="feed" />

        </section>
        <div class="search_footer" v-if="isimage">
          <hr>
          <span class="search_span">검색 결과가 없어요...</span>
          
          <img class="search_img" src="@/assets/img/근육2.png" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Feed from "@/components/feed/Feed.vue";
import axios from "axios";

export default {
  name: "Search",
  components: {
    Feed,
  },
  data() {
    return {
      userData: {
        Uid: localStorage.getItem("nowUid"),
        Email: localStorage.getItem("nowEmail"),
        avatarImage: localStorage.getItem("avatarImage"),
        followers: 567,
        followings: 567,
        posts: 67,
        oneLineIntroduction: localStorage.getItem("usercomment"),
      },
      content: "",
      feeds: {},
      isimage: true
    };
  },
  methods: {
    findFeed() {
      // axios 요청을 통해 데이터베이스에서 feed 찾아와야함
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/feed/feedTagSearch", {
          title: this.content,
        })
        .then(({ data }) => {
          this.feeds = data;
          //let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
          if (this.feeds != null) {
           // msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
            this.showData = true;
          }
          //alert(msg);
          console.log(this.feeds);
          console.log("test" + this.showData);
          this.isimage = false;
        })
        .catch(() => {
          alert("페이지 로딩 시 에러가 발생했습니다.");
          window.location.href = "/main";
        });
    },
  },
};
</script>

<style>
.modal-header {
  text-align: center;
}

.search_section {
  margin: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.search {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 600px;
  margin-top: 55px;
  background-color: #f2f3f5;
}

.green_window {
  display: inline-block;
  width: 80%;
  height: 34px;
  border: 2px solid rgb(23, 196, 197);
  background: white;
}
.input_text {
  width: 90%;
  height: 21px;
  margin: 3px 0 0 -25px;
  border: 0;
  line-height: 21px;
  font-weight: bold;
  font-size: 16px;
  outline: none;
}
.sch_smit {
  width: 20%;
  height: 34px;
  margin: 0;
  border: 0;
  vertical-align: top;
  background: rgb(23, 196, 197);
  color: white;
  font-weight: bold;
  border-radius: 1px;
  border-left: 0px;
  cursor: pointer;
}
.sch_smit:hover {
  background: rgb(133, 196, 197);
}

.main_feed_card_each {
  padding: 20px;
  border-radius: 10px;
  background-color: white;
}
.search_img{
  margin-top:30px;
  width:100%;
  
}
.search_span{
  margin-left:20%;
  font-size:30px;
}
</style>