<template v-slot:extension>
    <v-tabs v-model="active_tab" class="d-flex justify-center">

        <v-tab href="http://127.0.0.1:8000/">
            Home
        </v-tab>

        <v-tab href="http://127.0.0.1:8000/anime">
            Anime
        </v-tab>

        <v-tab href="http://127.0.0.1:8000/top">
            Top
        </v-tab>

        <v-tab href="http://127.0.0.1:8000/random">
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
    active_tab: 2,
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
