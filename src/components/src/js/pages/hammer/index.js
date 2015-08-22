module.exports = function () {
    var $ = require('jquery');
    require('jquery.cookie');
    var zc = require('ZeroClipboard');

    console.log('hello from hammer');

    var currentCurrency = $("#hammer__current_currency_helper").val();
    var $pastBtn = $("#hammer__past_btn");
    var $editBtn = $("#hammer__edit_btn");

    var client = new ZeroClipboard($pastBtn);

    client.on('ready', function (event) {
        // console.log( 'movie is loaded' );

        client.on('copy', function (event) {
            event.clipboardData.setData('text/plain', event.target.innerHTML);
        });

        client.on('aftercopy', function (event) {
            console.log('Copied text to clipboard: ' + event.data['text/plain']);
        });
    });

    client.on('error', function (event) {
        // console.log( 'ZeroClipboard error of type "' + event.name + '": ' + event.message );
        ZeroClipboard.destroy();
    });
    
    //$pastBtn.clipboard({
    //    path: '/static/components/swf/jclip.swf',
    //    copy: function() {
    //        var value = $.cookie('address' + currentCurrency);
    //
    //        if (typeof value == 'undefined') {
    //            value = window.prompt("Enter your wallet address:","");
    //        }
    //
    //        return value;
    //    }
    //});
    //
    //$editBtn.clipboard({
    //    path: '/static/components/swf/jclip.swf',
    //    copy: function() {
    //        var value = window.prompt("Enter your wallet address:","");
    //        $.cookie('address' + currentCurrency, value);
    //        return value;
    //    }
    //});
};