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
        v-model="loginData.username"
        type="text"
        required
        placeholder="Enter ID"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label="Password:" label-for="input-2">
      <b-form-input
        id="input-2"
        v-model="loginData.password"
        type="password"
        required
        placeholder="Enter password"
        @keypress.enter="$emit('login', loginData)"
      ></b-form-input>
    </b-form-group>


    <b-button @click="$emit('login', loginData)" variant="primary">Submit</b-button>

    
  </div>
</template>

<script>
  export default {
    name: 'LoginView',
    data() {
      return {
        loginData: {
            username: null,
            password: null
        },
        show: true
      }
    },
    methods: {

    }
  }
</script>