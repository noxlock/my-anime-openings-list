<template>
        <v-card>
            <v-parallax
                height="300"
                dark
                :src="'/media/' + profile[0].fields.banner"
            >
                <img :src="'/media/' + profile[0].fields.avatar" width="256">
                <v-btn style="max-width: 100px;">
                    <a :href="'/profile/' + username + '/list'">Song List</a>
                </v-btn>
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
    username: {
      type: String,
    },
  },
};
</script>
