import Vue from 'vue';
// import Vuex from "vuex";
// import storePlugin from "./vuex/vuex_store_as_plugin";
import axios from 'axios';
import VueAxios from 'vue-axios';
import Profile from '../profile/Profile.vue';
import vuetify from '../plugins/vuetify';

// Vue.use(Vuex);
// Vue.use(storePlugin);
Vue.config.productionTip = false;
Vue.use(VueAxios, axios);

new Vue({
  vuetify,
  el: '#profile',
  components: { Profile },
});
