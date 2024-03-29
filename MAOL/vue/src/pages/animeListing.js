import Vue from 'vue';

import Listing from '../anime/Listing.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;

new Vue({
  vuetify,
  el: '#list',
  components: { Listing },
});
