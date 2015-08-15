var $ = require('jquery');
var _ = require('lodash');
var titler = require('../../common/titler');

var faucetsFilter = function(currency, times, captcha, wallet) {
    console.log('hello from faucets filter!');

    var currencyButtons = $(currency);
    var timesButtons = $(times);
    var captchaButtons = $(captcha);
    var walletButtons = $(wallet);

    currencyButtons.click(function(ev){
        currencyButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        $("#faucets__currency_input").val($(this).data('currency'));
    });

    timesButtons.click(function(ev){
        timesButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        $("#faucets__time_input").val($(this).data('value'));
        titler.squaredCaption($('.faucets__filter_time_text'), $(this).text());
    });

    captchaButtons.click(function(ev){
        captchaButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        $("#faucets__captcha_input").val($(this).data('value'));
        titler.squaredCaption($('.faucets__filter_captcha_text'), $(this).text());
    });

    walletButtons.click(function(ev){
        walletButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        $("#faucets__wallet_input").val($(this).data('value'));
        titler.squaredCaption($('.faucets__filter_wallet_text'), $(this).text());
    });
};

module.exports = {};
module.exports.faucetsFilter = faucetsFilter;