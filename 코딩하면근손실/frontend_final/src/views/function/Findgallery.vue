<template>
  <div class="main_Findgallery">
        <div class="Findgallery_term col-lg-4 col-12">
                <button i class="Findgallery_term_button fas fa-running fa-2x" @click="onFeed(1)"></button>
                <button i class="Findgallery_term_button fas fa-futbol fa-2x" @click="onFeed(2)"></button>
                <button i class="Findgallery_term_button fas fa-dumbbell fa-2x" @click="onFeed(3)"></button>
                <button i class="Findgallery_term_button2 fas" @click="onFeed(4)">ETC</button>
        </div>
        <div class="Findgallery_section col-lg-4">
            <div class="main_find_feed_write">
                <div class="main_find_feed_write_picture">
                    <img class="modal_avatar_img" :src="userData.avatarImage" alt="avatar" />
                </div>
                <div class="main_find_feed_write_write">
                    <textarea
                    class="form-control border border-white"
                    id="show-modal"
                    @click="showModal = true"
                    rows="3"
                    :placeholder="
                        `${userData.Uid}` + ' 님 우리 같이 운동해요!'
                    "
                    ></textarea>
                </div>
                <FindgalleryModal v-if="showModal" @close="showModal = false" :userData="userData" />
            </div>
            <section class="main_find_feed_card py-4">
                <FindgalleryFeed class="main_find_feed_background" v-for="feed in feeds" :key="feed.meetNo" :feed="feed"/>
            </section>
        </div>
</div>
</template>

<script>
import FindgalleryFeed from "@/components/feed/FindgalleryFeed.vue";
import FindgalleryModal from "@/components/feed/FindgalleryModal";
import axios from "axios";

export default {
    name:"Findgallery",
    components:{
        FindgalleryFeed,
        FindgalleryModal,
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
    };
  },
  methods: {
    Logout() {
      window.location.href = "/";
      localStorage.clear();
    },
    onFeed(number) {
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/meet/meetAllByCategory", { category: number})
        .then(({ data }) => {
          console.log("피드불러오기")
          this.feeds = data
        })
        .catch((err) => {
          console.log(err)
        });
      }
  },

}
</script>

<style>
.main_Findgallery{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0;
    background-color: #fff;
}
.Findgallery_section{
    margin-top: 100px;
    width:100%;
    background-color: #f2f3f5;

}
.Findgallery_term{
    display:flex;
    position:fixed !important ;
    z-index:5000;
    margin-top:55px;
    width:100%;
    padding-left: 0px !important;
    padding-right:0px !important;
}
.Findgallery_term_button {
    border:none;
    border-top: 2px solid white;
    border-right: 2px solid white;
    background-color: rgb(23, 196, 197);
    color: white;
    width:33.33333333333333333333%;
    padding:3px;
    margin:0px;  
}
.Findgallery_term_button2{
    border:none;
    border-top: 2px solid white;
    background-color: rgb(23, 196, 197);
    color: white;
    width:33.33333333333333333333%;
    padding:3px;
    margin:0px;
    font-size:23px;

}
.Findgallery_term_button:focus {
    outline:none;
}
.Findgallery_term_button2:focus {
    outline:none;
}
.Findgallery_term_button:active{
  background-color: gray;
}
.Findgallery_term_button2:active{
  background-color: gray;
}
.main_find_feed_write {
  display: flex;
  margin-top: 30px;
  border-radius: 3px;
  border-radius: 10px;
  background-color: white;
  border-style: solid;
  border-color: white;
}
.main_find_feed_write_picture {
  margin: auto;
  margin-left: 5px;
  margin-right: 7px;
}
.main_find_feed_write_write {
  width: 100%;
}
.main_find_feed_background{
  background-color: white;
  margin-bottom: 24px;
  padding: 10px;
  border-radius: 10px;

}
</style>