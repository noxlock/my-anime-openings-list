// const path = require('path');
const BundleTracker = require("webpack-bundle-tracker");

const pages = {
    'index': {
        entry: './src/home.js',
        chunks: ['chunk-vendors']
    },
}

module.exports = {
    pages: pages,
    filenameHashing: false,
    productionSourceMap: false,
    publicPath: process.env.NODE_ENV === 'production'
        ? ''
        : `http://0.0.0.0:${process.env.PORT}/`,
    outputDir: '../static/vue/',
    runtimeCompiler: true,

    chainWebpack: config => {

        config.optimization
            .splitChunks({
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: "chunk-vendors",
                        chunks: "all",
                        priority: 1
                    },
                },
            });

        Object.keys(pages).forEach(page => {
            config.plugins.delete(`html-${page}`);
            config.plugins.delete(`preload-${page}`);
            config.plugins.delete(`prefetch-${page}`);
        })

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../vue/webpack-stats.json'}]);

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public(`http://0.0.0.0:${process.env.PORT}`)
            .host('0.0.0.0')
            .port(process.env.PORT)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["*"]})

    }
};