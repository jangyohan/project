<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'Logout',
  beforeCreate() {
    window.location.href = "/";
    localStorage.clear();
  },
}
</script>

<style>

</style>