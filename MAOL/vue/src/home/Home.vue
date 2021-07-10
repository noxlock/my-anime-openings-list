<template>
  <v-app>
    <v-main>
        <ToolBar></ToolBar>
        <Carousel></Carousel>
        {{ msg }}
    </v-main>
  </v-app>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import Carousel from '@/components/Carousel.vue'

export default {
  name: 'Home',
    components: {
        ToolBar,
        Carousel
    },
    props: { msg: String },

  data: () => ({
    //
  }),
};
</script>
