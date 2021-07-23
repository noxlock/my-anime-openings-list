<template>
    <v-parallax
        dark
        src="https://wallpaperboat.com/wp-content/uploads/2020/06/03/42361/aesthetic-anime-01.jpg"
    >
        <v-row
        align="center"
        justify="center"
        >
            <v-col
            class="text-center"
            cols="12"
            style='color: white;'
            >
                <div style="background-color: rgba(128, 0, 128, 0.2);">
                    <h1 class="text-h4 font-weight-thin mb-4" style="text-shadow: 0 0 3px #FF0000, 0 0 5px #0000FF;">
                        MAOL
                    </h1>
                    <h4 class="subheading" style="text-shadow: 0 0 5px #800080;">
                        The best anime site since {{ date.toLocaleString() }}
                    </h4>
                </div>
            </v-col>
        </v-row>
    </v-parallax>
</template>

<script>
export default {
    name: 'HomeBanner',
    data: () => ({
        date: new Date(Date.now())
    })
  }
</script>

