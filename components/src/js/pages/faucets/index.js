module.exports = function() {
    var $ = require('jquery');
    var superFilter = require('./filter');
    var liker = require('../../common/likes');

    $(function(){
        console.log('hello from faucets');

        var filter = superFilter.faucetsFilter(
            ".faucets__filter_btn_currency",
            ".faucets__filter_btn_time",
            ".faucets__filter_btn_captcha",
            ".faucets__filter_btn_wallet",
            ".faucets__faucet"
        );

        var $likeFaucets = $(".like-faucet");
        var $dislikeFaucets = $(".dislike-faucet");

        $likeFaucets.click(function(){
            var faucetId = $(this).data('faucet-id');
            liker.likeFaucet(faucetId, liker.LIKE, function(likes){
                $("#faucet-rating-" + faucetId).html(likes);
            });
        });

        $dislikeFaucets.click(function(){
            var faucetId = $(this).data('faucet-id');
            liker.likeFaucet(faucetId, liker.DISLIKE, function(likes){
                $("#faucet-rating-" + faucetId).html(likes);
            });
        });
    });
};