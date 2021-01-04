// import axios from 'axios';
// const SERVER_URL = 'http://127.0.0.1:8000/';

export default {
  setIsLogin(state, data) {
    state.isLogin = data
  },
  setUser(state, data) {
    state.UserInfo = data
  },
  // setUserInfo(state, data) {
  //   if (data !== false) {
  //     const config = {
  //       headers: {
  //         Authorization: `Token ${data}`
  //       },
  //     }
  //     axios.post(`${SERVER_URL}accounts/`, null, config)
  //     .then((res)=>{
  //       state.UserInfo = res.data
  //       console.log(state.UserInfo)
  //     })
  //     .catch(()=>{
  //     }); 
  //   } else {
  //     state.UserInfo = ''
  //   }
  // },
  setMailInput(state, data) {
    state.signUpInput = data
  },
  setMailCode(state, data) {
    state.mailCode = data
  },
  setMailValid(state, data) {
    state.mailValid = data
  },
  setIsLoggedIn(state, data) {
    state.isLoggedIn = data
  },
  setToken(state, data) {
    state.authToken = data
  },
  setLoginPath(state, data) {
    state.loginPath = data
  },
  setSchoolType(state, data) {
    state.schoolType = data
  },
  setSchoolName(state, data) {
    state.schoolName = data
  },
  setSchoolDetail(state, data) {
    state.schoolDetail = data
  },
  setSchoolType2(state, data) {
    state.schoolType2 = data
  },
  selectSchool(state, data) {
    state.selectedSchool = data
  },
  selectSchoolType(state, data) {
    state.selectedSchoolType = data
  },
  setMajorName(state, data) {
    state.majorName = data
  },
  setMajorType(state, data) {
    state.majorType = data
  },
  setMajorType2(state, data) {
    state.majorType2 = data
  },
  selectMajor(state, data) {
    state.selectedMajor = data
  },
  selectMajorType(state, data) {
    state.selectedMajorType = data
  },
  selectMajorType2(state, data) {
    state.selectedMajorType2 = data
  },
  setUserModalId(state, data) {
    state.UserModalId = data
  },
  setRecruitId(state, data) {
    state.recruitId = data
  },
  setUserDivide(state, data) {
    state.UserDivide = data
  },
  setCareerDetail(state, data) {
    state.careerDetail = data
  }
}