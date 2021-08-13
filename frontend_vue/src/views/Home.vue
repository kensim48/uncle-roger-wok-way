<template>
  <v-app id="inspire">
    <v-dialog v-model="modifyDialog" max-width="600px" persistent>
      <ModifyItem :item="selectedItem" />
    </v-dialog>
    <v-dialog v-model="checkoutDialog" max-width="600px" persistent>
      <v-card>
        <v-card-title>
          <span class="text-h5">Checkout</span>
        </v-card-title>
        <v-card-text>
          <v-container
            v-if="checkingoutItems.length > 0"
            class="grey lighten-5"
          >
            <v-row>
              <v-col>Name</v-col>
              <v-col>Price</v-col>
              <v-col>Quantity</v-col>
              <v-col>Total</v-col>
            </v-row>
            <v-row
              v-for="checkingoutItem in checkingoutItems"
              :key="checkingoutItem.id"
            >
              <v-col>{{ checkingoutItem.name }}</v-col>
              <v-col>{{ checkingoutItem.price }}</v-col>
              <v-col>{{ checkingoutItem.quantity }}</v-col>
              <v-col>{{
                checkingoutItem.price * checkingoutItem.quantity
              }}</v-col>
            </v-row>
            <v-row>
              <v-col></v-col>
              <v-col></v-col>
              <v-col>Final Total:</v-col>
              <v-col>{{ checkingoutPrice }}</v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" text @click="checkoutDialog = false">
            Close
          </v-btn>
          <v-btn color="primary" text @click="submitOrder()"> Submit </v-btn>
        </v-card-actions>
      </v-card>
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
    <v-dialog v-model="registerDialog" max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Registration</span>
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
                <v-text-field label="Email" required v-model="user.email"
                  ><v-icon slot="prepend">mdi-email</v-icon></v-text-field
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
          <v-btn color="secondary" text @click="registerDialog = false">
            Close
          </v-btn>
          <v-btn color="primary" text @click="handleRegister()"> Submit </v-btn>
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
      <v-toolbar-title v-if="loggedIn"
        >Welcome back, {{ username }}</v-toolbar-title
      >
      <v-toolbar-title v-else>Wok Way</v-toolbar-title>

      <v-spacer></v-spacer>
      <div v-if="loggedIn">
        <v-btn class="ma-2" @click="checkOutDialogActivate()">
          Checkout
          <v-icon right dark> mdi-cart </v-icon>
        </v-btn>
        <v-btn class="ma-2" color="secondary" @click="handleLogout()"
          >Logout</v-btn
        >
      </div>
      <div v-else>
        <v-btn class="ma-2" @click="registerDialog = true">Register</v-btn>
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
          <v-col v-for="item in items" :key="item.id" cols="3">
            <ItemCard
              :item="item"
              :isStaff="isStaff"
              :loggedIn="loggedIn"
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
    <v-snackbar v-model="registrationSnackbar" color="green">
      Successfully registered
    </v-snackbar>
    <v-snackbar v-model="orderSnackbar" color="green">
      Order Submitted
    </v-snackbar>
    <v-snackbar v-model="errorSnackbar" color="red">
      {{ errorMessage }}
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
    registrationSnackbar: false,
    orderSnackbar: false,
    errorSnackbar: false,
    errorMessage: "",
    loginDialog: false,
    registerDialog: false,
    modifyDialog: false,
    deleteDialog: false,
    checkoutDialog: false,
    isStaff: false,
    itemLoading: true,
    items: [],
    checkingoutItems: [],
    checkingoutPrice: 0,
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
    checkOutDialogActivate() {
      this.checkingoutItems = [];
      this.checkingoutPrice = 0;
      for (var item of this.items) {
        if (item["quantity"] != 0) {
          this.checkingoutItems.push(item);
          console.log(this.checkingoutItems);
          this.checkingoutPrice += item.price * item.quantity;
        }
      }
      this.checkoutDialog = true;
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
          this.errorMessage = error.response.data;
          this.errorSnackbar = true;
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
          this.errorMessage = error.response.data;
          this.errorSnackbar = true;
          this.itemLoading = false;
        }
      );
    },
    submitOrder() {
      this.checkoutDialog = false;
      UserService.postOrder({ data: this.checkingoutItems }).then(
        () => {
          this.orderSnackbar = true;
          for (var item of this.items) {
            item["quantity"] = 0;
          }
        },
        (error) => {
          this.content =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
          this.errorMessage = error.response.data;
          this.errorSnackbar = true;
          this.itemLoading = false;
        }
      );
    },
    handleRegister() {
      this.loading = true;
      if (this.user.username && this.user.password) {
        console.log(this.user);
        this.$store.dispatch("auth/register", this.user).then(
          () => {
            this.registerDialog = false;
            this.user = new User("", "");
            this.registrationSnackbar = true;
          },
          (error) => {
            this.loading = false;
            this.message =
              (error.response && error.response.data) ||
              error.message ||
              error.toString();
            this.errorMessage = error.response.data;
            this.errorSnackbar = true;
          }
        );
      }
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
            this.errorMessage = error.response.data;
            this.errorSnackbar = true;
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
