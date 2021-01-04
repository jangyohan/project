import Vue from 'vue'
import App from './App.vue'
import router from './router'

import VueCookies from 'vue-cookies'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import 'animate.css'
import 'fullpage-vue/src/fullpage.css'
import VueFullpage from 'fullpage-vue'


import VueScrollProgressBar from '@guillaumebriday/vue-scroll-progress-bar'

Vue.use(VueScrollProgressBar)

Vue.use(VueFullpage)


Vue.use(BootstrapVue)
Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
