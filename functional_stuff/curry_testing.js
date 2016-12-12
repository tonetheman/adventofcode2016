
let R = require("ramda");

var match = R.curry(function(what,str) {
	return str.match(what);
});

var replace = R.curry(function(what,replacement,str) {
	return str.replace(what,replacement);
});

var filter = R.curry(function(f,ary){
	return ary.filter(f);
});

var map = R.curry(function(f,ary) {
	return ary.map(f);
});

console.log(match(/\s+/g, "hello world"));
console.log(match(/\s+/g)("hello world")); // this returns a function first then does another call

var hasSpaces = match(/\s+/g);

console.log( hasSpaces("hello world") );
console.log( hasSpaces("nospaceshere") );


console.log( filter(hasSpaces, ["tony_colston", "tori amos"]) );

var findSpaces = filter(hasSpaces);

console.log( findSpaces(["tony_colston", "tori amos"]) );


