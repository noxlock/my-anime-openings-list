<template v-slot:extension>
    <v-tabs class="d-flex justify-center">
        <v-tabs-slider color="blue"></v-tabs-slider>

        <v-tab>
            Home
        </v-tab>

        <v-tab>
            Anime
        </v-tab>

        <v-tab>
            Top
        </v-tab>

        <v-tab>
            Random
        </v-tab>

        <v-text-field
            @focus="searchClosed = false"
            @blur="searchClosed = true"
            v-model='query'
            placeholder="Search"
            filled
            dense
            prepend-inner-icon='mdi-magnify'
            class="search mt-1"
            :class="{ 'closed': searchClosed && !query }"
        ></v-text-field>
    </v-tabs>

</template>

<script>

export default {
  name: 'HomeAppBar',
  props: {
  },
  data: () => ({
    searchClosed: true,
    query: null,
  }),
};
</script>

<style lang='sass'>
.v-input.search
    transition: max-width 0.5s
    float: left
    .v-input__slot
        &:before, &:after
            border-color: transparent !important
    &.closed
        max-width: 45px
        .v-input__slot
            background: transparent !important
</style>
