module.exports = {};

module.exports.squaredCaption = function($selector, text) {
    $selector.html('[' + text + ']');
};

module.exports.roundedCaption = function($selector, text) {
    $selector.html('(' + text + ')');
};