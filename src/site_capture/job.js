var page = require('webpage').create();

if (phantom.args.length === 0) {
    console.log('No web page specified!');
    phantom.exit();
} else {
    console.log('target site: ' + phantom.args[0]);
    console.log('target file: ' + phantom.args[1]);

    page.viewportSize = { width: 1280, height: 1280 };
    page.clipRect = { top: 0, left: 0, width: 1280, height: 1280 };
    page.open(phantom.args[0], function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address: ' + status);
            phantom.exit(0);
        } else {
            window.setTimeout(function () {
                page.render(phantom.args[1]);
                phantom.exit(0);
            }, 200);
        }
    });

}
