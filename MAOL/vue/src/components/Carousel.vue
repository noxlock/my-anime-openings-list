<template>
  <v-sheet
    class="mx-auto"
    elevation="8"
    max-width="800"
  >
    <v-slide-group
      class="pa-4"
      center-active
      show-arrows
    >
      <v-slide-item
        v-for="song in songs"
        :key="song.pk"
        v-slot="{ active, toggle }"
      >
        <v-card
          :color="active ? 'grey darken-2' : 'grey lighten-1'"
          class="ma-4"
          height="200"
          width="100"
          @click="toggle"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <v-card-title>
                {{ song.fields.name }}
            </v-card-title>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
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
    })
  }
</script>