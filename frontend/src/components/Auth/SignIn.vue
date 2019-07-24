<template>
  <form @submit.prevent="onSubmit" class="signin">
    <h1>Sign In Form</h1>
    <input type="text" id="login" placeholder="email" v-model="email" />
    <input type="password" id="password" placeholder="password" v-model="password" />
    <button class="signin-btn" :disabled="!ValidationFields">Sign In</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    onSubmit() {}
  },
  computed: {
    ValidationFields() {
      if (this.email.length !== 0 && this.password.length !== 0) {
        return true;
      }
      return false;
    }
  }
};
</script>

<style>
.signin {
  width: 30%;
  margin: 30px auto;
  border: 1px solid black;
  padding: 10px;
}

.signin input {
  display: block;
  width: 100%;
  margin-top: 10px;
}

.signin-btn {
  margin-top: 10px;
}
</style>
