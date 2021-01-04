<template>
  <transition name="modal">
      <div class="modal-mask" @click.self="$emit('close')">
        <div class="modal-wrapper" @click.self="$emit('close')">
            <div class="modal-container">
                <div class="modal_header">
                    <div class="modal_header_text">
                      Comments
                    </div>   
                </div>
                <div class="modal_close">

                  <span class="modal_close_button" style="color:skyblue"><i class="fas fa-times-circle fa-2x" @click="$emit('close')" ></i></span>
                </div>
                <div class="drag_parent">
                <div class="drag">
                    <div class="comment-box" v-for="commentData in commentDatas" :key="commentData.rno">
                      <div class="comment-user-icon">
                        <img :src = userData.avatarImage alt="Image">
                      </div>
                      <div class="comment-article">
                        <div class="comment-article-head">
                            <div class="comment-username comment-text">{{ commentData.uid_fk }}</div>
                            <div class="comment-update-time comment-text">{{ timeForToday(commentData.moddate) }}</div>
                        </div>
                        <div class="comment-content comment-text">{{ commentData.replytext }}</div>
                      </div>
                      <div v-if="commentData.uid_fk == userData.Uid">
                        <i id="toggle" class="fas fa-ellipsis-h mt-2" data-toggle="dropdown"></i>
                        <ul class="dropdown-menu dropdown-menu-right">
                          <li>
                            <a class="dropdown-item" href="#" @click="onUpdate(commentData)">수정</a>
                          </li>
                          <li>
                            <a class="dropdown-item" href="#" @click="onDelete(commentData.rno)">삭제</a>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="modal-footer d-flex justify-content-between">
                    <div class="modal-footer-header d-flex">
                        <div class="comment-my-icon">
                        <img :src = userData.avatarImage alt="Image">
                        </div>
                        <input v-model="updateData.replytext" @input="replyData.replytext = $event.target.value" v-on:keyup.enter="onComment" class='comment-input' type="text" placeholder="Please enter a comment...">
                    </div>
                    <i class="fas fa-location-arrow" @click="onComment"></i>
                    </div>
                </div>
                </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CommentModal',
  data() {
    return {
      add: false,
      commentDatas: [],
      replyData: {
        feedNo_fk: this.feedNo,
        uid_fk: localStorage.getItem("nowUid"),
        replytext: ''
      },
      userData: {
        Uid: localStorage.getItem("nowUid"),
        avatarImage: localStorage.getItem("avatarImage"),
      },
      isUpdate: false,
      updateData: {
        rno: null,
        replytext: ''
      }, 
    }
  },
  props: {
    // commentDatas: Array,
    feedNo: Number,
  },
  watch: {
    replyData: {
      deep: true,
      handler() {
        this.checkCommentInput();
      }
    },
  },
  // updated() {
  //   axios.post(`http://localhost:9999/muscleloss/api/reply/listReply/${this.feedNo}`, { feedNo_fk: this.feedNo})
  //     .then(({ data }) => {
  //       this.commentDatas = data
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     })
  // },
  mounted() {
    axios.post(`https://i3b305.p.ssafy.io/muscleloss/api/reply/listReply/${this.feedNo}`, { feedNo_fk: this.feedNo})
      .then(({ data }) => {
        this.commentDatas = data
      })
      .catch((err) => {
        console.log(err);
      })
    
  },
  methods: {
    checkCommentInput() {
      const INPUTBTN = document.querySelector('.fa-location-arrow')
      if (this.replyData.replytext) {
        INPUTBTN.classList.add('on-comment-input')
      } else {
        INPUTBTN.classList.remove('on-comment-input')
      }
    },
    onComment() {
      if(this.isUpdate) {
        axios.put(`https://i3b305.p.ssafy.io/muscleloss/api/reply/updateReply/${this.updateData.rno}`, this.updateData)
          .then(() => {
            console.log("update")
            axios.post(`https://i3b305.p.ssafy.io/muscleloss/api/reply/listReply/${this.feedNo}`, { feedNo_fk: this.feedNo})
              .then(({ data }) => {
                this.commentDatas = data
                this.updateData.replytext = "";
              })
              .catch((err) => {
                console.log(err);
              })
          })
        .catch((err) => {
          console.log(err);
          })
        this.isUpdate = false
      }
      else {
        axios.post(`https://i3b305.p.ssafy.io/muscleloss/api/reply/insertReply/${this.replyData.uid_fk}`, this.replyData)
          .then(({ data }) => {
            console.log(data)
            axios.post(`https://i3b305.p.ssafy.io/muscleloss/api/reply/listReply/${this.feedNo}`, { feedNo_fk: this.feedNo})
              .then(({ data }) => {
                this.commentDatas = data
                this.updateData.replytext = "";
              })
              .catch((err) => {
                console.log(err);
              })
              this.updateData.replytext = "";
          })
        .catch((err) => {
          console.log(err);
          })
      }
              this.updateData.replytext = "";
    },
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
    onDelete(rno) {
      axios.post(`https://i3b305.p.ssafy.io/muscleloss/api/reply/deleteReply/${rno}`, { rno: rno })
        .then(() => {
          axios.post(`https://i3b305.p.ssafy.io/muscleloss/api/reply/listReply/${this.feedNo}`, { feedNo_fk: this.feedNo})
              .then(({ data }) => {
                this.commentDatas = data
              })
              .catch((err) => {
                console.log(err);
              })
        })
      .catch((err) => {
        console.log(err);
        })
    },
    onUpdate(data) {
      document.querySelector('.comment-input').value = data.replytext
      this.updateData.rno = data.rno
      this.isUpdate = true
    }
  },
}
</script>

