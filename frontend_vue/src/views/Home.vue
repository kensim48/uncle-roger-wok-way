<template>
  <v-app id="inspire">
    <v-dialog v-model="modifyDialog" max-width="600px" persistent>
      <ModifyItem :item="selectedItem" />
    </v-dialog>
    <v-dialog v-model="deleteDialog" max-width="600px" persistent>
      <v-card>
        <v-card-title>
          <span class="text-h5">Delete item</span>
        </v-card-title>
        <v-card-text>
          Are you sure you want to delete {{ selectedItem.name }}?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" text @click="closeDeleteDialog()">
            No
          </v-btn>
          <v-btn color="primary" text @click="submitDeleteItem()"> Yes </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
      <v-toolbar-title v-if="isStaff"
        >Welcome back, {{ username }}</v-toolbar-title
      >
      <v-toolbar-title v-else>Wok Way</v-toolbar-title>

      <v-spacer></v-spacer>
      <div v-if="isStaff">
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
          <v-col cols="10">
            <div>Top Products</div>
          </v-col>
          <v-col cols="2" v-if="isStaff">
            <v-btn class="ma-2" color="primary" @click="modifyDialog = true"
              >New Item</v-btn
            >
          </v-col>
        </v-row>
        <v-row v-if="itemLoading">
          <v-col align="center" justify="center">
            <v-progress-circular
              :size="200"
              :width="15"
              color="primary"
              indeterminate
            ></v-progress-circular>
          </v-col>
        </v-row>
        <v-row v-else>
          <v-col v-for="item in items" :key="item.id" cols="4">
            <ItemCard
              :item="item"
              :isStaff="isStaff"
              :selectedItem="selectedItem"
              :modifyDialog="modifyDialog"
            />
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
import ModifyItem from "../components/ModifyItem.vue";
import User from "../models/user";
import UserService from "../services/user.service";
import { EventBus } from "@/event-bus";

export default {
  components: {
    ItemCard,
    ModifyItem,
  },
  data: () => ({
    user: new User("", ""),
    username: "",
    loginSnackbar: false,
    logoutSnackbar: false,
    loginDialog: false,
    modifyDialog: false,
    deleteDialog: false,
    isStaff: false,
    itemLoading: true,
    items: [],
    selectedItem: {},
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
    EventBus.$on("openEdit", (data) => {
      this.modifyDialog = true;
      this.selectedItem = data;
    });
    EventBus.$on("closeEdit", () => {
      this.modifyDialog = false;
      this.selectedItem = {};
    });
    EventBus.$on("refreshList", () => {
      this.getItemList();
    });
    EventBus.$on("openDelete", (data) => {
      this.deleteDialog = true;
      this.selectedItem = data;
    });
  },
  methods: {
    closeDeleteDialog() {
      this.deleteDialog = false;
      this.selectedItem = {};
    },
    submitDeleteItem() {
      UserService.deleteItemModify(this.selectedItem).then(
        () => {
          this.closeDeleteDialog();
          EventBus.$emit("refreshList");
        },
        (error) => {
          this.content =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
        }
      );
    },
    getItemList() {
      this.itemLoading = true;
      UserService.getItemList().then(
        (response) => {
          for (var item of response.data.data) {
            item["quantity"] = 0;
          }
          this.items = response.data.data;
          this.itemLoading = false;
        },
        (error) => {
          this.content =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
          this.itemLoading = false;
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
      this.loading = true;
      this.$store.dispatch("auth/logout").then(
        () => {
          this.logoutSnackbar = true;
          this.isStaff = false;
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
          this.isStaff = response.data.is_staff;
        },
        () => {
          this.handleLogout();
        }
      );
    },
  },
};
</script>
