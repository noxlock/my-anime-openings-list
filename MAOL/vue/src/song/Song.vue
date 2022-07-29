<template>
    <v-main>
        <ToolBar :user="username"></ToolBar>
        <div>
            <v-card>
                <h1>{{song[0].anime__english_name}} {{song[0].song_type}}{{song[0].number}}</h1>
                <h2>{{song[0].name}}</h2>
            </v-card>

            <video ref="video" :src="song[0].video_link" controls width='70%' preload='metadata'>
                <source type="video/webm">
            </video>
        </div>
    </v-main>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';

export default {
  name: 'Song',
  components: {
    ToolBar,
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
  }),
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
</style>
