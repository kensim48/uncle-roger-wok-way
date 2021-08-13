<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Edit item</span>
    </v-card-title>
    <v-card-text>
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-text-field
              label="Name"
              required
              v-model="item.name"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              label="Price"
              required
              v-model="item.price"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              label="Serial ID"
              required
              v-model="item.serial_id"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="secondary" text @click="emitCloseEditEvent()">
        Close
      </v-btn>
      <v-btn color="primary" text> Submit </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { EventBus } from "@/event-bus";

export default {
  props: {
    item: Object,
  },
  methods: {
    emitCloseEditEvent() {
      EventBus.$emit("closeEdit");
    },
  },
};
</script>
