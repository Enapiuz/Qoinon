var elixir = require('laravel-elixir');

elixir.config.registerWatcher("default", "./src/**/*");

elixir(function(mix) {
    mix.copy(
        './node_modules/bootstrap-sass/assets/fonts',
        './static/components/fonts'
    );

    mix.copy(
        './src/images',
        './static/components/images'
    );

    mix.copy(
        './node_modules/jquery-clipboard/jquery.clipboard.swf',
        './static/components/swf/jclip.swf'
    );

    mix.copy(
        './node_modules/jquery-clipboard/jquery.clipboard.js',
        './static/components/javascripts/jclip.js'
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