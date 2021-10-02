<template>
    <v-main>
        <ToolBar :username="user"></ToolBar>
        <v-card id='banner' style='background-color: black; width: 100%; min-height: 35%;'></v-card>
        <v-card outlined align="center">
            <h1>{{user}}'s Profile</h1>
        </v-card>
        <Carousel :songs="recentRated"></Carousel>
        <Carousel :songs="topRated"></Carousel>
    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';

export default {
  name: 'Profile',
  components: {
    ToolBar,
  },
  props: {
    user: {
      type: String,
    },
    recentRated: {
      type: Array,
    },
    topRated: {
      type: Array,
    },
  },
  data: () => ({
  }),
};
</script>
