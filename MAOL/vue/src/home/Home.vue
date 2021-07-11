<template>
  <v-app>
    <v-main>
        <ToolBar></ToolBar>
        <Carousel :songs=songs></Carousel>
        <br>
        <br>
        <br>
        <ul id="example-1">
            <li v-for="song in songs" :key="song.pk">
                <iframe width="560" height="315" :src=song.fields.youtube_link title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </li>
        </ul>
    </v-main>
  </v-app>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import Carousel from '@/components/Carousel.vue'


export default {
  name: 'Home',
    components: {
        ToolBar,
        Carousel
    },
    props: {
        songs: {
            type: Array
        }
     },

  data: () => ({
    //
  }),
};
</script>
