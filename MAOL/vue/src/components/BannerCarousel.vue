<template>
        <v-carousel
        cycle
        height="400"
        hide-delimiter-background
        show-arrows-on-hover
        >

            <v-carousel-item>
                <v-parallax
                dark
                src="/static/ai-art-1.png"
                class="artone"
                :height="height"
                >
                    <div class="bannertext-background">
                        <h1 class="banner-header text-h4 mb-4 text-center">
                            {{heading}}
                        </h1>
                        <h4 class="subheading text-center">
                            {{subheader}}
                        </h4>
                    </div>
                </v-parallax>
            </v-carousel-item>

            <v-carousel-item>
                <v-parallax
                dark
                src="/static/ai-art-2.png"
                class="arttwo"
                :height="height"
                >
                    <div class="bannertext-background">
                        <h1 class="banner-header text-h4 mb-4 text-center">
                            {{heading}}
                        </h1>
                        <h4 class="subheading text-center">
                            {{subheader}}
                        </h4>
                    </div>
                </v-parallax>
            </v-carousel-item>

            <v-carousel-item>
                <v-parallax
                dark
                src="/static/ai-art-3.png"
                class="artthree"
                :height="height"
                >
                    <div class="bannertext-background">
                        <h1 class="banner-header text-h4 mb-4 text-center">
                            {{heading}}
                        </h1>
                        <h4 class="subheading text-center">
                            {{subheader}}
                        </h4>
                    </div>
                </v-parallax>
            </v-carousel-item>
        </v-carousel>
</template>

<script>
export default {
  name: 'BannerCarousel',
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
.artone {
    .banner-header {
        text-shadow: 0 0 3px #0000FF, 0 0 5px #0000FF;
        font-weight: light;
    }
    .subheading {
        text-shadow: 0 0 5px #0000FF;
    }
}

.arttwo {
    .banner-header {
        text-shadow: 0 0 3px #4d2549, 0 0 5px #4d2549;
        font-weight: light;
    }
    .subheading {
        text-shadow: 0 0 5px #4d2549;
    }
}

.artthree {
    .banner-header {
        text-shadow: 0 0 3px #FF0000, 0 0 5px #0000FF;
        font-weight: light;
    }
    .subheading {
        text-shadow: 0 0 5px #800080;
    }
}

</style>
