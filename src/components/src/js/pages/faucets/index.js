module.exports = function() {
    var $ = require('jquery');
    var superFilter = require('./filter');

    $(function(){
        console.log('hello from faucets');

        var filter = superFilter.faucetsFilter(
            ".faucets__filter_btn_currency",
            ".faucets__filter_btn_time",
            ".faucets__filter_btn_captcha",
            ".faucets__filter_btn_wallet"
        );
    });
};