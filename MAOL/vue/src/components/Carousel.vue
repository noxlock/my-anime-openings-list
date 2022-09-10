<template>
    <v-sheet
    class="mx-auto"
    elevation="8"
    max-width="100%"
    >
        <v-slide-group
        v-model="selected"
        class="pa-4"
        show-arrows
        >
            <v-slide-item
            v-for="song in songs"
            :key="song.pk"
            v-slot="{ active, toggle }"
            >
                <v-card
                :color="active ? 'primary' : 'grey lighten-1'"
                class="ma-4"
                height="200"
                width="134"
                @click="toggle"
                >
                    <v-row
                    class="fill-height"
                    align="center"
                    justify="center"
                    >
                        <v-img :src="song.anime__cover"></v-img>
                    </v-row>
                </v-card>
            </v-slide-item>
    </v-slide-group>

        <v-expand-transition>
            <v-sheet
            v-if="selected != null"
            height="400"
            tile
            >
                <v-row
                class="fill-height"
                align="center"
                justify="center"
                style='background-color: lightgray;'
                >
                    <video controls width='35%' preload='auto'>
                        <source :src=songs[selected].video_link type="video/webm">
                    </video>
                    <div style="padding-left: 15em; color:blue;">
                        <v-select
                        :items="[1,2,3,4,5,6,7,8,9,10]"
                        v-model="rating"
                        label="Rating"
                        return-object
                        filled="true"
                        ></v-select>
                        <v-btn
                        color="primary"
                        :disabled="rating === ''"
                        @click="addToList(songs[selected].pk)"
                        >
                            Add To List
                        </v-btn>
                    </div>
                </v-row>
            </v-sheet>
        </v-expand-transition>

        <v-snackbar
        v-model="snack"
        :timeout="2000"
        :color="snackColour"
        >
            {{ snackText }}

            <template v-slot:action="{ attrs }">
                <v-btn
                v-bind="attrs"
                text
                @click="snack = false"
                >
                    Close
                </v-btn>
            </template>
        </v-snackbar>
    </v-sheet>
</template>

<script>

export default {
  name: 'Carousel',
  props: {
    songs: {
      type: Array,
    },
  },
  data: () => ({
    selected: null,
    rating: '',
    snack: '',
    snackText: '',
    snackColour: '',
  }),
  methods: {
    addToList(song) {
      this.$http.post('/api/addtolist/', {
        method: 'POST',
        data: { song, rating: this.rating },
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
  mounted() {
    this.$http.defaults.xsrfHeaderName = 'X-CSRFToken';
    this.$http.defaults.xsrfCookieName = 'csrftoken';
  },
};
</script>
