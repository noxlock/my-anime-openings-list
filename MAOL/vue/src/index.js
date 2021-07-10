import Vue from "vue/dist/vue.js";
import storePlugin from "./vuex/vuex_store_as_plugin";
import Vuex from "vuex";
import HelloWorld from "./components/HelloWorld";

Vue.use(Vuex);
Vue.use(storePlugin); 
Vue.config.productionTip = false;

new Vue({
  el: "#hello_world_a",
  components: {HelloWorld}
});