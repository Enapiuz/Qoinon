module.exports = function () {
    var $ = require('jquery');
    require('jquery.cookie');
    var zc = require('ZeroClipboard');

    console.log('hello from hammer');

    var currentCurrency = $("#hammer__current_currency_helper").val();
    var $pastBtn = $("#hammer__past_btn");
    var $editBtn = $("#hammer__edit_btn");
    var $faucetboxBtn = $("#hammer__faucetbox_balance");

    var cookieName = 'address' + currentCurrency;

    var client = new zc($pastBtn);

    client.on('ready', function (event) {
        // console.log( 'movie is loaded' );

        client.on('copy', function (event) {
            var value = $.cookie(cookieName);

            if (typeof value == 'undefined' || value.length == 0) {
                value = window.prompt("Enter your wallet address:","");
                $.cookie(cookieName, value);

                if (value == '') {
                    $faucetboxBtn.addClass('hide');
                } else {
                    $faucetboxBtn.attr('href', "https://faucetbox.com/en/check/" + value);
                    $faucetboxBtn.removeClass('hide');
                }
            }

            event.clipboardData.setData('text/plain', value);
        });

        client.on('aftercopy', function (event) {
            console.log('Copied text to clipboard: ' + event.data['text/plain']);
        });
    });

    client.on('error', function (event) {
        // console.log( 'ZeroClipboard error of type "' + event.name + '": ' + event.message );
        ZeroClipboard.destroy();
    });

    $editBtn.click(function(){
        var value = $.cookie(cookieName);
        value = window.prompt("Enter your wallet address:", value);

        if (value == null) return;

        $.cookie(cookieName, value);

        if (value == '') {
            $faucetboxBtn.addClass('hide');
        } else {
            $faucetboxBtn.attr('href', "https://faucetbox.com/en/check/" + value);
            $faucetboxBtn.removeClass('hide');
        }
    });

    $(function(){
        var hammerMenu = $("#hammer__menu");
        var mainMenu = $("#main_menu");
        var hammer = $(".hammer");

        $(window).resize(function(){
            if (hammerMenu.length == 1 && mainMenu.length == 1 && hammer.length > 0) {
                hammer.css('top', hammerMenu.height() + mainMenu.height() + 'px');
            }
        });
        $(window).resize();

    });
};