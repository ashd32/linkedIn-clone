<template>
  <div>
    <UserItem v-for="user in users" :key="user.id" />
  </div>
</template>

<script>
import UserItem from "@/components/User/UserItem";
export default {
  data() {
    return {
      users: []
    };
  },
  mounted() {
    fetch("http://localhost:8000/api/users")
      .then(response => response.json())
      .then(json => {
        this.users = json;
      });
  }
};
</script>

<style>
</style>
