<template>
  <div>
    <div class="my_feed">
      <div class="my_feed_section col-12 col-lg-4">
        <div class="d-flex justify-content-center">
          <div class>
            <h1 class="h3 text-center mb-4">My page</h1>
            <div class="d-flex justify-content-center">
              <div class="avatar avatar-xl">
                <img
                  id="profileChange"
                  class="avatar-img d-block"
                  :src="userData1.avatarImage"
                  alt="avatar"
                />

                <!-- 프로필 사진 변경 코드 작성해야됨 -->
              </div>
            </div>
            <div class="text-center mt-3">
              <h2 class="h5">{{ userData1.Uid }}</h2>
              <p class="small text-muted">{{ userData1.Email }}</p>
            </div>
          </div>
        </div>
        <p
          class="text-center"
          style="cursor: pointer; color:rgb(23, 196, 197);"
          @click="gotoprofile"
        >
          프로필 변경
        </p>
        <div class="d-flex justify-content-center flex-wrap">
          <div class="text-center px-3 py-2" @click="onFollow(1)">
            <p class="small text-muted mb-0">Followers</p>
            <p class="font-weight-bold mb-0">{{ countFollower }}</p>
          </div>
          <div class="text-center px-3 py-2" @click="onFollow(2)">
            <p class="small text-muted mb-0">Following</p>
            <p class="font-weight-bold mb-0">{{ countFollowing }}</p>
          </div>
          <div class="text-center px-3 py-2">
            <p class="small text-muted mb-0">Posts</p>
            <p class="font-weight-bold mb-0">{{ countPost }}</p>
          </div>
        </div>
        <FollowModal v-if="showFollow" @close="showFollow = false" :followDatas="followDatas"/>
        <div class="form-group mt-4 bg-white">
          <label id="oneLineInput" class="text-info" for="oneLine"
            >Introduction</label
          >
          <hr class="mb-1" />
          <textarea
            class="form-control border-0 bg-white"
            id="oneLine"
            rows="3"
            :placeholder="userData1.oneLineIntroduction"
            readonly
          ></textarea>
        </div>
        <div class="btn_group" style="margin-bottom: 16px">
          <button
            class=""
            style="border:solid 1px skyblue;border-radius: 5px;font-size: 13.333px;background-color: white;color: skyblue; padding: 5px; width:50%"
            @click="onMy"
          >
            My Feed
          </button>
          <button
            class=""
            style="border:solid 1px skyblue;border-radius: 5px;font-size: 13.333px;background-color: white;color: skyblue; padding: 5px; width:50%"
            @click="onShare"
          >
            Share Feed
          </button>
        </div>
        <Feed
          class="main_feed_background"
          v-for="feed in feeds"
          :key="feed.feedNo"
          :feed="feed"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Feed from "@/components/feed/Feed.vue";
import FollowModal from "@/components/feed/FollowModal.vue";
import axios from "axios";

export default {
  name: "Mypage",
  components: {
    Feed,
    FollowModal,
  },
  data() {
    return {
      userData1: {
        Uid: localStorage.getItem("nowUid"),
        Email: localStorage.getItem("nowEmail"),
        avatarImage: localStorage.getItem("avatarImage"),
        oneLineIntroduction: localStorage.getItem("usercomment"),
      },
      feeds: {},
      countFollower: null,
      countFollowing: null,
      countPost: null,
      followDatas: [],
      showFollow: false,
    };
  },
  created() {
    axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/feed/feedAllByUser", {
        uid_fk: localStorage.getItem("nowUid"),
      })
      .then(({ data }) => {
        this.feeds = data;
        this.countPost = this.feeds.length;
        // alert(data);
        // console.log(data);
        // alert(this.feeds);
        // let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        if (this.feeds != null) {
          // msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
          localStorage.setItem("moveUserpage", localStorage.getItem("nowUid"));
        }
        // alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/main";
      });

    // follower 수 구하는 axios
    axios
      .get(
        `https://i3b305.p.ssafy.io/muscleloss/api/follow/follower/${localStorage.getItem(
          "nowUid"
        )}`,
        { uid: localStorage.getItem("nowUid") }
      )
      .then(({ data }) => {
        this.countFollower = data;
      })
      .catch((err) => {
        console.log(err);
      });

    // following 수 구하는 axios
    axios
      .get(
        `https://i3b305.p.ssafy.io/muscleloss/api/follow/following/${localStorage.getItem(
          "nowUid"
        )}`,
        { uid: localStorage.getItem("nowUid") }
      )
      .then(({ data }) => {
        this.countFollowing = data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    Logout() {
      window.location.href = "/";
      localStorage.clear();
    },
    gotoprofile() {
      if (
        localStorage.getItem("nowUid") == localStorage.getItem("moveUserpage")
      ) {
        window.location.href = "/profile";
      }
    },
    onFollow(check) {
      this.showFollow = true
      if (check == 1) {
        // follower 리스트 구하는 axios
        axios
          .get(
            `https://i3b305.p.ssafy.io/muscleloss/api/follow/followerlist/${localStorage.getItem("nowUid")}`, { uid: localStorage.getItem("nowUid"),})
          .then(({ data }) => {
            this.followDatas = data;
          })
          .catch((err) => {
            console.log(err)
          });
      }
      else {
         // following 리스트 구하는 axios
        axios
          .get(
            `https://i3b305.p.ssafy.io/muscleloss/api/follow/followinglist/${localStorage.getItem("nowUid")}`, { uid: localStorage.getItem("nowUid"),})
          .then(({ data }) => {
            this.followDatas = data
          })
          .catch((err) => {
            console.log(err)

          });
      }
    },
    onMy() {
      axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/feed/feedAllByUser", {
        uid_fk: localStorage.getItem("nowUid"),
      })
      .then(({ data }) => {
        this.feeds = data;
        this.countPost = this.feeds.length;
        // alert(data);
        // console.log(data);
        // alert(this.feeds);
        // let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        if (this.feeds != null) {
          // msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
          localStorage.setItem("moveUserpage", localStorage.getItem("nowUid"));
        }
        // alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/main";
      });
    },
    onShare() {
       axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/share/feedByShare", {
        uid_fk: localStorage.getItem("nowUid"),
      })
      .then(({ data }) => {
        this.feeds = data;
        this.countPost = this.feeds.length;
        // let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        if (this.feeds != null) {
          // msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
          localStorage.setItem("moveUserpage", localStorage.getItem("nowUid"));
        }
        // alert(msg);
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
.my_feed {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
  background-color: white;
}

.my_feed_section {
  padding-top: 100px;
  background-color: #f2f3f5;
}

.my_feed_card_each {
  padding: 20px;
  border-radius: 10px;
  background-color: #f2f3f5;
}
.form-group {
  border-color: rgb(23, 196, 197);
  border-radius: 5px;
}
.mypage_feed {
  background-color: white;
  margin-bottom: 24px;
  padding: 10px;
  border-radius: 10px;
}
.btn_group {
  width: 100%;
}
</style>
