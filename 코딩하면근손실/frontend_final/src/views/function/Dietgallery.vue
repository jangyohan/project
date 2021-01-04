<template>
  <div class="main_Dietgallery">
    <div class="Dietgallery_term col-lg-4">
      <button class="Dietgallery_term_button" @click="today()">오늘</button>
      <button class="Dietgallery_term_button" @click="week()">일주일</button>
      <button class="Dietgallery_term_button2" @click="month()">한달</button>
    </div>

    <div class="Dietgallery_section col-12 col-lg-4 order-lg-1">
        
        <div class="Dietgallery_images">
            <img v-for="gallery in gallerys"
            :key="gallery.imageNo"
                class="testvip"
                :src="gallery.imagesrc"
                @click="showModal(gallery.imagesrc, gallery.imageNo, gallery.regdate)"
            />
          <DietgalleryModal
          v-if="showDietgalleryModal"
          @close="showDietgalleryModal = false"
          />
    
        </div>
    

      <div class="Dietgallery_Camera">
        <label>
          <input
            style="display: none"
            class="Dietgallery_take_photo"
            type="file"
            id="ex_file"
            accept="image/jpeg,image/gif,image/png"
            capture="camera"
            @change="onFileChange"
            ref="usergalleryImgChange"
            enctype="multipart/form-data"
          />
          <button
            id="galleryImageChange"
            class="Dietgallery_Camera_icon fas fa-camera-retro fa-3x"
            @click="$refs.usergalleryImgChange.click()"
          ></button>
        </label>
        <!-- <button i class="Dietgallery_Camera_icon fas fa-camera-retro fa-3x"></button> -->
        <!-- <input i class="Dietgallery_Camera_icon fas fa-camera-retro fa-3x" type="file" accept="image/*" capture="camera"> -->
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from "axios";
import DietgalleryModal from "@/components/feed/DietgalleryModal.vue";

export default {
  name: "Dietgallery",
  components: {
    DietgalleryModal,
  },
  data() {
    return {
      showDietgalleryModal: false,
      image: "",
      galleryimgsrc: null,
      galleryImage: {},
      gallerys: {},
    };
  },
  created() {
    axios
      .post(
        "https://i3b305.p.ssafy.io/muscleloss/api/gallery/galleryAllByUserToday",
        {
          uid_fk: localStorage.getItem("nowUid"),
        }
      )
      .then(({ data }) => {
        console.log(data);
        this.gallerys = data;
        let msg = "데이터베이스에서 갤러리리스트를 가져오지 못했습니다.";
        if (this.gallerys != null) {
          msg = "데이터베이스에서 갤러리리스트를 가져왔습니다.";
          localStorage.setItem(
            "UserGallerypage",
            localStorage.getItem("nowUid")
          );
        }
        console.log(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/dietgallery";
      });
  },
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      console.log(files[0]);
      this.galleryImage = files[0];
      // console.log(this.galleryImage);
      // console.log(this.galleryImage.name);
      // console.log(this.galleryImage.lastModifiedDate);
      // console.log(this.galleryImage.size);
      // console.log(this.galleryImage.type);
      // console.log(this.galleryImage.webkitRelativePath);
      var isImageOk = true;
      isImageOk = this.chk_file_type(files[0]);
      if (isImageOk == true) {
        this.createImage(files[0]);
      } else {
        window.location.href = "/dietgallery";
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
        .post(
          "https://i3b305.p.ssafy.io/muscleloss/api/gallery/gallerysave",
          formData
        )
        .then((res) => {
          console.log("galleryregister 결과 res : " + res.data);
          console.log("galleryregister 결과 res : " + JSON.stringify(res));
          this.galleryimgsrc = res.data;
          console.log("경로 저장 후 res.data : " + this.galleryimgsrc);
          if (this.galleryimgsrc != null) {
            axios
              .post(
                "https://i3b305.p.ssafy.io/muscleloss/api/gallery/galleryregister",
                {
                  uid_fk: localStorage.getItem("nowUid"),
                  imagesrc: this.galleryimgsrc,
                  imgtype: this.galleryImage.type,
                }
              )
              .then(({ data }) => {
                let msg = "gallery image DB저장 실패.";
                if (data != null) {
                  msg = "gallery image DB저장 완료.";
                  console.log("DB저장 후 data : " + data);
                }
                alert(msg);
                window.location.href = "/dietgallery";
              })
              .catch(() => {
                alert("image DB저장 시 에러가 발생했습니다.");
                window.location.href = "/dietgallery";
              });
          }
        })
        .catch((error) => {
          console.log(error.response);
          alert("사진 등록 시 에러가 발생했습니다.");
          window.location.href = "/dietgallery";
        });
    },
    showModal(src, imageNo, regdate) {
      
      sessionStorage.setItem("nowGalleryImage", src);
      sessionStorage.setItem("nowGalleryImageNo", imageNo);
      sessionStorage.setItem("nowGalleryDate", regdate);
      this.showDietgalleryModal = true;
    },
    today() {
      // 기본 페이지 로딩이 오늘 등록한 이미지만 보이는걸로 해놔서 새로고침기능으로 대체.
      window.location.href = "/dietgallery";
    },
    week() {
      // vue를 잘 몰라서 파일 날짜 정보에 따라 오늘, 일주일, 한달버튼 누를때마다 axios요청을 보내게 해놨습니다.
      axios
        .post(
          "https://i3b305.p.ssafy.io/muscleloss/api/gallery/galleryAllByUserWeek",
          {
            uid_fk: localStorage.getItem("nowUid"),
          }
        )
        .then(({ data }) => {
          console.log(data);
          this.gallerys = data;
          let msg = "데이터베이스에서 갤러리리스트를 가져오지 못했습니다.";
          if (this.gallerys != null) {
            msg = "데이터베이스에서 갤러리리스트를 가져왔습니다.";
            localStorage.setItem(
              "UserGallerypage",
              localStorage.getItem("nowUid")
            );
          }
          console.log(msg);
        })
        .catch(() => {
          alert("페이지 로딩 시 에러가 발생했습니다.");
          window.location.href = "/dietgallery";
        });
    },
    month() {
      axios
        .post(
          "https://i3b305.p.ssafy.io/muscleloss/api/gallery/galleryAllByUserMonth",
          {
            uid_fk: localStorage.getItem("nowUid"),
          }
        )
        .then(({ data }) => {
          console.log(data);
          this.gallerys = data;
          let msg = "데이터베이스에서 갤러리리스트를 가져오지 못했습니다.";
          if (this.gallerys != null) {
            msg = "데이터베이스에서 갤러리리스트를 가져왔습니다.";
            localStorage.setItem(
              "UserGallerypage",
              localStorage.getItem("nowUid")
            );
          }
          console.log(msg);
        })
        .catch(() => {
          alert("페이지 로딩 시 에러가 발생했습니다.");
          window.location.href = "/dietgallery";
        });
    },
  },
};
</script>

