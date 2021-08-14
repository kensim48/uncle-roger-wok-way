import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#ffaf40",
        secondary: "#f97c15",
        accent: "#ffeb3b",
        error: "#f44336",
        warning: "#e91e63",
        info: "#03a9f4",
        success: "#8bc34a",
      },
    },
  },
});
