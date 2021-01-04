<template>
  <div>
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex flex-row align-items-center">
        <div class="avatar mr-3">
          <img
            class="avatar-img"
            :src="userprofileimage"
            alt="avatar"
            @click="moveUserpage(feed.uid_fk)"
          />
        </div>
        <div>
          <h2
            class="h6 mb-0"
            style="cursor: pointer;"
            @click="moveUserpage(feed.uid_fk)"
          >
            {{ feed.uid_fk }}
          </h2>
          <p class="small text-muted mb-0">{{ timeForToday(feed.regdate) }}</p>
        </div>
      </div>
      <button
        v-if="feed.uid_fk==user"
        class="btn btn-icon btn-text-dark dropdown-toggle"
        data-toggle="dropdown"
        aria-expanded="false"
      >
        <i class="fas fa-ellipsis-v"></i>
      </button>
      <ul
        class="dropdown-menu dropdown-menu-right"
        v-if="feed.uid_fk == nowUserUid"
      >
        <li>
          <a class="dropdown-item" href="#" @click="feedDelete(feed.feedNo)">삭제</a>
        </li>
      </ul>
    </div>
    <img class="rounded w-100 mt-3" :src="image" alt="feed" />
    <div class="">
      <p class="h5 mt-2 mb-1">{{ feed.content }}</p>
      <transition-group name="fade" tag="div" class="modal_hash_group_modify mr-1">
        <div
          class="modal_hash_group_list text-small"
          v-for="(hash, index) in hashList"
          :key="`hash-${index}`"
        >
          {{ hash }}
        </div>
      </transition-group> 
    </div>
    <div class="d-flex justify-content-between">
      <div class="d-flex align-items-center">
        <button class="btn btn-text-dark pl-0" type="button" @click="onLike(feed.uid_fk)">
          <i v-if="isLiked" class="fas fa-heart text-danger mt-1"></i>
          <i v-else class="far fa-heart mr-1 mt-1"></i>
          {{ countLike }}
        </button>
        <button
          class="btn btn-text-dark"
          type="button"
          @click="showComment = true"
        >
          <i class="far fa-comment-alt mt-1"></i>
        </button>
      </div>
      <button class="btn btn-text-dark" type="button" @click="onShare(feed.uid_fk)">
        <i v-if="isShared" class="fas fa-share text-danger mt-1"></i>
        <i v-else class="fas fa-share text-dark mr-1 mt-1"></i>
      </button>
    </div>
    <CommentModal
      v-if="showComment"
      @close="showComment = false"
      :feedNo="feed.feedNo"
    />
  </div>
</template>

<script>
import CommentModal from "@/components/feed/CommentModal.vue";
import axios from "axios";

