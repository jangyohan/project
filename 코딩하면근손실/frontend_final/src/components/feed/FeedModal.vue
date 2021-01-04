<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal_header">
            <div class="modal_header_text">게시물 만들기</div>
          </div>
          <div class="modal_close">
            <span class="modal_close_button" style="color:rgb(23, 196, 197)">
              <i class="fas fa-times-circle fa-2x" @click="$emit('close')"></i>
            </span>
          </div>

          <div class="modal-body">
            <div class="modal-body-profile">
              <img
                class="modal_avatar_img"
                :src="userData.avatarImage"
                alt="avatar"
              />
              {{ userData.Uid }}
            </div>
            <div v-if="!image"></div>
            <div v-else>
              <img
                id="feedImage"
                class="avatar-img d-block"
                :src="image"
                alt="avatar"
                style="cursor: default; width:10%; height:10%;"
              />
            </div>
            <textarea
              class="modal-body-write"
              id="show-modal"
              cols="30"
              rows="6"
              placeholder="Content를 작성해주세요."
              v-model="feedContent"
            ></textarea>
            
            
          </div>

          <div class="modal_footer_write">
            <transition-group name="fade" tag="div" class="modal_hash_group">
              <div
                class="modal_hash_group_list"
                v-for="(hash, index) in hashList"
                :key="`hash-${index}`"
              >
                <div @click="delWriteHashItem(index)" class="modal_hash_close">
                  <i class="fas fa-times"></i>
                </div>
                {{ hash }}
              </div>
            </transition-group>
            
            <div class="modal_picture_tag">
              <div class="modal_picture_icon">
                <input
                  style="display: none"
                  ref="feedImageUpload"
                  type="file"
                  accept="image/jpeg,image/gif,image/png"
                  @change="onFileChange"
                  enctype="multipart/form-data"
                />
                <button
                  class="modal_tag_icon_hashtag"
                  @click="$refs.feedImageUpload.click()"
                >
                  <i class="fas fa-photo-video fa-2x"></i>
                </button>
              </div>
              <div class="modal_tag_icon">
                <button class="modal_tag_icon_hashtag">
                  <i
                    class="fas fa-hashtag fa-2x"
                    @click="showHashtag = true"
                  ></i>
                </button>
              </div>
              <HashtagModal @on-hashtag="onHashtag" v-if="showHashtag" @close="showHashtag=false" />
            </div>
            <button
              class="modal_footer_wirte_button"
              v-if="feedContent"
              @click="Submit"
            >
              게시
            </button>
            <button
              class="modal_footer_wirte_button_nothing"
              v-if="!feedContent"
              @click="Submit"
            >
              게시
            </button>
            
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import axios from "axios";
import HashtagModal from "@/components/feed/HashtagModal.vue";

