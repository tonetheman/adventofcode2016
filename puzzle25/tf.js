

function read_file_as_array() {
	let fs = require("fs");
	let data = fs.readFileSync("input.txt");
	let data_s = data.toString();
	data_s = data_s.split("\n");

	data_s = data_s.filter(function(n) {
		return n.length>0
	});

	return data_s;
}
