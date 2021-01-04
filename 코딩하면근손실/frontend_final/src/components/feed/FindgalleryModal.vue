<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container_Diet">
            <div class="modal_header">
                <div class="modal_header_text">같이 운동할 사람!</div>
            </div>
            <div class="modal_close">
                <span class="modal_close_button" style="color:rgb(23, 196, 197)">
                <i class="fas fa-times-circle fa-2x" @click="$emit('close')"></i>
                </span>
            </div>
            <div class="modal-body_Diet">
              <div class="modal-body-profile_Find">
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
                class="modal-body-write_Find"
                id="show-modal"
                cols="30"
                rows="2"
                placeholder="Content를 작성해주세요."
                v-model="infoData.content"
              ></textarea>
              <div class="Find_Map_register">
                <div style="width: 100%">
                  <input @input="infoData.map=$event.target.value" v-model="infoData.map" style="width:75%;" type="text" id="sample5_address" placeholder="주소">
                  <input style="width:25%;" type="button" @click="sample5_execDaumPostcode" value="주소 검색"><br>
                  <div id="map" style="width:100%;height:170px;margin-top:10px;display:none"></div>
                </div>
              </div>
              <div class="Findgallery_Modal_term mt-5">
                <button i class="Findgallery_Modal_term_button fas fa-running fa-2x" @click="onCategory(1)"></button>
                <button i class="Findgallery_Modal_term_button fas fa-futbol fa-2x" @click="onCategory(2)"></button>
                <button i class="Findgallery_Modal_term_button fas fa-dumbbell fa-2x" @click="onCategory(3)"></button>
                <button i class="Findgallery_Modal_term_button2 fas " @click="onCategory(4)">ETC</button>
              </div>
              
              <div>
                <span>미팅시간 : </span>
                <input class="Findgallery_time" type="datetime-local" v-on:change="checkDate">
              </div>
              <div>
                <span>오픈채팅 : </span>
                <input v-model="infoData.kakao" class="Findgallery_openchatting" type="text" placeholder="https://open.kakao.com/o/gNQXykrc">
              </div>
              
            </div>
        <div class="modal_footer_write">
            <button class="modal_footer_wirte_button" @click="onSubmit">등록</button>
        </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script src="https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script>
<script src="//dapi.kakao.com/v2/maps/sdk.js?appkey=b1df6594e5b411359a1d4aa0fbe45012&libraries=services"></script>
<script>
import axios from 'axios'

export default {
    name:"FindgalleryModal",
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
      infoData: {
        uid_fk: localStorage.getItem('nowUid'),
        userImage: localStorage.getItem('avatarImage'),
        content: '',
        category: null,
        meetdate: null,
        kakao: null,
        map: '',
      }
    };
  },
  props: {
    userData: Object,
  },
  // watch: {
  //   'infoData.map'() {
  //     console.log(this.infoData.map)
  //   }
  // },
  methods: {
    sample5_execDaumPostcode() {
      var mapContainer = document.getElementById('map'), // 지도를 표시할 div
        mapOption = {
            center: new daum.maps.LatLng(37.537187, 127.005476), // 지도의 중심좌표
            level: 5 // 지도의 확대 레벨
        };

      //지도를 미리 생성
      var map = new daum.maps.Map(mapContainer, mapOption);
      //주소-좌표 변환 객체를 생성
      var geocoder = new daum.maps.services.Geocoder();
      //마커를 미리 생성
      var marker = new daum.maps.Marker({
          position: new daum.maps.LatLng(37.537187, 127.005476),
          map: map
      });   
      new daum.Postcode({
          oncomplete: (data) => {
              var addr = data.address; // 최종 주소 변수
              this.infoData.map = addr
              // 주소 정보를 해당 필드에 넣는다.
              document.getElementById("sample5_address").value = addr;
              // 주소로 상세 정보를 검색
              geocoder.addressSearch(data.address, function(results, status) {
                  // 정상적으로 검색이 완료됐으면
                  if (status === daum.maps.services.Status.OK) {

                      var result = results[0]; //첫번째 결과의 값을 활용

                      // 해당 주소에 대한 좌표를 받아서
                      var coords = new daum.maps.LatLng(result.y, result.x);
                      // 지도를 보여준다.
                      mapContainer.style.display = "block";
                      map.relayout();
                      // 지도 중심을 변경한다.
                      map.setCenter(coords);
                      // 마커를 결과값으로 받은 위치로 옮긴다.
                      marker.setPosition(coords)
                  }
              });
          }
      }).open();
    },
    onCategory(category) {
      if (category==1) {
        this.infoData.category = 1
      }
      else if (category==2) {
        this.infoData.category = 2
      }
      else if (category==3) {
        this.infoData.category = 3
      }
      else {
        this.infoData.category = 4
      }
    },
    checkDate(event) {
      this.infoData.meetdate = event.target.value
    },
    onSubmit() {
      console.log(this.infoData)
      axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/meet/meetregister", this.infoData)
      .then(({ data }) => {
        console.log(data)
        this.$emit('close')
      })
      .catch((err) => {
        console.log(err)
      });
    },
  }
}
</script>

