<template>
  <div>
    
    
    <textarea v-model="message"></textarea>
    <button v-if="!message">제출</button>
    <button v-if="message">글을 입력해야 버튼이 보입니다.</button>
  </div>
</template>

<script>
export default {
  name:'test2',
  data() {
    return{
      message:''
    }
  }

}
</script>

<style>

</style>