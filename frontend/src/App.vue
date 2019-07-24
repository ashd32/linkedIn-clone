<template>
  <div id="app">
    <Header/>
    <SignIn/>
    <SignUp/>
  </div>
</template>

<script>
import SignIn from './components/Auth/SignIn.vue'
import SignUp from './components/Auth/SignUp.vue'
import Header from './components/Base/Header.vue'

export default {
  name: 'app',
  components: {
    SignIn, Header, SignUp
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
