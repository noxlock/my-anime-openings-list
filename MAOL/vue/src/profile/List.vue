<template>
    <v-main>
        <ToolBar :user="user"></ToolBar>
        <ProfileBanner :profile="profile"></ProfileBanner>
        <SongList :user="user" :username="username" :ratings="ratings"></SongList>

    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import ProfileBanner from '../components/ProfileBanner.vue';
import SongList from '../components/SongList.vue';

export default {
  name: 'List',
  components: {
    ToolBar,
    ProfileBanner,
    SongList,
  },
  props: {
    user: {
      type: String,
    },
    username: {
      type: String,
    },
    profile: {
      type: Array,
    },
    ratings: {
      type: Array,
    },
  },
  data: () => ({
  }),
};
</script>

<style>
#add-dialogue {
    height: 100%;
    width: 500px;
    background-color: whitesmoke;
    text-align: center;
}

.v-select {
    width: 75px;
}
</style>