export default {
  name: "FeedModal",
  components: {
    HashtagModal,
  },
  data() {
    return {
      feedTitle: [],
      feedContent: null,
      imageUrl: null,
      // imagePreview: "",
      item: {},
      showHashtag: false,
      hashList: [],
      image: "",
      message: "",
      feedImage: {},
      responseimage: null,
    };
  },
  props: {
    userData: Object,
  },
  methods: {
    //
    //여기서부터는 지우지 말아주세요.
    //
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      console.log(files[0]);
      this.feedImage = files[0];
      // console.log(this.feedImage);
      // console.log(this.feedImage.name);
      // console.log(this.feedImage.lastModifiedDate);
      // console.log(this.feedImage.size);
      // console.log(this.feedImage.type);
      // console.log(this.feedImage.webkitRelativePath);
      var isImageOk = true;
      isImageOk = this.chk_file_type(files[0]);
      if (isImageOk == true) {
        this.createImage(files[0]);
      } else {
        window.location.href = "/main";
      }
    },
    chk_file_type(obj) {
      // console.log("obj : " + obj);
      // console.log(/^image\/\w+/.test(obj.type));
      // console.log(!/^image\/\w+/.test(obj.type));
      if (/^image\/\w+/.test(obj.type)) {
        alert("이미지 파일 등록 완료");
        return true;
      } else {
        alert("이미지 파일만 등록이 가능합니다");
        return false;
      }
    },
    createImage(file) {
      // var image = new Image();
      var reader = new FileReader();
      var imgurl = "";
      reader.onload = (e) => {
        this.image = e.target.result;
        // console.log("this.image : " + this.image);
        // console.log("e.target.result : " + e.target.result);
        imgurl = "" + e.target.result;
      };
      reader.readAsDataURL(file);
      console.log("imgurl : " + imgurl);
      console.log("file : " + file);

      var formData = new FormData();
      formData.append("image", file);
      for (let key of formData.entries()) {
        console.log(`${key}`);
      }
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/file/fileUpload", formData)
        .then((res) => {
          console.log("fileupload 결과 res : " + res.data);
          console.log("fileupload 결과 res : " + JSON.stringify(res));
        })
        .catch((error) => {
          console.log(error.response);
          alert("사진 변경 시 에러가 발생했습니다.");
        });
    },
    //
    //여기까지는 지우지 말아주세요. 위에까지가 이미지 선택하면 잘 되는지 확인하는 함수. 아래가 이미지 저장, 반환 함수.

    onHashtag(data) {
      this.hashList = data
    },
    Submit() {
      for(var step in this.hashList){
        this.feedTitle = this.feedTitle + (this.hashList[step] + ';')
      }
      console.log(this.feedImage);
      var feedfile = this.feedImage;
      var reader = new FileReader();
      reader.readAsDataURL(feedfile);
      console.log("file : " + feedfile);

      var formData = new FormData();
      formData.append("image", feedfile);
      for (let key of formData.entries()) {
        console.log(`${key}`);
      }
      //Image 지정된 경로에 저장, 저장경로 반환.
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/file/feedimgsave", formData)
        .then((res) => {
          // console.log("profileimgsave 결과 res : " + res.data);
          // console.log("profileimgsave 결과 res : " + JSON.stringify(res));
          this.responseimage = res.data;
          console.log("경로 저장 후 res.data : " + this.responseimage);
          if (
            this.feedTitle == null ||
            this.feedContent == null ||
            this.feedTitle == "" ||
            this.feedContent == ""
          ) {
            alert("글의 Title과 Content는 반드시 작성하셔야 합니다.");
          } else {
            if (this.responseimage != null) {
              axios
                .post(
                  "https://i3b305.p.ssafy.io/muscleloss/api/feed/feedregister",
                  {
                    uid_fk: localStorage.getItem("nowUid"),
                    userimage: localStorage.getItem("avatarImageSrc"),
                    title: this.feedTitle,
                    content: this.feedContent,
                    fileName: this.responseimage,
                    imgtype: this.feedImage.type,
                  }
                )
                .then(({ data }) => {
                  let msg = "image DB저장 실패.";
                  if (data != null) {
                    msg = "image DB저장 완료.";
                    console.log("DB저장 후 data : " + data);
                  }
                  alert(msg);
                  window.location.href = "/main";
                })
                .catch(() => {
                  alert("image DB저장 시 에러가 발생했습니다.");
                  window.location.href = "/main";
                });
            }
          }
        })
        .catch((error) => {
          console.log(error.response);
          alert("사진 업로드 시 에러가 발생했습니다.");
        });
    },
    delWriteHashItem(index) {
      this.hashList.splice(index, 1);
    },
  },
};
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  position: relative;
  width: 90vw;
  height: 488px;
  margin: 0px auto;

  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}
@media (min-width: 500px) {
  .modal-container {
    width: 500px;
  }
}

.modal-header h3 {
  margin-top: 0;
  color: black;
  text-align: center;
}
.modal_header {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  align-content: center;
  padding: 1rem 1rem;
  border-bottom: 2px solid rgb(23, 196, 197);
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background-color: rgb(23, 196, 197);
  color: white;
}
.modal_header_text {
  justify-content: center;
}
.modal-body {
  /* margin: 10px 0; */
  height: 280px;
  width: 100%;
}
.modal-body-write {
  width: 100%;
  border-color: white;
  outline: none;
}
.modal_avatar_img {
  height: 36px;
  width: 36px;
}
.modal_close {
  position: absolute;
  top: 15px;
  right: 15px;
}
.modal_close_button {
  font-size: 15px;
  color: white !important;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
.modal-body-profile {
  height: 50px;
  width: 100%;
}
.modal_picture_tag {
  display: flex;
  margin-bottom:15px;
  width:100%;
}
.modal_picture_icon {
  padding-top: 5px;
  text-align: center;
  width: 50%;
}
.modal_tag_icon {
  padding-top: 5px;
  text-align: center;
  display: inline-block;
  width: 50%;
}
.modal_tag_icon_hashtag {
  background: none;
  border: none;
}
.modal_footer_write {
  position: absolute;
  bottom: 0;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  
  padding: 0.5rem;
  border-bottom-right-radius: calc(0.3rem - 1px);
  border-bottom-left-radius: calc(0.3rem - 1px);
  padding-right: 14px;
}
.modal_footer_wirte_button {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  color: white;
  background-color: rgb(23, 196, 197);
  border-color: rgb(23, 196, 197);
  border: none;
  padding: 5px 0px 5px 0px;
}
.modal_footer_wirte_button_nothing {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  color: white;
  background-color: grey;
  border-color: grey;
  border: none;
  padding: 5px 0px 5px 0px;
}
.modal-container::-webkit-scrollbar {
  width: 10px;
}
/* 스크롤바의 width */
::-webkit-scrollbar-track {
  background-color: transparent;
}
/* 스크롤바의 전체 배경색 */
::-webkit-scrollbar-thumb {
  background: silver;
}
/* 스크롤바 색 */
::-webkit-scrollbar-button {
  display: none;
}
/* 스크롤바 버튼 */

.modal_footer_wirte_button:focus {
  outline: none;
}

.modal_hash_group_list {
  display: inline-block;
  margin-right: 5px;

  margin-left: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
  color: white;
  background-color: rgb(23, 196, 197);
  padding-left: 10px;
  padding-right: 10px;
}
.modal_hash_group{
  margin-top:30px;
}
</style>
