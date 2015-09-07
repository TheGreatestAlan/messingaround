var express = require('express');
var router = express.Router();

///* GET home page. */
//router.get('/', function(req, res, next) {
//  res.render('index', { title: 'Express' });
//});


router.get('/',function(req, res) {
	res.render('index', {
		title: 'My App!'
	});
	var util = require('util'),
	    exec = require('child_process').exec,
	    child;
	child = exec('sudo python ../../led.py',
		function (error, stdout, stderr) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error: ' + error);
			}
		});
});

module.exports = router;
