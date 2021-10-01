<template>
        <v-card elevation="0">
            <v-toolbar flat>

                <v-img src='./assets/site-logo-trans.png' max-width='267' max-height='63'></v-img>

                <v-spacer></v-spacer>

                <div class="d-flex justify-space-between">
                    <div style='float: right;'>
                        <a v-if="username != 'AnonymousUser'" :href="'/profile/' + username">
                            {{ username }}
                        </a>
                        <a v-else href="/auth/login">Login</a>
                    </div>

                    <v-spacer></v-spacer>

                    <v-icon style='float: right;'>mdi-account</v-icon>

                    <v-spacer></v-spacer>
                    <a href="/auth/logout">Logout</a>
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
