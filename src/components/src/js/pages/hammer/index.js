module.exports = function() {
    var $ = require('jquery');
    require('jquery.cookie');
    require('zeroclipboard');
    require('jquery.clipboard');

    console.log('hello from hammer');

    var currentCurrency = $("#hammer__current_currency_helper").val();
    var $pastBtn = $("#hammer__past_btn");
    var $editBtn = $("#hammer__edit_btn");

    $pastBtn.click(function(e){
        e.preventDefault();
    });

    $editBtn.click(function(e){
        e.preventDefault();
    });

    $pastBtn.clipboard({
        path: '/static/components/swf/jclip.swf',
        copy: function() {
            var value = $.cookie('address' + currentCurrency);

            if (typeof value == 'undefined') {
                value = window.prompt("Enter your wallet address:","");
            }

            return value;
        }
    });

    $editBtn.clipboard({
        path: '/static/components/swf/jclip.swf',
        copy: function() {
            var value = window.prompt("Enter your wallet address:","");
            $.cookie('address' + currentCurrency, value);
            return value;
        }
    });
};