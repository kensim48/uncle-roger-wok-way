<template>
  <v-app id="inspire">
    <v-app-bar
      app
    >
      <v-toolbar-title>Wok's Way</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn class="ma-2" >
        Register
      </v-btn>
      <v-btn class="ma-2" color="primary">
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
          <v-col
            v-for="n in 24"
            :key="n"
            cols="4"
          >
            <v-card height="200"></v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    //
  }
</script>