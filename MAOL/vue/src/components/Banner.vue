<template>
    <v-parallax
        dark
        :src="image"
        :class="styles"
        :height="height"
    >
    <div class="bannertext-background">
        <h1 class="banner-header text-h4 font-weight-thin mb-4 text-center">
            {{heading}}
        </h1>
        <h4 class="subheading text-center">
            {{subheader}}
        </h4>
    </div>
    </v-parallax>
</template>

<script>
export default {
  name: 'Banner',
  props: {
    styles: {
      type: String,
    },
    image: {
      type: String,
    },
    height: {
      type: String,
    },
    heading: {
      type: String,
    },
    subheader: {
      type: String,
    },
  },
  data: () => ({
  }),
};
</script>

<style lang="scss" scoped>
.home-style {
    .bannertext-background {
        background-color: rgba(128, 0, 128, 0.2);
    }
    .banner-header {
        text-shadow: 0 0 3px #FF0000, 0 0 5px #0000FF;
    }
    .subheading {
        text-shadow: 0 0 5px #800080;
    }
}

.anime-style {
    .bannertext-background {
        background-color: rgba(225, 231, 245, 0.2);
    }
    .banner-header {
        text-shadow: 0 0 3px #000000, 0 0 5px #000000;
    }
    .subheading {
        text-shadow: 0 0 5px #800080;
    }
}

</style>
