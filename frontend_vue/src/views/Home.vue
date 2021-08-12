<template>
  <v-app id="inspire">
    <v-app-bar app color="primary">
      <v-toolbar-title>Wok Way</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn class="ma-2"> Register </v-btn>
      <v-btn class="ma-2" color="secondary"> Login </v-btn>
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
    item: {
      name: "hello",
      price: 4,
      quantity: 0,
    },
  }),
};
</script>
