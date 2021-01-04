<template>
  <div>
    <div class="profile_all col-lg-4 mx-auto">
      <!-- <User :userData="userData" /> -->
      <div class="d-flex justify-content-center pt-4">
        <div class="pt-4">
          <h1 class="h3 mb-4 text-center mt-5">Profile</h1>
          <div class="d-flex justify-content-center">
            <div class="avatar avatar-xl" v-if="!image">
              <img
                id="profileChange"
                class="avatar-img d-block"
                :src="userData1.avatarImage"
                alt="avatar"
                style="cursor: default;"
              />
              <div class="file_input2 text-right">
                <label>
                  <input
                    style="display: none"
                    ref="userProfileImgChange"
                    type="file"
                    accept="image/jpeg,image/gif,image/png"
                    @change="onFileChange"
                    enctype="multipart/form-data"
                  />
                  <button
                    id="changeImage"
                    class="fas fa-exchange-alt text-warning"
                    style="color:rgb(133, 196, 197)!important;"
                    @click="$refs.userProfileImgChange.click()"
                  ></button>
                </label>
              </div>
            </div>
            <div class="avatar avatar-xl" v-else>
              <img
                id="profileChange"
                class="avatar-img d-block"
                :src="image"
                alt="avatar"
                style="cursor: default;"
              />
            </div>
          </div>
          <!-- <div class="file_input2 text-right">
            <label>
              <i
                id="changeImage"
                class="fas fa-exchange-alt text-warning"
                style="color:rgb(133, 196, 197)!important;"
              ></i>
            </label>
          </div> -->
          <div class="text-center mt-3">
            <h2 class="h5" style="margin-top:30px">{{ userData1.Uid }}</h2>
            <p class="small text-muted">{{ userData1.Email }}</p>
          </div>
        </div>
      </div>
      <div class="text-center">
        <button @click="saveImage" v-if="image" class="text-center text-warning">
          save
        </button>
        <button
          @click="removeImage"
          v-if="image"
          class="text-center text-warning"
        >
          Remove
        </button>
      </div>

      <!-- <img :src="responseimage" /> -->
      <!-- <img src="/fileupload/20200816070513_muscleloss.png" /> -->
      <div class="d-flex justify-content-center flex-wrap">
        <div class="text-center px-3 py-2">
          <p class="small text-muted mb-0">Followers</p>
          <p class="font-weight-bold mb-0">{{ countFollower }}</p>
        </div>
        <div class="text-center px-3 py-2">
          <p class="small text-muted mb-0">Following</p>
          <p class="font-weight-bold mb-0">{{ countFollowing }}</p>
        </div>
        <div class="text-center px-3 py-2">
          <p class="small text-muted mb-0">Posts</p>
          <p class="font-weight-bold mb-0">{{ countPost }}</p>
        </div>
      </div>
      <div class="form-group mt-4 bg-white">
        <label id="oneLineInput" class="text-info">Change your password</label>
        <hr class="mb-1" />
        <form id="resetPassword" action class>
          <input
            type="text"
            class="input-field mt-0 pt-0"
            placeholder="Current Password"
            v-model="CurrentPassword"
            style="font-size: 13.333px;"
            required
          />
          <input
            type="password"
            class="input-field"
            placeholder="Enter Password"
            v-model="password1"
            style="font-size: 13.333px;"
            required
          />
          <input
            type="password"
            class="input-field"
            placeholder="Password Comfirmation"
            v-model="password2"
            style="font-size: 13.333px;"
            required
          />
          <div class="d-flex flex-row-reverse">
            <button
              class="my-2"
              @click="modifyPW"
              style="border:solid 1px skyblue;border-radius: 5px;font-size: 13.333px;background-color: white;color: skyblue; padding: 5px;"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
      <div class="form-group mt-4 bg-white">
        <label id="oneLineInput" class="text-info" for="oneLine"
          >Introduction</label
        >
        <hr class="mb-1" />
        <textarea
          class="form-control border-0"
          id="oneLine"
          rows="3"
          :placeholder="userData1.oneLineIntroduction"
          v-model="Introduction"
        ></textarea>
        <div class="d-flex flex-row-reverse" style="padding: 6px 12px">
          <button
            class="my-2"
            @click="IntroductionHandler"
            style="border:solid 1px skyblue;border-radius: 5px;font-size: 13.333px;background-color: white;color: skyblue; padding: 5px;"
          >
            Submit
          </button>
        </div>
      </div>
      <div class="form-group bg-white">
        <label id="oneLineInput" class="text-info"
          >Please check your interest (MAX 3)</label
        >
        <hr class="mb-1" />
        <form>
          <input type="checkbox" id="Soccer" name="Soccer" value="Soccer" />
          <label for="Soccer">워킹, 러닝</label>
          <input
            type="checkbox"
            id="Basketball"
            name="Basketball"
            value="Basketball"
          />
          <label for="Basketball">구기운동</label>
          <input type="checkbox" id="Pilates" name="Pilates" value="Pilates" />
          <label for="Pilates">헬스&필라테스</label>
          <input type="checkbox" id="Bowling" name="Bowling" value="Bowling" />
          <label for="Bowling">격투기</label>
          <input
            type="checkbox"
            id="Mountain climbing"
            name="Mountain climbing"
            value="Mountain climbing"
          />
          <label for="Mountain climbing">아웃도어</label>
          <div class="d-flex flex-row-reverse">
            <button
              class="my-2 mr-2"
              @click="onInterest"
              style="border:solid 1px skyblue;border-radius: 5px;font-size: 13.333px;background-color: white;color: skyblue; padding: 5px;"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
      <br />
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Profile",
  components: {},
  data() {
    return {
      userData1: {
        Uid: localStorage.getItem("nowUid"),
        Email: localStorage.getItem("nowEmail"),
        avatarImage: localStorage.getItem("avatarImage"),
        followers: 567,
        followings: 567,
        posts: 67,
        oneLineIntroduction: localStorage.getItem("usercomment"),
      },
      CurrentPassword: "",
      password1: "",
      password2: "",
      Introduction: "",
      item: {},
      image: "",
      message: "",
      profileImage: {},
      responseimage: null,
      countFollower: null,
      countFollowing: null,
      countPost: null,
      feed: {},
    };
  },
  methods: {
    //
    //여기서부터는 지우지 말아주세요.
    //
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      console.log(files[0]);
      this.profileImage = files[0];
      // console.log(this.profileImage);
      // console.log(this.profileImage.name);
      // console.log(this.profileImage.lastModifiedDate);
      // console.log(this.profileImage.size);
      // console.log(this.profileImage.type);
      // console.log(this.profileImage.webkitRelativePath);
      var isImageOk = true;
      isImageOk = this.chk_file_type(files[0]);
      if (isImageOk == true) {
        this.createImage(files[0]);
      } else {
        window.location.href = "/profile";
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
    saveImage() {
      console.log(this.profileImage);
      var profilefile = this.profileImage;
      var reader = new FileReader();
      reader.readAsDataURL(profilefile);
      console.log("file : " + profilefile);

      var formData = new FormData();
      formData.append("image", profilefile);
      for (let key of formData.entries()) {
        console.log(`${key}`);
      }
      //Image 지정된 경로에 저장, 저장경로 반환.
      axios
        .post(
          "https://i3b305.p.ssafy.io/muscleloss/api/file/profileimgsave",
          formData
        )
        .then((res) => {
          // console.log("profileimgsave 결과 res : " + res.data);
          // console.log("profileimgsave 결과 res : " + JSON.stringify(res));
          this.responseimage = res.data;
          console.log("경로 저장 후 res.data : " + this.responseimage);
          if (res != null) {
            axios
              .post(
                "https://i3b305.p.ssafy.io/muscleloss/api/member/updateProfile",
                {
                  email: localStorage.getItem("nowEmail"),
                  avatarImage: this.responseimage,
                  imgtype: this.profileImage.type,
                }
              )
              .then(({ data }) => {
                //let msg = "image DB저장 실패.";
                if (data != null) {
                  //msg = "image DB저장 완료.";
                  console.log("DB저장 후 data : " + data);
                  var finallysrc =
                    "data:" + this.profileImage.type + ";base64," + data;
                  localStorage.setItem("avatarImage", finallysrc);
                }
                //alert(msg);
                window.location.href = "/profile";
              })
              .catch(() => {
                alert("image DB저장 시 에러가 발생했습니다.");
                window.location.href = "/profile";
              });
          }
        })
        .catch((error) => {
          console.log(error.response);
          alert("사진 저장 시 에러가 발생했습니다.");
        });
      //Image DB저장.
    },
    removeImage() {
      this.image = "";
    },
    //
    //여기까지는 지우지 말아주세요.

    Logout() {
      window.location.href = "/";
      localStorage.clear();
    },
    IntroductionHandler() {
      axios
        .post("https://i3b305.p.ssafy.io/muscleloss/api/member/updateComment", {
          email: localStorage.getItem("nowEmail"),
          usercomment: this.Introduction,
        })
        .then(({ data }) => {
          //let msg = "Comment 변경 실패.";
          if (data == 1) {
            //msg = "Comment 변경 완료.";
            localStorage.setItem("usercomment", this.Introduction);
          }
          //alert(msg);
          this.$router.push("/mypage")
        })
        .catch(() => {
          alert("Comment 변경 시 에러가 발생했습니다.");
          this.$router.push("/mypage")
        });
    },
    modifyPW() {
      if (this.password1 == this.password2) {
        axios
          .post("https://i3b305.p.ssafy.io/muscleloss/api/member/modifypw", {
            email: localStorage.getItem("nowEmail"),
            password: this.CurrentPassword,
          })
          .then(({ data }) => {
            let msg = "Current Password가 틀립니다. 올바르게 입력해주세요.";
            if (data == 1) {
              msg = "Current Password가 확인되었습니다. 비밀번호 변경 완료.";
            }
            alert(msg);
            if (data == 1) {
              axios
                .post("https://i3b305.p.ssafy.io/muscleloss/api/member/modifyPW", {
                  email: localStorage.getItem("nowEmail"),
                  password: this.password2,
                })
                .then(({ res }) => {
                  let msg2 = "비밀번호 변경 실패.";
                  if (res == 1) {
                    msg2 = "비밀번호 변경 완료.";
                  }
                  alert(msg2);
                })
                .catch(() => {
                  alert("비밀번호 변경 시 에러가 발생했습니다.");
                });
            }
          })
          .catch(() => {
            alert("비밀번호 변경 시 에러가 발생했습니다.");
          });
      } else {
        alert("Passwords do not match");
      }
    },
    onInterest() {
      alert("관심사가 등록되었습니다.")
      this.$router.push('/Mypage')
    }
  },
  created() {
    axios
      .post("https://i3b305.p.ssafy.io/muscleloss/api/feed/feedAllByUser", {
        uid_fk: localStorage.getItem("nowUid"),
      })
      .then(({ data }) => {
        this.feeds = data;
        this.countPost = this.feeds.length;
        // alert(data);
        // console.log(data);
        // alert(this.feeds);
        //let msg = "데이터베이스에서 피드리스트를 가져오지 못했습니다.";
        if (this.feeds != null) {
          // msg = "데이터베이스에서 피드리스트를 가져왔습니다.";
          localStorage.setItem("moveUserpage", localStorage.getItem("nowUid"));
        }
        //alert(msg);
      })
      .catch(() => {
        alert("페이지 로딩 시 에러가 발생했습니다.");
        window.location.href = "/main";
      });

    // follower 수 구하는 axios
    axios
      .get(
        `https://i3b305.p.ssafy.io/muscleloss/api/follow/follower/${localStorage.getItem(
          "nowUid"
        )}`,
        { uid: localStorage.getItem("nowUid") }
      )
      .then(({ data }) => {
        this.countFollower = data;
      })
      .catch((err) => {
        console.log(err);
      });

    // following 수 구하는 axios
    axios
      .get(
        `https://i3b305.p.ssafy.io/muscleloss/api/follow/following/${localStorage.getItem(
          "nowUid"
        )}`,
        { uid: localStorage.getItem("nowUid") }
      )
      .then(({ data }) => {
        this.countFollowing = data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
#profileChange {
  position: relative;
}
.profile_all {
  background-color: #f2f3f5;
}

.file_input2 label input {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}
.file_input2 input[type="text"] {
  vertical-align: middle;
  display: inline-block;
  width: 200px;
  height: 28px;
  line-height: 28px;
  font-size: 5px;
  border: 1px solid rgb(133, 196, 197);
}
#changeImage {
  border: solid 1px yellow;
  border-radius: 50%;
}
#resetPassword {
  padding: 6px 12px;
}
.mb-1 {
  border-color: rgb(133, 196, 197);
}
.form-control {
  resize: none;
}
</style>
