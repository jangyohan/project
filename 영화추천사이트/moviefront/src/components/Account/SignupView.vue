<template>
  <div class="container">
    
    <b-form-group
      id="input-group-1"
      label="Id"
      label-for="input-1"
      description="ID를 입력해주세요"
    >
      <b-form-input
        id="input-1"
        v-model="signupData.username"
        type="text"
        required
        placeholder="Enter ID"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label="Password:" label-for="input-2">
      <b-form-input
        id="input-2"
        v-model="signupData.password1"
        type="password"
        required
        placeholder="Enter password1"
      ></b-form-input>
    </b-form-group>

  <b-form-group id="input-group-3" label="Password Confirm:" label-for="input-3">
      <b-form-input
      id="input-3"
      v-model="signupData.password2"
      type="password"
      required
      placeholder="Enter password2"
      ></b-form-input>
  </b-form-group>


    <b-button @click="$emit('signup',signupData)" variant="primary">Submit</b-button>

   
    
  </div>
</template>

<script>
  export default {
    name: 'SignupView',
    data() {
      return {
        signupData: {
            username: null,
            password1: null,
            password2: null,
        },
        show: true
      }
    },
    methods: {

    }
  }
</script>