
let _ = require("ramda");

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

let i_cpy = function(s,state) {
  let data = s.match(/cpy\s+(\d+|[a-z]+)\s+(\d+|[a-z]+)/)
  let arg0 = data[1]; // src register or value
  let arg1 = data[2]; // dst register

  if (isNumeric(arg0)) {
    let o = {};
    o[arg1] = parseFloat(arg0);
    let newState = _.merge(state,o);
    return newState;
  } else {
    let o = {};
    o[arg1] = state[arg0];
    let newState = _.merge(state,o);
    return newState;
  }
}

let i_inc = function(s,state) {
  let data = s.match(/inc\s+([a-z]+)/)
  let arg0 = data[1]; // register to inc
  let newState = JSON.parse(JSON.stringify(state));
  newState[arg0]++;
  return newState;
}

let i_dec = function(s,state) {
  let data = s.match(/dec\s+([a-z]+)/)
  let arg0 = data[1];
  let newState = JSON.parse(JSON.stringify(state));
  newState[arg0]--;
  return newState;
}

let i_jnz = function(s,state) {
  let data = s.match(/jnz\s+([a-z]+|\d+)\s+([a-z]+|\d+)/)
  let arg0 = data[1];
  let arg1 = data[2];
  return state;
}

let cpu = function(s,state) {
    console.log("CPU",s,state);
    if (s.startsWith("cpy")) {
      state = i_cpy(s,state);
    } else if (s.startsWith("inc")) {
      state = i_inc(s,state);
    } else if (s.startsWith("dec")) {
      state = i_dec(s,state);
    }
    return state;
}

let cpu2 = function(s) {
  let state = {};
  let newState = cpu(s,state);
  return newState;
}

let state = {};
let s = ["cpy 41 a", "cpy a b", "inc a", "inc a",
  "dec a", "jnz a 2", "dec a"];

for (let i=0;i<s.length;i++) {
  state = cpu(s[i],state);
  console.log("state after step",i, state);
}
