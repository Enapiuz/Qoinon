module.exports = function() {
    var $ = require('jquery');
    require('jquery.cookie');

    console.log('hello from hammer');

    var currentCurrency = $("#hammer__current_currency_helper").val();
    var $pastBtn = $("#hammer__past_btn");
    var $editBtn = $("#hammer__edit_btn");

    $pastBtn.click(function(){
        var value = $.cookie('address' + currentCurrency);

        if (typeof value == 'undefined') {

        } else {

        }
    });
};