var $ = require('jquery');

module.exports = {};

module.exports.LIKE = 1;
module.exports.DISLIKE = 2;

module.exports.likeFaucet = function(faucetId, type, ifSuccess) {
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
            ifSuccess(data.likes);
        }
    }).complete(function(){

    });
};