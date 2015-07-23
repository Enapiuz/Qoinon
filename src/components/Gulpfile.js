var elixir = require('laravel-elixir');


elixir(function(mix) {
    mix.copy(
        './bower_components/bootstrap-sass/assets/fonts',
        './static/components/fonts'
    );

    mix.sass(
        ['../../../scss/vendor.scss'],
        './static/components/css/vendor.css'
    );

    mix.sass(
        ['../../../scss/main.scss'],
        './static/components/css/main.css'
    );

    mix.scripts(
        ['../../../bower_components/bootstrap-sass/assets/javascripts/bootstrap.js'],
        './static/components/javascripts/vendor.js'
    );
});