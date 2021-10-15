<template>
    <v-data-table
    :search="search"
    single-expand
    multi-sort
    :headers="[
        {'value': 'song__anime__cover'},
        {'text': 'Anime', 'value': 'song__anime__english_name'},
        {'text': 'Type', 'value': 'song__song_type'},
        {'text': 'Number', 'value': 'song__number'},
        {'text': 'Rating', 'value': 'rating'},
        {'value': 'data-table-expand', 'align': 'end'}
    ]"
    :items="ratings"
    :items-per-page="-1"
    hide-default-footer
    item-key="song__pk"
    show-expand
    >
        <template v-slot:top>
            <v-toolbar elevation="0" class="d-flex justify-center">
                <v-toolbar-title class="text-h4">{{username}}'s Song List</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
        </template>

        <template v-slot:item.song__anime__cover="{ item }">
            <v-img
            contain
            :aspect-ratio="16/9"
            :height="100"
            :src="item.song__anime__cover">
            </v-img>
        </template>

        <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
                <v-card elevation="1" class="d-flex justify-center">
                    <video controls width='30%' preload='auto'>
                            <source :src="item.song__video_link" type="video/webm">
                    </video>

                    <!--<v-form action="/api/addtolist">-->
                        <v-card id="add-dialogue" class="text-h5" elevation="2">
                            <p>Add to list</p>

                            <v-select
                            :items="[1,2,3,4,5,6,7,8,9,10]"
                            v-model="rating"
                            label="Rating"
                            return-object
                            ></v-select>
                            <button v-on:click="addToList(item.song__pk)">Greet</button>
                        </v-card>
                    <!--</v-form>-->
                </v-card>
            </td>
        </template>
    </v-data-table>
</template>

<script>

export default {
  name: 'SongList',
  components: {
  },
  props: {
    username: {
      type: String,
    },
    ratings: {
      type: Array,
    },
  },
  methods: {
    addToList(song) {
      this.$http.defaults.xsrfHeaderName = 'X-CSRFToken';
      this.$http.defaults.xsrfCookieName = 'csrftoken';

      this.$http.post('/api/addtolist/', {
        method: 'POST',
        data: { song, rating: this.rating },
      });
    },
  },
  data: () => ({
    expanded: [],
    search: '',
    rating: '',
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
