<template>
        <v-card elevation="0">
            <v-toolbar flat>

                <v-img src='vue/src/assets/site-logo-trans.png'
                max-width='267' max-height='63'></v-img>

                <v-spacer></v-spacer>

                <div class="d-flex justify-space-between">
                    <div>
                        <!-- If logged in -->
                        <a v-if="username != 'AnonymousUser'" :href="'/profile/' + username">
                            {{ username }}
                            <v-icon>mdi-account</v-icon>
                        </a>
                        <a v-else href="/auth/login">Login</a>
                    </div>

                    <br>

                    <a href="/auth/logout"><v-icon>mdi-exit-to-app</v-icon></a>
                </div>
            </v-toolbar>
        </v-card>
</template>

<script>

export default {
  name: 'Toolbar',
  props: {
    username: {
      type: String,
    },
  },
};
</script>

<style scoped>

a {
    padding-left: 20px;
    text-decoration: none;
}
</style>
