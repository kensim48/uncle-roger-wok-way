<template>
  <div>
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
        <div v-if="loggedIn">
          <v-btn fab dark small color="highlight" @click="emitOpenEditEvent()">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn
            class="mx-2"
            fab
            dark
            small
            color="red"
            @click="emitOpenDeleteEvent()"
          >
            <v-icon>mdi-trash-can</v-icon>
          </v-btn>
        </div>
        <v-spacer></v-spacer>
        <div v-if="item.quantity == 0">
          <v-btn fab dark small color="primary" @click="item.quantity++">
            <v-icon>mdi-cart-plus</v-icon>
          </v-btn>
        </div>
        <div v-else>
          <v-btn
            class="mx-2"
            fab
            dark
            small
            color="secondary"
            @click="item.quantity--"
          >
            <v-icon>mdi-minus</v-icon>
          </v-btn>
          <v-btn fab dark small color="primary" @click="item.quantity++">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { EventBus } from "@/event-bus";

export default {
  components: {},
  data: () => ({}),
  props: {
    item: Object,
    loggedIn: Boolean,
  },
  methods: {
    emitOpenEditEvent() {
      EventBus.$emit("openEdit", this.item);
    },
    emitOpenDeleteEvent() {
      EventBus.$emit("openDelete", this.item);
    },
  },
};
</script>
