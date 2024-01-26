<template>
    <v-main>
        <ToolBar :user="user"></ToolBar>
        <HomeAppBar></HomeAppBar>

        <v-card>
            <h1> Search Results for {{query}}</h1>
        </v-card>
        <v-data-table
        :headers="[
            {'value': 'cover'},
            {'text': 'Name', 'value': 'english_name'},
            // {'value': 'actions', 'sortable': false},
        ]"
        hide-default-footer
        :items="anime"
        :items-per-page="10"
        :search="search"
        class="elevation-1"
        >
            <template v-slot:top>
                <v-card class="table-headers" flat>
                    <v-spacer></v-spacer>
                    <h2>Anime</h2>
                </v-card>
            </template>

            <!-- Show img for cover instead of url -->
            <template v-slot:item.cover="{ item }">
                <a :href="`/anime/${item.pk}`">
                    <v-img
                    contain
                    :aspect-ratio="16/9"
                    :height="100"
                    :src="item.cover">
                    </v-img>
                </a>
            </template>

            <template v-slot:item.english_name="{ item }">
                <a :href="`/anime/${item.pk}`">
                    {{ item.english_name }}
                </a>
            </template>
        </v-data-table>

        <v-card class="table-headers">
            <h2>Songs</h2>
        </v-card>
        <SongList
            :username=null :user="user" :list="list" :ratings="songs" :headers="[
            {'value': 'anime__cover'},
            {'text': 'Anime', 'value': 'anime__english_name'},
            {'text': 'Type', 'value': 'song_type'},
            {'text': 'Number', 'value': 'number'},
            {'text': 'Song Name', 'value': 'name'},
            {'value': 'actions', 'sortable': false},
        ]"></SongList>
    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import SongList from '../components/SongList.vue';

export default {
  name: 'Search',
  components: {
    ToolBar,
    HomeAppBar,
    SongList,
  },
  props: {
    anime: {
      type: Array,
    },
    songs: {
      type: Array,
    },
    user: {
      type: String,
    },
    list: {
      type: Number,
    },
    query: {
      type: String,
    },
  },
  data: () => ({
    search: '',
    searchClosed: true,
    selected: null,
    rating: '',
    snack: '',
    snackText: '',
    snackColour: '',
  }),
  methods: {
    addToList(song) {
      this.$http.post('/api/ratings/', {
        song,
        rating: this.rating,
        parent_list: this.list,
      }).then((res) => {
        if (res.status === 201) {
          this.snack = true;
          this.snackColour = 'success';
          this.snackText = 'Song added successfully!';
        } else {
          this.snack = true;
          this.snackColour = 'error';
          this.snackText = 'This song is already in your list!';
        }
      }).catch(() => {
        this.snack = true;
        this.snackColour = 'error';
        this.snackText = 'An unknown error has occurred';
      });
    },
  },
};
</script>

<style>
.v-card {
text-align: center;
}

v-col {
color: white;
}

.table-headers {
    text-align: left;
    padding-left: 4em;
}
</style>
