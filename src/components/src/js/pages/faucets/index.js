module.exports = function() {
    var $ = require('jquery');

    console.log('hello from faucets');

    function setDropdownSelection($dropdown, title) {

    }

    $(function(){
        var currencyButtons = $(".faucets__filter_btn_currency");

        currencyButtons.click(function(ev){
            currencyButtons.removeClass('faucets__filter_btn--active');
            $(this).addClass('faucets__filter_btn--active');
            $("#faucets__currency_input").val($(this).data('currency'));
        });
    });
};