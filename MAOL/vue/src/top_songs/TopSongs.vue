<template>
    <div>
        <ToolBar :user="user"></ToolBar>
        <HomeAppBar></HomeAppBar>
        <Banner
        :styles="'home-style'"
        :image="`https://wallpaperboat.com/wp-content/uploads/2020/06/03/42361/aesthetic-anime-01.jpg`"
        :heading="'MAOL'"
        :subheader="'The best anime site since ' + date.toLocaleString()"
        >
        </Banner>
        <v-card-title>
            Top Rated Songs
            <v-spacer></v-spacer>
            <v-text-field
            @focus="searchClosed = false"
            @blur="searchClosed = true"
            v-model='search'
            placeholder="Search"
            filled
            dense
            prepend-inner-icon='mdi-magnify'
            class="search mt-1"
            :class="{ 'closed': searchClosed && !search }"
        ></v-text-field>
        </v-card-title>
        <SongList :ratings="songs" :user="user"
        :headers="[
        {'value': 'anime__cover'},
        {'text': 'Type', 'value': 'song_type'},
        {'text': 'Number', 'value': 'number'},
        {'text': 'Song Name', 'value': 'name'},
        {'value': 'actions', 'sortable': false},
        ]"></Songlist>
    </div>
</template>

<script>
import ToolBar from '../components/ToolBar.vue';
import HomeAppBar from '../components/HomeAppBar.vue';
import Banner from '../components/Banner.vue';
import SongList from '../components/SongList.vue';

export default {
  name: 'Top',
  components: {
    ToolBar,
    HomeAppBar,
    Banner,
    SongList,
  },
  props: {
    songs: {
      type: Array,
    },
    user: {
      type: String,
    },
  },
  data: () => ({
    search: '',
    searchClosed: true,
    date: new Date(Date.now()),
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
