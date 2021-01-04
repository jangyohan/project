<template>
  <transition name="modal">
    <div class="modal-mask" @click.self="$emit('close')">
      <div class="modal-wrapper" @click.self="$emit('close')">
        <div class="modal-container">
          <div class="modal_header">
            <div class="modal_header_text">
              FollowList
            </div>   
          </div>
          <div class="modal_close">
            <span class="modal_close_button" style="color:skyblue"><i class="fas fa-times-circle fa-2x" @click="$emit('close')" ></i></span>
          </div>
          <div class="drag_parent">
            <div class="drag">
              <div class="comment-box mt-3 mb-0" v-for="followData in followDatas" :key="followData.id">
                user : {{ followData.uid }}       
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'FollowModal',
  data() {
    return {

    }
  },
  props: {
    followDatas: Array
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
  vertical-align: center;
}
.modal-container {
  position: relative;
  width: 90VW;
  height: 488px;
  margin: 0px auto;
  padding: 3px 3px;
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

.comment-box {
  display: flex;
  /* background-color: grey; */
  /* margin-top: 10px;
  margin: 10px 0; */
  padding: 0px 8px;
  height: 20px;
  vertical-align: center;
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
  border-bottom: 1px solid #dee2e6;
  border-top-left-radius: calc(.3rem - 1px);
  border-top-right-radius: calc(.3rem - 1px);
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