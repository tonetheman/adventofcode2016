
let _ = require("ramda");

let trace = _.curry(function(tag,x) {
	console.log(tag,x);
	return x;
});

let compose = _.compose;
let split = _.split;
let replace = _.replace;
let toLower = _.toLower;
let map = _.map
let join = _.join;

var dasherize = compose( join("-"), trace("before join"), map(toLower), split(" "), replace(/s{2,}/ig," "));
var dasherize2 = compose( join("-"), map(toLower), split(" "), replace(/s{2,}/ig," "));

let res1 = dasherize("The world is a vampire");
let res2 = dasherize2("The world is a vampie");

