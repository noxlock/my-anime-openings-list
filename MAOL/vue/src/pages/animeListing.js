import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import Listing from '../anime/Listing.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

new Vue({
  vuetify,
  el: '#list',
  components: { Listing },
});
