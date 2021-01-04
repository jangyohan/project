<template>
  <transition name="modal">
    <div class="modal-mask" @click.self="$emit('close')">
      <div class="modal-wrapper" @click.self="$emit('close')">
        <div class="modal-container">
          <div class="modal_header">
            <div class="modal_header_text">
              Alarm
            </div>   
          </div>
          <div class="modal_close">
            <span class="modal_close_button" style="color:skyblue"><i class="fas fa-times-circle fa-2x" @click="$emit('close')" ></i></span>
          </div>
          <div class="drag_parent">
            <div class="drag">
              <div v-for="(alarm, index) in alarms" v-bind:key='index'>
                <div class="alarm-box">
                  {{ alarm.message }}<span class="alarm-update-time ml-2">{{ timeForToday(alarm.date) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AlarmModal',
  data() {
    return {
      alarms: {},
    }
  },
  props: {
    alarmData: Object, 
  },
  created() {
    axios
      .get(`https://i3b305.p.ssafy.io/muscleloss/api/alarm/listAlarm/${localStorage.getItem("nowUid")}`, { uid: localStorage.getItem("nowUid"),})
      .then(({ data }) => {
        this.alarms = data;
 
        // let msg = "데이터베이스에서 알람리스트를 가져오지 못했습니다.";
        if (this.alarms != null) {
          // msg = "데이터베이스에서 알람리스트를 가져왔습니다.";
        }
        // alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
      });
    },
  mounted() {
    axios
      .get(`https://i3b305.p.ssafy.io/muscleloss/api/alarm/listAlarm/${localStorage.getItem("nowUid")}`, { uid: localStorage.getItem("nowUid"),})
      .then(({ data }) => {
        this.alarms = data;
 
        // let msg = "데이터베이스에서 알람리스트를 가져오지 못했습니다.";
        if (this.alarms != null) {
          // msg = "데이터베이스에서 알람리스트를 가져왔습니다.";
        }
        // alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
      });
  },
  methods: {
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
  }
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

.drag_parent::-webkit-scrollbar { width: 10px; }
/* 스크롤바의 width */
::-webkit-scrollbar-track { background-color: transparent; }
/* 스크롤바의 전체 배경색 */
::-webkit-scrollbar-thumb { background: silver;}
/* 스크롤바 색 */
::-webkit-scrollbar-button { display: none; }
/* 스크롤바 버튼 */

.modal_header {
  display: flex;
  
  justify-content: center;
  align-items: flex-start;
  align-content: center;
  
  border-bottom: 1px solid #dee2e6;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
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
.alarm-box {
  /* display: flex; */
  margin: 10px 0;
  padding: 5px 5px 8px 5px;
  height: 40px;
  border-top: cadetblue solid 1px;
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
.alarm-box .alarm-text {
  font-size: 90%;
  line-height: 1;
}

.alarm-username {
  font-weight: 700;
  margin-right: 10px;
}

.alarm-update-time {
  color: rgb(99, 99, 99);
  font-size: 70% !important;
  /* margin-top: 1px; */
}
</style>