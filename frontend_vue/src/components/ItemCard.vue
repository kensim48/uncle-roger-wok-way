<template>
  <v-card>
    <v-img
      class="white--text align-end"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="200px"
    >
    </v-img>
    <v-card-title>
      {{ item.name }}
    </v-card-title>
    <v-card-subtitle> ${{ item.price.toFixed(2) }} </v-card-subtitle>

    <v-card-actions>
      <div class="ml-3" v-if="item.quantity != 0">
        {{ item.quantity }} in cart
      </div>
      <v-spacer></v-spacer>
      <div v-if="item.quantity == 0">
        <v-btn fab dark small color="primary">
          <v-icon>mdi-cart-plus</v-icon>
        </v-btn>
      </div>
      <div v-else>
        <v-btn icon>
          <v-icon>mdi-minus-circle-outline</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    item: Object,
  },
};
</script>
