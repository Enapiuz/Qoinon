var $ = require('jquery');
var _ = require('lodash');
var titler = require('../../common/titler');

var faucetsFilter = function(currency, times, captcha, wallet, faucet) {
    console.log('hello from faucets filter!');

    var currencyButtons = $(currency);
    var timesButtons = $(times);
    var captchaButtons = $(captcha);
    var walletButtons = $(wallet);
    var faucets = $(faucet);

    var selection = {
        currency: null,
        times: null,
        captca: null,
        wallet: null
    };

    function filter() {
        console.log(faucets);

        faucets.each(function(idx){
            var canDisplay = true;
            var $this = $(this);

            if ($this.data('currency') != selection.currency) {
                canDisplay = false;
            }

            if (canDisplay) {
                $this.show();
            } else {
                $this.hide();
            }
        });
    }

    currencyButtons.click(function(ev){
        currencyButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        selection.currency = $(this).data('currency');

        filter();
    });

    timesButtons.click(function(ev){
        timesButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        titler.squaredCaption($('.faucets__filter_time_text'), $(this).text());
        selection.times = $(this).data('value');

        filter();
    });

    captchaButtons.click(function(ev){
        captchaButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        titler.squaredCaption($('.faucets__filter_captcha_text'), $(this).text());
        selection.captca = $(this).data('value');

        filter();
    });

    walletButtons.click(function(ev){
        walletButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        titler.squaredCaption($('.faucets__filter_wallet_text'), $(this).text());
        selection.wallet = $(this).data('value');

        filter();
    });
};

module.exports = {};
module.exports.faucetsFilter = faucetsFilter;