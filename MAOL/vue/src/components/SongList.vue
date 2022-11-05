<template>
    <div>
        <v-data-table
        :headers="headers"
        :items="ratings"
        :items-per-page="-1"
        hide-default-footer
        class="elevation-1"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <!-- Dialogue for playing a song -->
                    <v-dialog v-model="playDialog" max-width="700px">
                        <v-card>
                            <video ref="video" :src="videoSrc" controls width='100%' preload='auto'>
                                <source type="video/webm">
                            </video>

                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue darken-1"
                            text @click="closeDialog('playDialog')">Close
                            </v-btn>
                            <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>

                    <!-- Dialog for adding a song to your list -->
                    <v-dialog v-model="addDialog" max-width="500px">
                        <v-card>
                            <v-card-title class="text-h5 justify-center">
                                Add this song to your list?
                            </v-card-title>

                            <div class="d-flex justify-center">
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-select
                                :items="[1,2,3,4,5,6,7,8,9,10]"
                                v-model="rating"
                                label="Rating"
                                return-object
                                ></v-select>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                            </div>

                            <v-card-actions>
                                <v-spacer></v-spacer>

                                <v-btn color="blue darken-1"
                                text @click="closeDialog('addDialog')">Cancel
                                </v-btn>

                                <v-btn color="blue darken-1"
                                text @click="addToList(selected)">OK
                                </v-btn>

                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>

                    <!-- Dialog for deleting -->
                    <v-dialog v-model="deleteDialog" max-width="500px">
                        <v-card>
                            <v-card-title class="text-h5">
                                Are you sure you want to delete this item?
                            </v-card-title>

                            <v-card-actions>
                                <v-spacer></v-spacer>

                                <v-btn color="blue darken-1"
                                text @click="closeDialog('deleteDialog')">Cancel
                                </v-btn>

                                <v-btn color="blue darken-1"
                                text @click="deleteItemConfirm">OK
                                </v-btn>

                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>

            <!-- Edit Rating Value -->
            <template v-if="user == username" v-slot:item.rating="props">
                <v-edit-dialog
                :return-value.sync="props.item.rating"
                @open="openRatingDialog(props.item)"
                @close="closeDialog('ratingDialog')"
                >
                    {{ props.item.rating }}
                    <template v-slot:input>
                        <v-select
                        :items="[1,2,3,4,5,6,7,8,9,10]"
                        v-model="rating"
                        label="Rating"
                        return-object
                        ></v-select>
                        <v-btn color="blue darken-1"
                        text @click="saveRating(props.item)">OK
                        </v-btn>
                    </template>
                </v-edit-dialog>
            </template>

            <!-- Show img for cover instead of url -->
            <template v-slot:item.song__anime__cover="{ item }">
                <a :href="'../../anime/' + item.song__anime__pk">
                    <v-img
                    contain
                    :aspect-ratio="16/9"
                    :height="100"
                    :src="item.song__anime__cover">
                    </v-img>
                </a>
            </template>

            <template v-slot:item.anime__cover="{ item }">
                <a :href="'../../anime/' + item.anime__pk">
                    <v-img
                    contain
                    :aspect-ratio="16/9"
                    :height="100"
                    :src="item.anime__cover">
                    </v-img>
                </a>
            </template>

            <template v-slot:item.song__anime__english_name="{ item }">
                <a :href="'../../anime/' + item.song__anime__pk">
                    {{ item.song__anime__english_name }}
                </a>
            </template>

            <template v-slot:item.anime__english_name="{ item }">
                <a :href="'../../anime/' + item.anime__pk">
                    {{ item.anime__english_name }}
                </a>
            </template>

            <template v-slot:item.name="{ item }">
                <a :href="item.detail_link">
                    {{ item.name }}
                </a>
            </template>

            <template v-slot:item.song__name="{ item }">
                <a :href="item.song__detail_link">
                    {{ item.song__name }}
                </a>
            </template>

            <!-- Actions -->
            <template v-slot:item.actions="{ item }">
                <v-icon
                small
                class="mr-2"
                @click="playSong(item)"
                >
                    mdi-play-circle
                </v-icon>

                <v-icon
                small
                class="mr-2"
                @click="openAddDialog(item)"
                v-if="user != username"
                >
                    mdi-plus-thick
                </v-icon>

                <v-icon
                small
                @click="deleteItem(item)"
                v-if="user == username"
                >
                    mdi-delete
                </v-icon>
            </template>

        </v-data-table>

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
    </div>
</template>

<script>

export default {
  name: 'SongList',
  components: {
  },
  props: {
    user: {
      type: String,
    },
    username: {
      type: String,
      default: 'system',
    },
    ratings: {
      type: Array,
    },
    headers: {
      type: Array,
    },
  },
  data: () => ({
    snack: '',
    snackText: '',
    snackColour: '',
    deleteDialog: false,
    playDialog: false,
    addDialog: false,
    expanded: [],
    index: -1,
    rating: '',
    videoSrc: '',
    selected: null,
  }),
  watch: {
    playDialog(val) {
      if (!val) {
        this.$refs.video.pause();
      }
    },
  },
  methods: {
    addToList(song) {
      // Since the SongList can be used in either a User's
      // List, or an Anime's List, we need to check which
      // variable to use when calling our API.
      if (song.pk) {
        song = song.pk;
      } else {
        song = song.song__pk;
      }
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

    editRating(song) {
      this.$http.post('/api/editrating/', {
        method: 'POST',
        data: { song, new_rating: this.rating },
      }).then(() => {
        this.snack = true;
        this.snackColour = 'success';
        this.snackText = 'Rating updated successfully! Refresh to update.';
      }).catch(() => {
        this.snack = true;
        this.snackColour = 'error';
        this.snackText = 'An unknown error has occurred.';
      });
    },

    removeFromList(song) {
      if (song.pk) {
        song = song.pk;
      } else {
        song = song.song__pk;
      }
      this.$http.post('/api/deletefromlist/', {
        method: 'POST',
        data: { song },
      }).then(() => {
        this.ratings.splice(this.index, 1);
        this.snack = true;
        this.snackColour = 'success';
        this.snackText = 'Song deleted successfully!';
      }).catch(() => {
        this.snack = true;
        this.snackColour = 'error';
        this.snackText = 'An unknown error has occurred';
      });
    },

    playSong(item) {
      if (item.video_link) {
        this.selected = item.video_link;
      } else {
        this.selected = item.song__video_link;
      }
      this.playDialog = true;
      this.videoSrc = this.selected;
    },

    deleteItem(item) {
      this.selected = item;
      this.index = this.ratings.indexOf(item);
      this.deleteDialog = true;
    },

    deleteItemConfirm() {
      this.removeFromList(this.selected);
      this.closeDialog('deleteDialog');
    },

    saveRating(item) {
      this.editRating(item.song__pk);
      item.rating = this.rating;
      this.closeDialog('ratingDialog');
    },

    openRatingDialog(item) {
      this.ratingDialog = true;
      this.selected = item;
    },

    openAddDialog(item) {
      this.addDialog = true;
      this.selected = item;
    },

    closeDialog(dialog) {
      this.$data[dialog] = false;
    },
  },
  mounted() {
    this.$http.defaults.xsrfHeaderName = 'X-CSRFToken';
    this.$http.defaults.xsrfCookieName = 'csrftoken';
  },
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
    max-width: 75px;
}

.mid {
    max-width: 50px;
}
</style>
