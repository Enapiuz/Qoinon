module.exports = function() {
    var $ = require('jquery');
    var superFilter = require('./filter');

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
            faucetLikeAction($(this).data('faucet-id'), 1)
        });

        $dislikeFaucets.click(function(){
            faucetLikeAction($(this).data('faucet-id'), 2)
        });

        function faucetLikeAction(faucetId, type) {
            $.ajax({
                'url': '/api/like_faucet',
                'dataType': 'JSON',
                'cache': false,
                'data': {
                    'type': type,
                    'faucet_id': faucetId
                }
            }).success(function(data){
                if (data.success == 1) {
                    $("#faucet-rating-" + faucetId).html(data.likes);
                }
            }).complete(function(){

            });
        }
    });
};