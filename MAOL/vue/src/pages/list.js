import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import List from '../profile/List.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

new Vue({
  vuetify,
  el: '#list',
  components: { List },
});
