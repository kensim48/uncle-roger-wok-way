<template>
  <v-app id="inspire">
    <v-dialog v-model="loginDialog" max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Login</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="Username" required v-model="user.username"
                  ><v-icon slot="prepend">mdi-account</v-icon></v-text-field
                >
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Password"
                  type="password"
                  required
                  v-model="user.password"
                  ><v-icon slot="prepend">mdi-key</v-icon></v-text-field
                >
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" text @click="loginDialog = false">
            Close
          </v-btn>
          <v-btn color="primary" text @click="handleLogin()"> Submit </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-app-bar app color="primary">
      <v-toolbar-title v-if="loggedIn"
        >Welcome back, {{ username }}</v-toolbar-title
      >
      <v-toolbar-title v-else>Wok Way</v-toolbar-title>

      <v-spacer></v-spacer>
      <div v-if="loggedIn">
        <v-btn class="ma-2" @click="handleLogout()">Logout</v-btn>
      </div>
      <div v-else>
        <v-btn class="ma-2">Register</v-btn>
        <v-btn class="ma-2" color="secondary" @click="loginDialog = true">
          Login
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-img
          :src="require('../assets/Big_Logo.svg')"
          class="my-3"
          contain
          height="200"
        />
        <v-row>
          <v-col>
            <div>Top Products</div>
          </v-col>
        </v-row>
        <v-row>
          <v-col v-for="item in items" :key="item.id" cols="4">
            <ItemCard :item="item" />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-snackbar v-model="loginSnackbar" color="green">
      Successfully logged in
    </v-snackbar>
    <v-snackbar v-model="logoutSnackbar" color="green">
      Successfully logged out
    </v-snackbar>
  </v-app>
</template>

<script>
import ItemCard from "../components/ItemCard.vue";
import User from "../models/user";
import UserService from "../services/user.service";

export default {
  components: {
    ItemCard,
  },
  data: () => ({
    user: new User("", ""),
    username: "",
    loginSnackbar: false,
    logoutSnackbar: false,
    loginDialog: false,
    items: [],
    // item: {
    //   name: "hello",
    //   price: 4,
    //   quantity: 0,
    // },
  }),
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    this.getItemList();
    if (this.loggedIn) {
      console.log("logged in");
      this.getUserDetails();
    }
  },
  methods: {
    getItemList() {
      UserService.getItemList().then(
        (response) => {
          for (var item of response.data.data) {
            item["quantity"] = 0;
          }
          this.items = response.data.data;
        },
        (error) => {
          this.content =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
        }
      );
    },
    handleLogin() {
      this.loading = true;
      if (this.user.username && this.user.password) {
        console.log(this.user);
        this.$store.dispatch("auth/login", this.user).then(
          () => {
            this.getUserDetails();
            this.loginDialog = false;
            this.loginSnackbar = true;
            this.user = new User("", "");
          },
          (error) => {
            this.loading = false;
            this.message =
              (error.response && error.response.data) ||
              error.message ||
              error.toString();
          }
        );
      }
    },
    handleLogout() {
      console.log("tun");
      this.loading = true;
      this.$store.dispatch("auth/logout").then(
        () => {
          this.logoutSnackbar = true;
        },
        (error) => {
          this.message =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
        }
      );
    },
    getUserDetails() {
      UserService.getUserDetails().then(
        (response) => {
          this.username = response.data.username;
        },
        (error) => {
          this.content =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
        }
      );
    },
  },
};
</script>
