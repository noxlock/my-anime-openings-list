<template>
    <v-app>
        <v-main>
            <ToolBar></ToolBar>
            <HomeBanner></HomeBanner>

            <v-card style="text-align: center;" class="text-h4">Top Songs</v-card>

            <Carousel :songs="songs"></Carousel>
        </v-main>
    </v-app>
</template>

<script>
import ToolBar from '../components/ToolBar.vue'
import Carousel from '../components/Carousel.vue'
import HomeBanner from '../components/HomeBanner.vue'


export default {
  name: 'Home',
    components: {
        ToolBar,
        Carousel,
        HomeBanner
    },
    props: {
        songs: {
            type: Array
        }
     },

  data: () => ({
  }),
};
</script>
