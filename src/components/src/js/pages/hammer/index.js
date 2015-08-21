module.exports = function() {
    var $ = require('jquery');
    require('jquery.cookie');

    $.cookie('qwe', 'ewq');

    console.log('hello from hammer');
};