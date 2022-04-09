<template>
        <v-main>
            <ToolBar :user="username"></ToolBar>
            <HomeAppBar></HomeAppBar>
            <Banner
            :styles="'home-style'"
            :image="`https://wallpaperboat.com/wp-content/uploads/2020/06/03/42361/aesthetic-anime-01.jpg`"
            :height="'500'"
            :heading="'MAOL'"
            :subheader="'The best anime site since ' + date.toLocaleString()"
            >
            </Banner>

            <v-card outlined class="text-h4">Top Songs</v-card>
            <!-- <p>{{songs[0]}}</p> -->
            <Carousel :songs="songs"></Carousel>
        </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import Banner from '../components/Banner.vue';
import Carousel from '../components/Carousel.vue';

export default {
  name: 'Home',
  components: {
    ToolBar,
    HomeAppBar,
    Banner,
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
