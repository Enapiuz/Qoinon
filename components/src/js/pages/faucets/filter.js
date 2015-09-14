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
        times: {
            val: null,
            min: 'null',
            max: 'null'
        },
        captcha: null,
        wallet: null
    };

    function changeLink($el) {
        var btn = $el.find(".faucets__btn_go").first();
        var newLink = btn.data('href');

        newLink += (selection.currency == null)? '' : '&cur=' + selection.currency;
        newLink += (selection.captcha == null)? '' : '&cpt=' + selection.captcha;
        newLink += (selection.wallet == null)? '' : '&cat=' + selection.wallet;
        newLink += (selection.times.min == null || selection.times.min == 'null')? '' : '&tmin=' + selection.times.min;
        newLink += (selection.times.max == null || selection.times.max == 'null')? '' : '&tmax=' + selection.times.max;

        btn.attr('href', newLink);
    }

    function filter() {
        console.log(selection);

        faucets.each(function(idx){
            var canDisplay = true;
            var $this = $(this);

            if (selection.currency !== null && $this.data('currency') != selection.currency) {
                canDisplay = false;
            }

            if (selection.captcha !== null && $this.data('captcha') != selection.captcha) {
                canDisplay = false;
            }

            if (selection.wallet !== null && $this.data('wallet') != selection.wallet) {
                canDisplay = false;
            }

            if (selection.times.min !== 'null' && selection.times.min !== null && $this.data('cooldown') < selection.times.min) {
                canDisplay = false;
            }

            if (selection.times.max !== 'null' && selection.times.max !== null && $this.data('cooldown') > selection.times.max) {
                canDisplay = false;
            }

            if (canDisplay) {
                changeLink($this);
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
        selection.times.val = $(this).data('value');
        selection.times.min = $(this).data('min');
        selection.times.max = $(this).data('max');

        filter();
    });

    captchaButtons.click(function(ev){
        captchaButtons.removeClass('faucets__filter_btn--active');
        $(this).addClass('faucets__filter_btn--active');
        titler.squaredCaption($('.faucets__filter_captcha_text'), $(this).text());
        selection.captcha = $(this).data('value');

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