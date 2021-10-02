<template>
    <v-app>
        <v-main>
            <ToolBar :username="username"></ToolBar>
            <HomeAppBar></HomeAppBar>
            <HomeBanner></HomeBanner>

            <v-card outlined class="text-h4">Top Songs</v-card>

            <Carousel :songs="songs"></Carousel>
        </v-main>
    </v-app>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import HomeBanner from '../components/HomeBanner.vue';
import Carousel from '../components/Carousel.vue';

export default {
  name: 'Home',
  components: {
    ToolBar,
    HomeAppBar,
    HomeBanner,
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
  }),
};
</script>

<style scoped>
.v-card {
    text-align: center;
}
</style>
