<template>
  <form class="signup" @submit.prevent="onSubmit">
    <h1>Sign Up Form</h1>
    <input type="text" placeholder="login" v-model="credential.username" />
    <input type="text" placeholder="email" v-model="credential.email" />
    <input type="text" placeholder="full name" v-model="credential.full_name" />
    <input type="date" placeholder="birthday" v-model="credential.birthday">
    <select name="countries" @change="onChangeCountry" v-model="country">
      <option
        v-for="country in countries"
        :value="country.country_id"
        :key="country.country_id"
      >{{ country.name }}</option>
    </select>
    <select name="cities" v-if="country" v-model="credential.city">
      <option
        v-for="city in cities"
        :value="city.city_id"
        :disabled="!countryIsChosen"
        :key="city.pk"
      >{{city.name}}</option>
    </select>
    <input type="password" placeholder="password" v-model="credential.password" />
    <button class="signup-btn">Sign Up</button>
  </form>
</template>

<script>
export default {
  name: "SignUp",
  data() {
    return {
      country: null,
      countries: [],
      cities: [],
      credential: {
        username: "",
        email: "",
        full_name: "",
        city: null,
        birthday: null,
        password: ""
      }
    };
  },
  mounted() {
    fetch("http://localhost:8000/api/countries/")
      .then(response => response.json())
      .then(json => {
        this.countries = json.results;
      });
  },
  computed: {
    countryIsChosen() {
      if (this.country) {
        return true;
      }
      return false;
    }
  },
  methods: {
    onChangeCountry() {
      fetch(`http://localhost:8000/api/cities/?country=${this.country}`)
        .then(response => response.json())
        .then(json => {
          this.cities = json;
        });
    },

    onSubmit() {
        console.log(this.credential)
        fetch('http://localhost:8000/api/auth/users/create', {
            method: 'POST',
            body: JSON.stringify(this.credential),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => response.json())
          .then(response => console.log("all its good"))
    }
  }
};
</script>

<style scoped>
.signup {
  width: 30%;
  margin: 30px auto;
  border: 1px solid black;
  padding: 10px;
}
.signup input {
  display: block;
  margin-top: 10px;
  width: 100%;
}
.signup select {
  margin-top: 10px;
  margin-bottom: 10px;
  width: 100%;
}

.signup-btn {
  margin: 10px;
}
</style>
