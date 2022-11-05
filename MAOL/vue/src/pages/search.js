import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import Search from '../home/Search.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

new Vue({
  vuetify,
  el: '#search',
  components: { Search },
});
