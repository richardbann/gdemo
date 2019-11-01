const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main-[chunkhash].js",
    path: path.resolve(__dirname, "build")
  },
  devtool: "eval-source-map",
  plugins: [
    new MiniCssExtractPlugin({
      filename: "main-[chunkhash].css",
      path: path.resolve(__dirname, "build"),
      ignoreOrder: false // Enable to remove warnings about conflicting order
    }),
    new CleanWebpackPlugin()
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [
              "@babel/preset-react",
              [
                "@babel/preset-env",
                {
                  targets: {
                    browsers: ["last 2 versions"]
                  },
                  modules: false // Needed for tree shaking to work.
                }
              ]
            ]
          }
        }
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          // "style-loader",  not to use with minicss extract plugin
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              ident: "postcss",
              // postcss-preset-env, cssnano ?
              plugins: [require("tailwindcss"), require("autoprefixer")]
            }
          }
        ]
      }
    ]
  }
};
