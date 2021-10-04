<template>
    <v-main>
        <ToolBar :username="username"></ToolBar>
        <!-- Banner and profile picture -->
        <v-card outlined align="center">
            <v-parallax
                height="300"
                dark
                :src="'/media/' + profile[0].fields.banner"
            >
                <img :src="'/media/' + profile[0].fields.avatar" width="256">
            </v-parallax>
        </v-card>
        <v-card outlined class="text-h3"> {{username}}'s Top Songs </v-card>

        <!-- <Carousel :songs="recent"></Carousel> -->
        <Carousel :songs="top"></Carousel>
    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import Carousel from '../components/Carousel.vue';

export default {
  name: 'Profile',
  components: {
    ToolBar,
    Carousel,
  },
  props: {
    profile: {
      type: Array,
    },
    username: {
      type: String,
    },
    recent: {
      type: Array,
    },
    top: {
      type: Array,
    },
  },
  data: () => ({
  }),
};
</script>

<style scoped>
#banner {
    width: 100%;
    min-height: 35%;
}

.v-card {
    text-align: center;
}

</style>
