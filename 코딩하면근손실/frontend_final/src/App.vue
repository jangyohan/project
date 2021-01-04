<template>
  <div id="app">
    <div v-if="isLogged" class="nav_all col-lg-4">
      <b-navbar class="nav_toggle" toggleable="lg" type="dark">
        <b-navbar-brand href="/main">
          <img src="@/assets/img/근육3.png"  class="nav_logo" alt="">
          NoMuscleLoss
        </b-navbar-brand>
        <div class="nav_icon">
          <button class="nav_icon_bell"><span style="color:white;"><i class="nav_icon_bell fas fa-bell fa-2x" @click="showAlarm=true"></i></span></button>
          <router-link class="text-dark text-decoration-none" to="Mypage"><button class="nav_icon_user"><span style="color:white;"><i class="nav_icon_user fas fa-user fa-2x"></i></span></button></router-link>
        </div>
        <AlarmModal v-if="showAlarm" @close="showAlarm=false" />
        <Nav />
      </b-navbar> 
    </div>
    
    <router-view></router-view>
  </div>
</template>


<script>
import "./components/css/style.css";
import Nav from "@/components/feed/Nav.vue"
import AlarmModal from "@/components/feed/AlarmModal.vue"

export default {
  name: "app",
  data() {
    return {
      isLogged: false,
      showAlarm: false,
    }
  },
  methods: {
  },
  mounted() {
    this.isLogged = localStorage.getItem('nowToken')
  },
  components:{
    Nav,
    AlarmModal,
  }
};
</script>

<style>
.nav_icon {
  display:flex;
  margin-left:auto;
}
.nav_icon_bell{
  background-color: rgb(23, 196, 197);;
  border:none;
  margin-right:8px;
}
.nav_icon_user{
  background-color: rgb(23, 196, 197);;
  border:none;
}
.nav_logo{
  width:35px;
  height:35px;
  
}
</style>  