const path = require('path');
const CopyPlugin = require('copy-webpack-plugin')

module.exports = {
  entry: './app/static/src/js/index.js',  // Correct entry path under the 'app' folder
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'app', 'static', 'dist', 'js'),  // Output directory
  },
  module: {
    rules: [
      // JavaScript and CSS loaders as required
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              ['@babel/preset-env', { targets: "defaults" }]
            ]
          }
        }
      },
      {
        test: /\.scss$/,
        use: [
          'style-loader',  // Injects CSS into the DOM
          'css-loader',    // Translates CSS into CommonJS
          'sass-loader'    // Compiles Sass to CSS
        ]
      }
    ]
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        // Copy Shoelace assets to dist/shoelace
        {
          from: path.resolve(__dirname, 'node_modules/@shoelace-style/shoelace/dist/assets'),
          to: path.resolve(__dirname, 'app/static/dist/css/shoelace/assets')
        }
      ]
    })
  ]
};