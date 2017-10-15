#!/usr/bin/env node

const webpack = require('webpack');


const NODE_ENV = process.env.NODE_ENV || 'development';
module.exports = {

    entry: {
        index: './index.jsx',
    },

    resolve: {
        // modules: [`${__dirname}/static_src`, 'node_modules'],
        extensions: ['.js', '.jsx'],
    },

    context: `${__dirname}/static_src`,

    output: {
        path: `${__dirname}/static/build/`,
        filename: NODE_ENV === 'development' ? '[name].js' : '[name]-[hash].js',
        publicPath: '/static/build/',
        library: '[name]',
    },

    watch: NODE_ENV === 'development',
    watchOptions: {
        aggregateTimeout: 100,
    },

    module:
        {
            rules: [
                {
                    test: /\.(js|jsx)$/,
                    include: `${__dirname}/static_src`,
                    loader: 'babel-loader?presets[]=react&presets[]=es2015',
                },
                {
                    test: /\.css$/,
                    loader: 'style-loader!css-loader',
                },
                {
                    test: /\.(png|jpg|gif|svg|ttf|eot|woff|woff2)$/,
                    loader: 'url-loader?limit=4096&name=[path][name].[ext]',
                },
            ],
        }
    ,

    devtool: NODE_ENV === 'development' ? 'cheap-module-source-map' : false,

    plugins:
        [
            new webpack.NoEmitOnErrorsPlugin(),
        ],
}
;

if (NODE_ENV !== 'development') {
    module.exports.plugins.push(
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warning: false,
                drop_console: true,
            },
        })
    )
}
