var elixir = require('laravel-elixir');

var path = {
    'bootstrap': 'bower_components/bootstrap-sass/assets/'
};

elixir(function(mix) {
    mix.sass(
        ['../../../scss/vendor.scss'],
        './static/components/css/'
    );
});