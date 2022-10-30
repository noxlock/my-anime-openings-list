<template>
    <v-main>
        <ToolBar :user="username"></ToolBar>
        <HomeAppBar></HomeAppBar> <!--MAYBE-->

        <!-- Banner and profile picture -->
        <ProfileBanner :profile="profile" :username="username"></ProfileBanner>
        <v-card outlined class="text-h3"> {{username}}'s Top Songs </v-card>
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

.left-box {
    float: left;
    justify-content: center;
    align-items: center;
    padding-top: 50px;
    padding-left: 100px;
    background-color: #aeb1b6;
}
.v-btn {
    padding-block: 50px;
}

</style>
