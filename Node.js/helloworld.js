// load http module
var http = require('http');

// create http server
http.createServer(function (req, res) {
	
	// content header
	res.writeHead(200, {'content-type': 'text/plain'});

	// write message and signal communicate is complete
	res.end("Hello, World!\n");
}).listen(8124);

console.log('Server is running on 8124');