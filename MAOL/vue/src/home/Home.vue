<template>
  <v-app>
    <v-main>
        <ToolBar></ToolBar>
        Home
    </v-main>
  </v-app>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'

export default {
  name: 'Home',
    components: {
        ToolBar
    },

  data: () => ({
    //
  }),
};
</script>
