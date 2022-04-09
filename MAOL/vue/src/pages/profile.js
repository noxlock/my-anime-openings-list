import Vue from 'vue';
// import Vuex from "vuex";
// import storePlugin from "./vuex/vuex_store_as_plugin";
import Profile from '../profile/Profile.vue';
import vuetify from '../plugins/vuetify';

// Vue.use(Vuex);
// Vue.use(storePlugin);
Vue.config.productionTip = false;

new Vue({
  vuetify,
  el: '#profile',
  components: { Profile },
});
