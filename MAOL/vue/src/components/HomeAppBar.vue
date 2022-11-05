<template>
    <v-card>
        <v-tabs
        hide-slider
        class="d-flex justify-center"
        >
            <v-tab class="home" href="/">
                Home
            </v-tab>

            <v-tab href="/anime">
                Anime
            </v-tab>

            <v-tab href="/top">
                Top
            </v-tab>

            <v-tab href="/random">
                Random
            </v-tab>

            <form id="search" action="/search">
                <v-text-field
                @focus="searchClosed = false"
                @blur="searchClosed = true"
                v-model='query'
                id="query"
                name="q"
                type="search"
                placeholder="Search"
                filled
                dense
                prepend-inner-icon='mdi-magnify'
                class="search mt-1"
                :class="{ 'closed': searchClosed && !query }"
                ></v-text-field>
            </form>
        </v-tabs>

    </v-card>
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
.v-tab--active
    color: rgba(0,0,0,.54) !important
</style>
