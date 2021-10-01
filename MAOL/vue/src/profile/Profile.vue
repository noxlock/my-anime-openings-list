<template>
    <h1>Deez {{user}}</h1>
</template>
<script>

export default {
  name: 'Profile',
  props: {
    user: {
      type: String,
    },
  },
  data: () => ({
  }),
};
</script>
