<template>
    <v-main>
        <ToolBar :user="username"></ToolBar>
        <HomeAppBar></HomeAppBar> <!--MAYBE-->

        <!-- Banner and profile picture -->
        <ProfileBanner :profile="profile"></ProfileBanner>

        <v-card outlined class="text-h3"> {{username}}'s Top Songs </v-card>

        <!-- <Carousel :songs="recent"></Carousel> -->
        <Carousel :songs="top"></Carousel>
    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import ProfileBanner from '../components/ProfileBanner.vue';
import Carousel from '../components/Carousel.vue';

export default {
  name: 'Profile',
  components: {
    ToolBar,
    HomeAppBar,
    ProfileBanner,
    Carousel,
  },
  props: {
    profile: {
      type: Array,
    },
    username: {
      type: String,
    },
    // recent: {
    //   type: Array,
    // },
    top: {
      type: Array,
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
