let mix = require('laravel-mix');

mix.js('vue/app.js', 'dist/').sass('vue/app.scss', 'dist/')

mix.setResourceRoot("/static/build"); // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setPublicPath("static"); // Path where mix-manifest.json is created

// Now you can use full mix api
// Refer the file that was created in Step 2 to be compile
mix.js(`home/resources/js/home.js`, `static/build`).vue()
mix.sass(`home/resources//sass/home.scss`, `static/build`);