<style>
.modal-container_Diet {
  position: relative;
  width: 90vw;
  height: 600px;
  margin: 0px auto;

  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}
@media (min-width: 500px) {
  .modal-container_Diet {
    width: 500px;
  }
}

.modal-body_Diet {
  /* margin: 10px 0; */
  height: 500px;
  width: 100%;
  padding:16px;
}
.testvip_modal {
    width:100%;
    height:100%;
    
}
.modal-body-write_Find {
  width: 100%;
  border-color: white;
  outline: none;
}
.modal-body-profile_Find{
  height: 50px;
  width: 100%;
  margin-top:5px;
  margin-left:10px;

}
.Findgallery_FeedModal_term{
  display: flex;
  position:fixed !important ;
  z-index:5000;
  margin-top:55px;
  width:100%;
  padding-left: 0px !important;
  padding-right:0px !important;

}
/* .Findgallery_FeedModal_term_button{
  border:none;
  border-top: 2px solid white;
  border-right: 2px solid white;
  background-color: rgb(23, 196, 197);
  color: white;
  width:33.33333333333333333333%;
  padding:3px;
  margin:0px;  

}
.Findgallery_FeedModal_term_button2{
    border:none;
    border-top: 2px solid white;
    background-color: rgb(23, 196, 197);
    color: white;
    width:33.33333333333333333333%;
    padding:3px;
    margin:0px;
    font-size:23px;

} */
.Findgallery_time{
  border-color:rgb(23, 196, 197);
  border-style:solid;
  border-radius:5px;
  width:350px;
  margin-bottom:5px;
}

.Findgallery_openchatting{
  width: 350px;
  border-color:rgb(23, 196, 197);
  border-style:solid;
  border-radius:5px;
}
@media (max-width: 500px) {
  .Findgallery_time{
    width:200px;
  }
  .Findgallery_openchatting{
    width: 200px;
  }
  .Find_Map_register{
  height: 25vh;
  margin-bottom:10px;
}
}
input::placeholder {
  font-size:13px;
}
input:focus{
  outline:none;
}
.Find_Map_register{
  height: 27vh;
  margin-bottom:10px;
}
.Findgallery_Modal_term{
    display:flex;
    width:100%;
    padding-left: 0px !important;
    padding-right:0px !important;
    margin-bottom:10px;
}
.Findgallery_Modal_term_button {
    
  
    border:none;
    border-top: 2px solid white;
    border-right: 2px solid white;
    background-color: rgb(23, 196, 197);
    color: white;
    width:25%;
    padding:3px;
    margin:0px;  
}
.Findgallery_Modal_term_button2{
    border:none;
    border-top: 2px solid white;
    background-color: rgb(23, 196, 197);
    color: white;
    width:25%;
    padding:3px;
    margin:0px;
    font-size:23px;
}

.Findgallery_Modal_term_button:active {
  background-color: gray;
}
.Findgallery_Modal_term_button2:active {
  background-color: gray;
}
</style>