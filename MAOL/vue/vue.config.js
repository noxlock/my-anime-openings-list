const BundleTracker = require('webpack-bundle-tracker');

const pages = {
  index: {
    entry: './src/pages/index.js',
    chunks: ['chunk-vendors'],
  },
  profile: {
    entry: './src/pages/profile.js',
    chunks: ['chunk-vendors'],
  },
  list: {
    entry: './src/pages/list.js',
    chunks: ['chunk-vendors'],
  },
  animeListing: {
    entry: './src/pages/animeListing.js',
    chunks: ['chunk-vendors'],
  },
  anime: {
    entry: './src/pages/anime.js',
    chunks: ['chunk-vendors'],
  },
  song: {
    entry: './src/pages/song.js',
    chunks: ['chunk-vendors'],
  },
};

module.exports = {
  pages,
  filenameHashing: false,
  productionSourceMap: false,
  publicPath: process.env.NODE_ENV === 'production'
    ? ''
    : 'http://localhost:8080/',
  outputDir: '../static/vue/',
  runtimeCompiler: true,

  chainWebpack: (config) => {
    config.optimization
      .splitChunks({
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: 'chunk-vendors',
            chunks: 'all',
            priority: 1,
          },
        },
      });

    Object.keys(pages).forEach((page) => {
      config.plugins.delete(`html-${page}`);
      config.plugins.delete(`preload-${page}`);
      config.plugins.delete(`prefetch-${page}`);
    });

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: '../vue/webpack-stats.json' }]);

    config.resolve.alias
      .set('__STATIC__', 'static');

    config.devServer
      .public('http://localhost:8080')
      .host('localhost')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ 'Access-Control-Allow-Origin': ['*'] });
  },
};
