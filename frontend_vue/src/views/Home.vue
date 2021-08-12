<template>
  <v-app id="inspire">
    <v-dialog v-model="loginDialog" max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">User Login</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="Username" required
                  ><v-icon slot="prepend">mdi-account</v-icon></v-text-field
                >
              </v-col>
              <v-col cols="12">
                <v-text-field label="Password" type="password" required
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
          <v-btn color="primary" text @click="loginDialog = false">
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-app-bar app color="primary">
      <v-toolbar-title>Wok Way</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn class="ma-2"> Register </v-btn>
      <v-btn class="ma-2" color="secondary" @click="loginDialog = true">
        Login
      </v-btn>
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
          <v-col v-for="n in 24" :key="n" cols="4">
            <ItemCard :item="item" />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import ItemCard from "../components/ItemCard.vue";
export default {
  components: {
    ItemCard,
  },
  data: () => ({
    loginDialog: false,
    item: {
      name: "hello",
      price: 4,
      quantity: 0,
    },
  }),
};
</script>
