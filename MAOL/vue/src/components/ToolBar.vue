<template>
        <v-card elevation="0">
            <v-toolbar flat>

                <a href="/">
                    <v-img src='/static/site-logo-trans.png'
                    max-width='267' max-height='63'></v-img>
                </a>

                <v-spacer></v-spacer>

                <div class="d-flex justify-space-between">
                    <div>
                        <!-- If logged in -->
                        <a v-if="user != 'AnonymousUser'" :href="'/profile/' + user">
                            {{ user }}
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
    user: {
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
