<template>
  <div>
    <v-alert
      border="top"
      color="red lighten-2"
      dark
    >
      {{ msg }}
    </v-alert>
    </div>
</template>

<script>
    export default {
        name: 'Test',
        props: { msg: String },
    }
</script>