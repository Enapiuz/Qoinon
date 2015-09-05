window.$ = window.jQuery = require('jquery');
require('bootstrap');

// подключение модулей страниц
require('./pages/faucets')();
require('./pages/hammer')();
require('./pages/faq')();