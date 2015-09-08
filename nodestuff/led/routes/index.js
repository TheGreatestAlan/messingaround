var express = require('express');
var router = express.Router();
var alicia = 'Hello.  Alicia. You\'re one of the perviest people I\'ve ever met .';
var drew = 'Hello. Drew.  You silly old man.';
var standard = 'THE WORLD IS MIIIIINNNEEEEEE!!!!!!';
var me = 'Why hello there, you handsome devil';

router.get('/',function(req, res) {
	if(req.connection.remoteAddress == '50.183.124.90'){
		standard = alicia;
	} else if (req.connection.remoteAddress == '66.249.84.199') {
		standard = drew;
	} else if (req.connection.remoteAddress == '66.87.151.233') {
		standard = drew;
	} else if (req.connection.remoteAddress == '107.2.238.40') {
		standard = me;
	}
	res.render('index', {
		title: 'ALANALANALAN',
		inside: standard
	});
	console.log(req.connection.remoteAddress);
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
