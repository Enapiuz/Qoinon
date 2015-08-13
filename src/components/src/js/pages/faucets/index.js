module.exports = function() {
    var $ = require('jquery');

    console.log('hello from faucets');

    function setCaption($el, title) {
        $el.html('[' + title + ']');
    }

    $(function(){
        var currencyButtons = $(".faucets__filter_btn_currency");
        var timesButtons = $(".faucets__filter_btn_time");
        var captchaButtons = $(".faucets__filter_btn_captcha");
        var walletButtons = $(".faucets__filter_btn_wallet");

        currencyButtons.click(function(ev){
            currencyButtons.removeClass('faucets__filter_btn--active');
            $(this).addClass('faucets__filter_btn--active');
            $("#faucets__currency_input").val($(this).data('currency'));
        });

        timesButtons.click(function(ev){
            timesButtons.removeClass('faucets__filter_btn--active');
            $(this).addClass('faucets__filter_btn--active');
            $("#faucets__time_input").val($(this).data('value'));
            setCaption($('.faucets__filter_time_text'), $(this).html());
        });

        captchaButtons.click(function(ev){
            captchaButtons.removeClass('faucets__filter_btn--active');
            $(this).addClass('faucets__filter_btn--active');
            $("#faucets__captcha_input").val($(this).data('value'));
            setCaption($('.faucets__filter_captcha_text'), $(this).html());
        });

        walletButtons.click(function(ev){
            walletButtons.removeClass('faucets__filter_btn--active');
            $(this).addClass('faucets__filter_btn--active');
            $("#faucets__wallet_input").val($(this).data('value'));
            setCaption($('.faucets__filter_wallet_text'), $(this).html());
        });
    });
};