<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container_Diet">
          <div class="modal_header">
            <div class="modal_header_text">사진</div>
          </div>
          <div class="modal_close">
            <span class="modal_close_button" style="color:rgb(23, 196, 197)">
              <i class="fas fa-times-circle fa-2x" @click="$emit('close')"></i>
            </span>
          </div>
          <div class="modal-body_Diet">
            <img class="testvip_modal" :src="nowGalleryImage" />
            <div class="testvip_modal_date">{{ nowGalleryDate }}</div>
          </div>
          <div class="modal_footer_write">
            <button
              class="modal_footer_wirte_button"
              @click="galleryDelete(nowGalleryImageNo)"
            >
              삭제
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import axios from "axios";
export default {
  name: "DietgalleryModal",
  data() {
    return {
      nowGalleryImage: sessionStorage.getItem("nowGalleryImage"),
      nowGalleryImageNo: sessionStorage.getItem("nowGalleryImageNo"),
      nowGalleryDate:sessionStorage.getItem("nowGalleryDate")
    };
  },
  methods: {
    galleryDelete(ImageNo) {
      console.log("ImageNo : " + ImageNo);
      axios
        .post(
          `https://i3b305.p.ssafy.io/muscleloss/api/gallery/galleryDelete/${ImageNo}`
        )
        .then(({ data }) => {
          console.log(data);
          alert("Gallery Image 삭제 성공!!");
          window.location.href = "/dietgallery";
        })
        .catch((err) => {
          console.log(err);
          alert("Gallery Image 삭제 실패!!");
          window.location.href = "/dietgallery";
        });
    },
  },
};
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
  position:relative;
}
.testvip_modal {
  width: 100%;
  height: 100%;
  
}

@media (min-width: 450px) {
  .testvip_modal {
    padding: 0 10%;
  }
}
@media (min-width: 992px) {
  .testvip_modal {
    padding: 0 20%;
  }
}
.testvip_modal_date{
  padding: 5px 10px;
   background-color: rgb(23, 196, 197);
   text-align: center;
   position: absolute;
   top: 90%;
  left: 50%;
  transform: translate( -50%, -50% );
  border-radius:10px;
}

</style>