import Vue from 'vue';

import Song from '../song/Song.vue';
import vuetify from '../plugins/vuetify';

Vue.config.productionTip = false;

new Vue({
  vuetify,
  el: '#song',
  components: { Song },
});
