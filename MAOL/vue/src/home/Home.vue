<template>
        <v-main>
            <ToolBar :user="username"></ToolBar>
            <HomeAppBar></HomeAppBar>
            <BannerCarousel
            :height="'500'"
            :heading="'MAOL'"
            :subheader="'The best anime site since ' + date.toLocaleString()">
            </BannerCarousel>

            <v-card outlined class="text-h4">Top Songs</v-card>
            <Carousel :songs="songs"></Carousel>
        </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import BannerCarousel from '../components/BannerCarousel.vue';
import Carousel from '../components/Carousel.vue';

export default {
  name: 'Home',
  components: {
    ToolBar,
    HomeAppBar,
    BannerCarousel,
    Carousel,
  },
  props: {
    songs: {
      type: Array,
    },
    username: {
      type: String,
    },
  },

  data: () => ({
    date: new Date(Date.now()),
  }),
};
</script>

<style>
.v-card {
    text-align: center;
}

v-col {
    color: white;
}

</style>
