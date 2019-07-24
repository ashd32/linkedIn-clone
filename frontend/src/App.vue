<template>
  <div id="app">
    <Header />
    <SignIn />
    <SignUp />
    <Footer />
  </div>
</template>

<script>
import SignIn from "./components/Auth/SignIn.vue";
import SignUp from "./components/Auth/SignUp.vue";
import Header from "./components/Base/Header.vue";
import Footer from "./components/Base/Footer.vue";

export default {
  name: "app",
  components: {
    SignIn,
    Header,
    SignUp,
    Footer
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
