<template>
        <v-card outlined align="center">
            <v-parallax
                height="300"
                dark
                :src="'/media/' + profile[0].fields.banner"
            >
                <img :src="'/media/' + profile[0].fields.avatar" width="256">
            </v-parallax>
        </v-card>
</template>

<script>
export default {
  name: 'ProfileBanner',
  props: {
    profile: {
      type: Array,
    },
  },
};
</script>
