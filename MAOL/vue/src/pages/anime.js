import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';

import Anime from '../anime/Anime.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);

new Vue({
  vuetify,
  el: '#anime',
  components: { Anime },
});
