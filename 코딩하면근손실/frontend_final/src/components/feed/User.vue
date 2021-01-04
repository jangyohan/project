<template>
  <div>
    <div class="d-flex justify-content-center">
      <div class="py-4">
        <div class="avatar avatar-xl">
          <img class="avatar-img" :src="userData.avatarImage" alt="avatar" />
        </div>
        <div class="text-center mt-3">
          <h2 class="h5">{{ userData.Uid }}</h2>
          <p class="small text-muted">{{ userData.Email }}</p>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center flex-wrap">
      <div class="text-center px-3 py-2">
        <p class="small text-muted mb-0">Followers</p>
        <p class="font-weight-bold mb-0">{{ userData.followers }}K</p>
      </div>
      <div class="text-center px-3 py-2">
        <p class="small text-muted mb-0">Following</p>
        <p class="font-weight-bold mb-0">{{ userData.followings }}K</p>
      </div>
      <div class="text-center px-3 py-2">
        <p class="small text-muted mb-0">Posts</p>
        <p class="font-weight-bold mb-0">{{ userData.posts }}</p>
      </div>
    </div>
    <!-- 한줄 소개 작성 -->
    <p class="text-muted mb-0 py-4 text-center">{{ userData.oneLineIntroduction }}</p>
    <div class="text-center">
      <button class="btn btn-link" type="button">
        <router-link :to="{ name: 'Profile', params: { userData: userData } }">View your profile</router-link>
      </button>
      <button class="btn btn-link" type="button"><router-link to="feed/create">Create Feed</router-link></button>

    </div>
  </div>
</template>

<script>
export default {
  name: "User",
  data() {
    return {};
  },
  props: {
    userData: Object,
  },
};
</script>

<style></style>
