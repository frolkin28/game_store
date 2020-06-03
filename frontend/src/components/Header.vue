<template>
  <div class="container header">
    <div class="header-logo">
      <img src="@/assets/logo.png" width="30" height="30" />
      <div class="logo-title">
        <h5>
          <router-link to="/">Game store</router-link>
        </h5>
      </div>
    </div>
    <div class="navbar">
      <ul>
        <li>
          <router-link to="/">Games</router-link>
        </li>
        <li>
          <a href="#">Community</a>
        </li>
        <li>
          <a href="#">About</a>
        </li>
        <li>
          <a href="#">Support</a>
        </li>
        <li>
          <div v-if="getToken">
            <div>
              {{ getUser.first_name }}
              {{ getUser.second_name }}
            </div>
            <div class="logged-in"></div>
          </div>
          <div v-else>
            <router-link to="/sign_up">Sign up</router-link>
            <router-link to="/login">Sign in</router-link>
          </div>
        </li>
      </ul>
    </div>
    <div class="logout" v-if="getToken">
      <button type="button" class="btn btn-dark btn-sm" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
  
  computed: {
    ...mapGetters(['getUser', 'getToken'])
  },
  methods: {
    ...mapMutations(['updateUser', 'updateToken']),
    logout() {
      localStorage.removeItem("user");
      localStorage.removeItem("token");
      this.updateUser(null);
      this.updateToken(null);
      // this.$router.push("/");
    }
  }
};
</script>

<style scope>
.header {
  padding: 5px 0px;
  display: flex;
  color: #ffffff;
}

.header-logo {
  flex: 2;
  display: flex;
  align-items: center;
}

.logo-title {
  flex: 4;
  padding-top: 10px;
}

.logo-title h5 a {
  text-decoration: none;
  color: #ffffff;
}

.navbar {
  flex: 8;
}

.navbar ul {
  width: 100%;
  margin-top: 9px;
  padding: 0;
  list-style: none;
  display: flex;
}

.navbar li {
  flex: 1;
}

.navbar li:nth-last-of-type(1) {
  flex: 8;
  display: flex;
  justify-content: flex-end;
}

.navbar a {
  color: #ffffff;
  text-decoration: none;
  font-size: 16px;
  padding: 0px 10px;
}

.logout {
  flex: 0.8;
  display: flex;
  align-items: center;
}

.logout button {
  flex: 1;
  width: 30px;
  height: 30px;
}
</style>