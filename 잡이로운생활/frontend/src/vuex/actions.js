import axios from 'axios';
const SERVER_URL = 'https://j3b104.p.ssafy.io/api/';

export default {
  setUserInfo(context) {
    if (context.state.authToken) {
      const config = {
        headers: {
          Authorization: `Token ${context.state.authToken}`
        },
      }
      axios.post(`${SERVER_URL}accounts/`, null, config)
      .then((res)=>{
        context.commit('setUser',res.data)
      })
      .catch(()=>{
      }); 
    } else {
      context.commit('setUser', '')
    }
  },
}
