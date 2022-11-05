<template>
    <v-main>
        <ToolBar :user="username"></ToolBar>
        <HomeAppBar></HomeAppBar>
        <div>
            <v-card flat>
                <h1>{{song[0].anime__english_name}} {{song[0].song_type}}{{song[0].number}}</h1>
                <h2>{{song[0].name}}</h2>
            </v-card>
            <br/>
        </div>

            <v-row>
                <v-col cols="9">
                    <video ref="video" :src="song[0].video_link"
                    controls width='70%' preload='metadata'>
                    <source type="video/webm">
                    </video>
                </v-col>
                <v-col cols="3">
                    <div style="float:left; color:blue;">
                        <a :href="'../anime/' + song[0].anime__pk">
                            <h3>
                                {{
                                    song[0].anime__english_name
                                }}
                                <br/>
                            </h3>
                        </a>
                        <h4>
                            {{
                                song[0].song_type + song[0].number + ' ' + song[0].name
                            }}
                        </h4>
                        <br/>
                        <v-select
                        :items="[1,2,3,4,5,6,7,8,9,10]"
                        v-model="rating"
                        label="Rating"
                        return-object
                        :filled=true
                        ></v-select>
                        <v-btn
                        color="primary"
                        :disabled="rating === ''"
                        @click="addToList(song[0].pk)"
                        >
                            Add To List
                        </v-btn>
                    </div>
                </v-col>
            </v-row>

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
    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';

export default {
  name: 'Song',
  components: {
    ToolBar,
    HomeAppBar,
  },
  props: {
    song: {
      type: Array,
    },
    username: {
      type: String,
    },
  },
  data: () => ({
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

<style>
h1, h2 {
    text-align: center;
}
video {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

h4 {
    color: #1976D2
}
</style>
