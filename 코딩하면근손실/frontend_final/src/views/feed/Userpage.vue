<template>
  <div class="user_feed">
    <div class="user_feed_section col-12 col-lg-4">
      <div class="d-flex justify-content-center">
        <div class>
          <h1 class="h3 text-center mb-4">{{ moveuserfeeds.uid }} page</h1>
          <div class="d-flex justify-content-center">
            <div class="avatar avatar-xl">
              <img
                id="profileChange"
                class="avatar-img d-block"
                :src="moveuserfeeds.avatarImage"
                alt="avatar"
              />
            </div>
          </div>
          <div class="text-center mt-3">
            <h2 class="h5">{{ moveuserfeeds.uid }}</h2>
            <p class="small text-muted">@{{ moveuserfeeds.email }}</p>
          </div>
        </div>
      </div>
      <!-- follow/unfollow 로직 작성해야함 -->
      <p
        class="text-center text-info"
        style="cursor: pointer;"
        @click="onFollow"
        v-if="isFollowed"
      >
        언팔로우
      </p>
      <p
        class="text-center text-warning"
        style="cursor: pointer;"
        @click="onFollow"
        v-else
      >
        팔로우
      </p>
      <div class="d-flex justify-content-center flex-wrap">
        <div class="text-center px-3 py-2">
          <p class="small text-muted mb-0">Followers</p>
          <p class="font-weight-bold mb-0">{{ countFollower }}</p>
        </div>
        <div class="text-center px-3 py-2">
          <p class="small text-muted mb-0">Following</p>
          <p class="font-weight-bold mb-0">{{ countFollowing }}</p>
        </div>
        <div class="text-center px-3 py-2">
          <p class="small text-muted mb-0">Posts</p>
          <p class="font-weight-bold mb-0">{{ countPost }}</p>
        </div>
      </div>
      <div class="form-group mt-4 bg-white">
        <label id="oneLineInput" class="text-info" for="oneLine"
          >Introduction</label
        >
        <hr class="mb-1" />
        <textarea
          class="form-control border-0 bg-white"
          id="oneLine"
          rows="3"
          :placeholder="moveuserfeeds.usercomment"
          readonly
        ></textarea>
      </div>
      <Feed
        class="main_feed_background"
        v-for="feed in feeds"
        :key="feed.feedNo"
        :feed="feed"
      />
    </div>
    <br />
  </div>
</template>

<script>
import Feed from "@/components/feed/Feed.vue";
import axios from "axios";
export default {
  name: "Userpage",
  components: {
    Feed,
  },

  data() {
    return {
      feeds: {},
      moveuserfeeds: {},
      countFollower: null,
      countFollowing: null,
      countPost: null,
      isFollowed: false,
      followData: {
        follower: localStorage.getItem("nowUid"),
        following: localStorage.getItem("moveUserpage"),
      },
    };
  },
  created() {
    axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/feed/feedAllByUser", {
        uid_fk: localStorage.getItem("moveUserpage"),
      })
      .then(({ data }) => {
        this.feeds = data;
        this.countPost = this.feeds.length;
        // alert(data);
        // console.log(data);
        // alert(this.feeds);
        //let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        if (this.feeds != null) {
          //msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
        }
        //alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/main";
      });

    axios
      .get(
        `https://i3b305.p.ssafy.io/muscleloss/api/member/${localStorage.getItem(
          "moveUserpage"
        )}`,
        {
          uid_fk: localStorage.getItem("moveUserpage"),
        }
      )
      .then(({ data }) => {
        this.moveuserfeeds = data;
        console.log(data);
        console.log(
          "this.moveuserfeeds : " + JSON.stringify(this.moveuserfeeds)
        );
        // let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        // if (this.feeds != null) {
        //   msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
        // }
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
          "moveUserpage"
        )}`,
        { uid: localStorage.getItem("moveUserpage") }
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
          "moveUserpage"
        )}`,
        { uid: localStorage.getItem("moveUserpage") }
      )
      .then(({ data }) => {
        this.countFollowing = data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  mounted() {
    axios
      .post(
        `https://i3b305.p.ssafy.io/muscleloss/api/follow/isFollow/${localStorage.getItem(
          "nowUid"
        )}`,
        this.followData
      )
      .then(({ data }) => {
        if (data == "success") {
          this.isFollowed = true;
        } else {
          this.isFollowed = false;
        }
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    onFollow() {
      if (this.isFollowed == false) {
        axios
          .post(
            "https://i3b305.p.ssafy.io/muscleloss/api/follow/registFollow",
            this.followData
          )
          .then(({ data }) => {
            console.log(data);
            this.countFollower = this.countFollower + 1;
          })
          .catch((err) => {
            console.log(err);
          });
        this.isFollowed = !this.isFollowed;
      } else {
        axios
          .post(
            "https://i3b305.p.ssafy.io/muscleloss/api/follow/deleteFollow",
            this.followData
          )
          .then(({ data }) => {
            console.log(data);
            this.countFollower = this.countFollower - 1;
          })
          .catch((err) => {
            console.log(err);
          });
        this.isFollowed = !this.isFollowed;
      }
      axios
        .get(
          `https://i3b305.p.ssafy.io/muscleloss/api/follow/follower/${localStorage.getItem("moveUserpage")}`,
          { uid: localStorage.getItem("moveUserpage") }
        )
        .then(({ data }) => {
          this.countFollower = data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    onChange() {
      axios
        .get(
          `https://i3b305.p.ssafy.io/muscleloss/api/follow/follower/${localStorage.getItem("moveUserpage")}`,
          { uid: localStorage.getItem("moveUserpage") }
        )
        .then(({ data }) => {
          this.countFollower = data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  watch: {
    countFollower() {
      this.onChange();
    },
  },
};
</script>

<style>
.user_feed {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
  background-color: #f2f3f5;
}

.user_feed_section {
  margin-top: 100px;
}

.user_feed_card_each {
  padding: 20px;
  border-radius: 10px;
  background-color: white;
}

.mypage_feed {
  background-color: white;
  margin-bottom: 24px;
  padding: 10px;
  border-radius: 10px;
}
</style>
