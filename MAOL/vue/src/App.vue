<template>
  <v-app>
    <v-main>
        <ToolBar></ToolBar>
    </v-main>
  </v-app>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'

export default {
  name: 'App',
    components: {
        ToolBar
    },

  data: () => ({
    //
  }),
};
</script>