<style>
.Dietgallery_take_photo {
  display: none;
}

.main_Dietgallery {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
  background-color: #fff;
}
.Dietgallery_term {
  display: flex;
  position: fixed !important ;
  z-index: 5000;
  margin-top: 55px;
  width: 100%;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
/* .nav_all {
  display:flex;
  position:fixed !important;
  top:0;
  left:0;
  right:0;
  z-index: 5000;
  background-color:white;
  margin:auto;
  padding: 0 !important;
  
  

} */
.Dietgallery_section {
  margin-top: 100px;
  width: 100%;
  background-color: #f2f3f5;
  padding: 0px !important;
}

/* .Dietgallery {
  margin: 0;
  padding: 0 !important;
  padding-right: 0 !important;
  width: 100%;
  height: 600px;
  margin-top: 55px;
  background-color: #f2f3f5;
  
} */

.Dietgallery_term_button {
  border: none;
  border-top: 2px solid white;
  border-right: 2px solid white;
  background-color: rgb(23, 196, 197);
  color: white;
  width: 33.33333333333333333333%;
  padding: 0px;
  margin: 0px;
}
.Dietgallery_term_button2 {
  border: none;
  border-top: 2px solid white;

  background-color: rgb(23, 196, 197);
  color: white;
  width: 33.33333333333333333333%;
  padding: 0px;
  margin: 0px;
}
.Dietgallery_term_button:focus {
  outline: none;
}
.Dietgallery_term_button2:focus {
  outline: none;
}
.Dietgallery_images_each {
    display:flex;
    position: relative;

 
  
}
.testvip {
  position: relative;
  margin: 2.5px;
  padding:0px !important;
  width: 32%;
  
}

.Dietgallery_Camera {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  padding-bottom: 50px;
  text-align: center;
  color: white;
}

.Dietgallery_Camera_icon {
  color: rgb(23, 196, 197);
  border: none;
  background-color: transparent;
}
.Dietgallery_Camera_icon:focus {
  outline: none;
}
</style>