<style scoped>
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.4s;

}

.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;

}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  position: relative;
  width: 90VW;
  height: 488px;
  margin: 0px auto;
  
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}
@media (min-width: 500px) {
  .modal-container {
    width: 500px;
  }
}   

.modal-head {
  width: 100%;
  height: 5%;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background-color: white;
  border-bottom: 1px solid #dee2e6;
  display: flex;
  align-items: center;
  padding: 1rem 1rem;
}

.modal-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 10%;
  padding: 0px 15px 0px 10px;
  border-top-left-radius: calc(.3rem - 1px);
  border-top-right-radius: calc(.3rem - 1px);
  border-top: 1px solid #dee2e6;
  background-color: white;
  display: flex;
  align-items: center;
}

.modal-footer-header {
  width: 80%;
}

.modal-back-btn {
  margin: 0 10px;
  width: 25px;
  height: 25px;
  cursor: pointer;
}

.modal-back-btn .fas {
  font-size: 100% !important;
  padding-left: 5%;
  color: skyblue;
}

.modal-category {
  font-weight: 600;
  color: skyblue;
  padding-bottom: 3px;
}


.drag_parent::-webkit-scrollbar { width: 10px; }
/* 스크롤바의 width */
::-webkit-scrollbar-track { background-color: transparent; }
/* 스크롤바의 전체 배경색 */
::-webkit-scrollbar-thumb { background: silver;}
/* 스크롤바 색 */
::-webkit-scrollbar-button { display: none; }
/* 스크롤바 버튼 */



.comment-user-icon img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: rgb(199, 199, 199);
}

.comment-box {
  display: flex;
  /* background-color: grey; */
  margin: 10px 0;
  padding: 0px 5px;
  height: 40px;
}

.comment-my-icon img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: rgb(199, 199, 199);
  margin-right: 20px;
}

.comment-article {
  width: 80%;
  height: 40px;
  display: flex;
  flex-direction: column;
  margin-left: 15px;
}

.comment-article-head {
  display: flex;
  height: 50%;
  margin-top: 4px;
}

.comment-content {
  height: 50%;
}

.comment-input {
  height: 30px;
  width: 100%;
  border: none;
  margin-top: 3px;
}

.comment-input:focus {
  outline: none;
}

.on-comment-input {
  color: skyblue;
}

.comment-box .comment-text {
  font-size: 90%;
  line-height: 1;
}

.comment-username {
  font-weight: 700;
  margin-right: 10px;
}

.comment-update-time {
  color: rgb(99, 99, 99);
  font-size: 70% !important;
  margin-top: 1px;
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
.modal_close {
  position: absolute;
  top:15px;
  right:15px;
}
.modal_close_button {
  font-size:15px;
}
.drag_parent {
  width: 100%;
  height: 400px;
  overflow-y: auto;
  scroll-behavior: smooth;
}
.darg{
  width: 100%;
  min-height: 100%;
}
#toggle {
  color: gray;
  cursor: pointer;
}

</style>