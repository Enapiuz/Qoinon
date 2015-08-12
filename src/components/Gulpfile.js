var elixir = require('laravel-elixir');


elixir(function(mix) {
    // ������
    mix.copy(
        './bower_components/bootstrap-sass/assets/fonts',
        './static/components/fonts'
    );

    // ��������
    mix.copy(
        './src/images',
        './static/components/images'
    );

    // css ����
    mix.sass(
        ['../../../src/scss/vendor.scss'],
        './static/components/css/vendor.css'
    );

    // css
    mix.sass(
        ['../../../src/scss/main.scss'],
        './static/components/css/main.css'
    );

    // ������� � browserify
    mix.browserify(
        '../../../src/js/main.js',
        './static/components/javascripts/main.js'
    );
});