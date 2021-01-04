<template>
  <div>
    <div class="main_feed">
      <div class="main_feed_section col-12 col-lg-4 order-lg-1">
        <div class="main_feed_write">
          <div class="main_feed_write_picture">
            <img class="modal_avatar_img" :src="userData.avatarImage" alt="avatar" />
          </div>
          <div class="main_feed_write_write">
            <textarea
              class="form-control border border-white"
              id="show-modal"
              @click="showModal = true"
              rows="3"
              :placeholder="
                `${userData.Uid}` + ' 님 무슨 생각을 하고 계신가요?'
              "
            ></textarea>
          </div>
          <FeedModal v-if="showModal" @close="showModal = false" :userData="userData" >
            <h3 slot="header">게시물 만들기</h3>
          </FeedModal>
        </div>
        <section class="main_feed_card py-4">
          <Feed class="main_feed_background" v-for="feed in feeds" :key="feed.feedNo" :feed="feed" />
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import Feed from "@/components/feed/Feed.vue";
import FeedModal from "@/components/feed/FeedModal.vue";
import axios from "axios";

export default {
  name: "Main",
  components: {
    Feed,
    FeedModal,
  },

  data() {
    return {
      showModal: false,
      userData: {
        Uid: localStorage.getItem("nowUid"),
        Email: localStorage.getItem("nowEmail"),
        avatarImage: localStorage.getItem("avatarImage"),
        followers: 567,
        followings: 567,
        posts: 67,
        oneLineIntroduction: localStorage.getItem("usercomment"),
      },
      feeds: {},
      hashList: []
    };
  },

  created() {
    axios
      .get("https://i3b305.p.ssafy.io/muscleloss/api/feed/feedAll", {})
      .then(({ data }) => {
        this.feeds = data;
        //let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        if (this.feeds != null) {
          //msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
        }
        //alert(msg);
        console.log(this.feeds);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/";
      });
  },
  methods: {
    Logout() {
      window.location.href = "/";
      localStorage.clear();
    },
  },

};
</script>

<style>
.modal-header {
  text-align: center;
}
.main_feed {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
  background-color: #fff;
}

.main_feed_write {
  display: flex;
  margin-top: 50px;
  border-radius: 3px;
  border-radius: 10px;
  background-color: white;
  border-style: solid;
  border-color: white;
}
.main_feed_write_picture {
  margin: auto;
  margin-left: 5px;
  margin-right: 7px;
}
.main_feed_write_write {
  width: 100%;
}
.main_feed_section {
  margin-top: 30px;
  background-color: #f2f3f5;
}
.main_feed_background {
  background-color: white;
  margin-bottom: 24px;
  padding: 10px;
  border-radius: 10px;
}
.main_feed_header {
  text-align: center;
}
.main_feed_card_each {
  padding: 20px;
  border-radius: 10px;
  background-color: white;
}
</style>