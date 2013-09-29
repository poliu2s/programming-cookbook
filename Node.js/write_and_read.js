// Reading and writing data to stdin and stdout, respectively

process.stdin.resume();

process.stdin.on('data', function (chunk) {
	process.stdout.write('data: ' + chunk);
});