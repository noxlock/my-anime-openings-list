import Vue from 'vue/dist/vue.js'
import Vuex from "vuex";
import storePlugin from "./vuex/vuex_store_as_plugin";
import Test from './components/Test.vue'
import ToolBar from './components/ToolBar.vue'
import vuetify from './plugins/vuetify'

Vue.use(Vuex);
Vue.use(storePlugin);
Vue.config.productionTip = false;

new Vue({
    vuetify,
    el: "#hello_world",
    components: {Test}
});
new Vue({
    el: "#hello_world_a",
    components: {ToolBar}
  });