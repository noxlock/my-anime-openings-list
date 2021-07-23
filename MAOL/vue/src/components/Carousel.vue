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
                style='background-color: grey'
                >
                    <video controls width='35%' preload='auto'>
                        <source :src=songs[selected].video_link type="video/webm">
                    </video>
                </v-row>
            </v-sheet>
        </v-expand-transition>
    </v-sheet>
</template>
<script>

  export default {
    name: 'Carousel',
    props: {
        songs: {
            type: Array
        }
    },
    data: () => ({
        selected: null
    })
  }
</script>