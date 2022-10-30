import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';

import Top from '../top_songs/TopSongs.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;
Vue.use(VueAxios, axios);

new Vue({
  vuetify,
  el: '#top',
  components: { Top },
});
