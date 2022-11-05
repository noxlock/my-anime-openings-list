<template>
        <v-card>
            <v-parallax
                height="300"
                dark
                :src="'/media/' + profile[0].fields.banner"
            >
                <img :src="'/media/' + profile[0].fields.avatar" width="256">
                <v-row class="text-start">
                    <v-col>
                        <v-btn class="mr-4">
                            <a :href="'/profile/' + username">Profile</a>
                        </v-btn>
                        <v-btn>
                            <a :href="'/profile/' + username + '/list'">Song List</a>
                        </v-btn>
                    </v-col>
                </v-row>
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

<style scoped>
v-btn {
    max-width: 100px;
}
v-row {
    margin: 0
}
</style>
