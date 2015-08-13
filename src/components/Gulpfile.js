var elixir = require('laravel-elixir');

elixir.config.registerWatcher("default", "./src/**/*");

elixir(function(mix) {
    mix.copy(
        './bower_components/bootstrap-sass/assets/fonts',
        './static/components/fonts'
    );

    mix.copy(
        './src/images',
        './static/components/images'
    );

    mix.sass(
        ['../../../src/scss/vendor.scss'],
        './static/components/css/vendor.css'
    );

    mix.sass(
        ['../../../src/scss/main.scss'],
        './static/components/css/main.css'
    );

    mix.browserify(
        '../../../src/js/main.js',
        './static/components/javascripts/main.js'
    );
});