export default {
  name: "Feed",
  components: {
    CommentModal,
  },
  props: {
    feed: Object,
  },
  data() {
    return {
      nowUserUid: localStorage.getItem("nowUid"),
      feedimgsrc: "",
      userprofileimage: "",
      image: "",
      feedfileName: this.feed.fileName,
      item: {},
      showComment: false,
      isLiked: null,
      countLike: null,
      commentDatas: {},
      likeData: {
        feedNo_fk: this.feed.feedNo,
        uid_fk: localStorage.getItem("nowUid"),
      },
      hashList: [],
      user: localStorage.getItem("nowUid"),
      isShared: null,
      shareData: {
        feedNo_fk: this.feed.feedNo,
        uid_fk: localStorage.getItem("nowUid")
      },

    };
  },
  created() {
    console.log("avatarImageSrc : " + localStorage.getItem("avatarImageSrc"));
    console.log("this.feedfileName : " + this.feedfileName);
    axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/feed/getfeedimage", {
        userimage: localStorage.getItem("avatarImageSrc"),
        fileName: this.feedfileName,
      })
      .then(({ data }) => {
        this.item = data;
        this.userprofileimage = this.item.userimage;
        this.image = this.item.fileName;
      })
      .catch((error) => {
        console.log(error.response);
        alert("DB에서 image 호출 시 에러가 발생했습니다.");
      });
  },
  methods: {
    feedModify() {},
    timeForToday(value) {
      const today = new Date();
      const timeValue = new Date(value);

      const betweenTime = Math.floor(
        (today.getTime() - timeValue.getTime()) / 1000 / 60
      );
      if (betweenTime < 1) return "방금전";
      if (betweenTime < 60) {
        return `${betweenTime}분전`;
      }

      const betweenTimeHour = Math.floor(betweenTime / 60);
      if (betweenTimeHour < 24) {
        return `${betweenTimeHour}시간전`;
      }

      const betweenTimeDay = Math.floor(betweenTime / 60 / 24);
      if (betweenTimeDay < 365) {
        return `${betweenTimeDay}일전`;
      }

      return `${Math.floor(betweenTimeDay / 365)}년전`;
    },
    onLike(uid_feed) {
      console.log(uid_feed);
      if (this.isLiked == false) {
        axios
          .post(
            `https://i3b305.p.ssafy.io/muscleloss/api/like/updatelike/${uid_feed}`, 
              this.likeData
          )
          .then(({ data }) => {
            console.log(data);
            this.countLike = this.countLike + 1;
          })
          .catch((err) => {
            console.log(err);
          });
        this.isLiked = !this.isLiked;
      } else {
        axios
          .post(
            `https://i3b305.p.ssafy.io/muscleloss/api/like/deletelike`,
            this.likeData
          )
          .then(({ data }) => {
            console.log(data);
            console.log(this.isLiked);
            this.countLike = this.countLike - 1;
          })
          .catch((err) => {
            console.log(err);
            console.log(this.isLiked);
          });
        this.isLiked = !this.isLiked;
      }
      axios
        .get(
          `https://i3b305.p.ssafy.io/muscleloss/api/like/countlike/${this.likeData.feedNo_fk}`
        )
        .then(({ data }) => {
          this.countLike = data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    onChange() {
      axios
        .get(
          `https://i3b305.p.ssafy.io/muscleloss/api/like/countlike/${this.likeData.feedNo_fk}`
        )
        .then(({ data }) => {
          this.countLike = data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    moveUserpage(uid_fk) {
      localStorage.setItem("moveUserpage", uid_fk);
      if (
        localStorage.getItem("moveUserpage") == localStorage.getItem("nowUid")
      ) {
        window.location.href = "/mypage";
      } else {
        window.location.href = "/userpage";
      }
    },
    feedDelete(feedNo) {
      console.log("feedNo : " + feedNo);
      axios
        .post(`https://i3b305.p.ssafy.io/muscleloss/api/feed/feedDelete/${feedNo}`)
        .then(({ data }) => {
          console.log(data);
          alert("feed 삭제 성공!!");
          window.location.href = "/main";
        })
        .catch((err) => {
          console.log(err);
          alert("feed 삭제 실패!!");
          window.location.href = "/main";
        });
    },
    onShare(uid_feed) {
      if (this.isShared == false) {
        axios
          .post(
            `https://i3b305.p.ssafy.io/muscleloss/api/share/registershare/${uid_feed}`,
            this.shareData
          )
          .then(() => {
            
          })
          .catch((err) => {
            console.log(err);
          });
        this.isShared = !this.isShared;
      } else {
        axios
          .post(
            "https://i3b305.p.ssafy.io/muscleloss/api/share/deleteshare",
            this.shareData
          )
          .then(({ data }) => {
            console.log(data);
            
          })
          .catch((err) => {
            console.log(err);
          });
        this.isShared = !this.isShared; 
        }
    },
  },
  mounted() {
    axios
      .post(
        "https://i3b305.p.ssafy.io/muscleloss/api/like/checklike",
        this.likeData
      )
      .then(({ data }) => {
        if (data == "success") {
          this.isLiked = true;
        } else {
          this.isLiked = false;
        }
      })
      .catch((err) => {
        console.log(err);
      });

    axios
      .get(
        `https://i3b305.p.ssafy.io/muscleloss/api/like/countlike/${this.likeData.feedNo_fk}`
      )
      .then(({ data }) => {
        this.countLike = data;
      })
      .catch((err) => {
        console.log(err);
      });
    var step = 0
    var temp = ''
    for(step; step < this.feed.title.length; step++) {
      if(this.feed.title[step]==';'){
        this.hashList.push(temp)
        temp = ''
      }
      else {
        temp = temp + this.feed.title[step]
      }
    }
    //isShared axios
    axios
      .post(
        "https://i3b305.p.ssafy.io/muscleloss/api/share/checkshare",
        this.shareData
      )
      .then(({ data }) => {
        if (data == "success") {
          this.isShared = true;
        } else {
          this.isShared = false;
        }
      })
      .catch((err) => {
        console.log(err);
      });
  },
  watch: {
    countLike() {
      this.onChange();
    },
  },
};
</script>

<style scoped>
.modal_hash_group_modify{
  margin-top:5px;
}
.modal_hash_group_list {
  display: inline-block;
  margin-right: 5px;

  margin-left: 0px;
  margin-bottom: 5px;
  border-radius: 5px;
  color: white;
  background-color: rgb(23, 196, 197);
  padding-left: 10px;
  padding-right: 10px;
  font-size: 15px;
}
</style>