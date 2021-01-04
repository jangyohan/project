<template>
  <div>
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex flex-row align-items-center">
        <div class="avatar mr-3">
          <img
            class="avatar-img"
            :src="feed.userimage"
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
          <a class="dropdown-item" href="#" @click="feedDelete(feed.meetNo)">삭제</a>
        </li>
      </ul>
    </div>
    <div :id="feed.meetNo" style="width:100%;height:150px;"></div>
    <div style="width: 100%; text-align: center;">{{ feed.map }}</div>
    <div class="">
      <p class>{{ feed.content }}</p>
      
      <p>모임 시간:{{ feed.meetdate }}</p>
      <a :href= feed.kakao>오픈 채팅</a>
      
    </div>
    <div class="d-flex justify-content-between">
      
    </div>
  </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=b1df6594e5b411359a1d4aa0fbe45012&libraries=services"></script>
<script>
import axios from 'axios'

export default {
  name: "FindgalleryFeed",
  components: {
  },
  props: {
    feed: Object,
  },
  data() {
    return {
      nowUserUid: localStorage.getItem("nowUid")
      }
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
    moveUserpage(uid_fk) {
      console.log(uid_fk);
      localStorage.setItem("moveUserpage", uid_fk);
      if (
        localStorage.getItem("moveUserpage") == localStorage.getItem("nowUid")
      ) {
        window.location.href = "/mypage";
      } else {
        window.location.href = "/userpage";
      }
    },
    feedDelete(meetNo) {
      axios
        .post(`https://i3b305.p.ssafy.io/muscleloss/api/meet/meetDelete/${meetNo}`)
        .then(({ data }) => {
          console.log(data)
          window.location.href = "/findgallery";
        })
        .catch((err) => {
          cosole.log(err)
        });
    }
  },
  mounted() {
    var mapContainer = document.getElementById(this.feed.meetNo), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };  

    // 지도를 생성합니다    
    var map = new kakao.maps.Map(mapContainer, mapOption); 

    // 주소-좌표 변환 객체를 생성합니다
    var geocoder = new kakao.maps.services.Geocoder();

    // 주소로 좌표를 검색합니다
    geocoder.addressSearch(this.feed.map, (result, status) => {

        // 정상적으로 검색이 완료됐으면 
        if (status === kakao.maps.services.Status.OK) {

            var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

            // 결과값으로 받은 위치를 마커로 표시합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: coords
            });

            // 인포윈도우로 장소에 대한 설명을 표시합니다
            var infowindow = new kakao.maps.InfoWindow({
                content: '<div style="width:150px;text-align:center;padding:6px 0;">point</div>'
            });
            infowindow.open(map, marker);

            // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
            map.setCenter(coords);
        } 
    });    
  }
};
</script>

<style>
.avatar-img{
  text-indent:0 !important;
}
</style>