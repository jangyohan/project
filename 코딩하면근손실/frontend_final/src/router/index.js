import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/views/user/Login.vue";
import Findpw from "@/views/user/Findpw.vue";
import Changepw from "@/views/user/Changepw.vue";
import UserList from "@/views/user/UserList.vue";
import Main from "@/views/feed/Main.vue";
import Profile from "@/views/feed/Profile.vue";
import FeedCreate from "@/views/feed/FeedCreate.vue";
import test from "@/views/feed/test.vue";
import test2 from "@/views/feed/test2.vue";
import test3 from "@/views/feed/test3.vue";
import Mypage from "@/views/feed/Mypage";
import Userpage from "@/views/feed/Userpage";
import Logout from "@/views/user/Logout";
// import { search } from "core-js/fn/symbol";
import search from "@/views/feed/Search.vue";
import Dietgallery from "@/views/function/Dietgallery.vue";
import Findgallery from "@/views/function/Findgallery.vue";
import LocationMap from "@/views/function/LocationMap.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/findpw",
    name: "Findpw",
    component: Findpw,
  },
  {
    path: "/changepw",
    name: "Changepw",
    component: Changepw,
  },
  {
    path: "/userlist",
    name: "UserList",
    component: UserList,
  },
  {
    path: "/main",
    name: "Main",
    component: Main,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    props: true,
  },
  {
    path: "/feed/create",
    name: "FeedCreate",
    component: FeedCreate,
  },
  {
    path: "/test",
    name: "test",
    component: test,
  },
  {
    path: "/test2",
    name: "test2",
    component: test2,
  },
  {
    path: "/test3",
    name: "test3",
    component: test3,
  },
  {
    path: "/mypage",
    name: "Mypage",
    component: Mypage,
  },
  {
    path: "/userpage",
    name: "userpage",
    component: Userpage,
    props: true,
  },
  {
    path: "/logout",
    name: "logout",
    component: Logout,
  },
  {
    path: "/search",
    name: "search",
    component: search,
  },
  {
    path: "/dietgallery",
    name: "dietgallery",
    component: Dietgallery,
  },
  {
    path: "/findgallery",
    name: "findgallery",
    component: Findgallery,
  },
  {
    path: "/LocationMap",
    name: "LocationMap",
    component: LocationMap,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
