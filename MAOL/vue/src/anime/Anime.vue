<template>
    <v-main>
        <ToolBar :user="username"></ToolBar>
        <HomeAppBar></HomeAppBar>
        <div id="thx">
        <Banner
        :styles="'anime-style'"
        :image="anime[0].cover"
        :height="'150'"
        :heading="anime[0].english_name"
        >
        </Banner>
        </div>

            <v-row no-gutters>
                <v-col cols="2" class="left">
                    <v-card>
                        <aside>
                            <v-img
                            :src="anime[0].cover"
                            >
                            </v-img>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                            do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                            Ut enim ad minim veniam, quis nostrud exercitation ullamco
                            laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                            irure dolor in reprehenderit in voluptate velit esse cillum
                            dolore eu fugiat nulla pariatur. Excepteur sint occaecat
                            cupidatat non proident, sunt in culpa qui officia deserunt
                            mollit anim id est laborum
                        </aside>
                    </v-card>
                </v-col>

                <v-col cols="9">
                    <SongList :ratings="songs" :headers="[
                        {'text': 'Type', 'value': 'song_type'},
                        {'text': 'Number', 'value': 'number'},
                        {'text': 'Song Name', 'value': 'name'},
                        {'value': 'actions', 'sortable': false},
                    ]"></Songlist>
                </v-col>
            </v-row>

    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import Banner from '../components/Banner.vue';
import SongList from '../components/SongList.vue';

export default {
  name: 'Anime',
  components: {
    ToolBar,
    HomeAppBar,
    Banner,
    SongList,
  },
  props: {
    anime: {
      type: Array,
    },
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

<style>
#thx {
    background-color: black;
}

.left {
    float: left;
}

#songs-container {
    padding-top: 0.5em;
}

.row {
    background-color: grey;
}

.col {
    margin-right: 60px;
}
</style>
