
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
    o[arg1] = parseInt(arg0);
    let newState = _.merge(state,o);
    newState.pc++;
    return newState;
  } else {
    let o = {};
    o[arg1] = state[arg0];
    let newState = _.merge(state,o);
    newState.pc++;
    return newState;
  }
}

let i_inc = function(s,state) {
  let data = s.match(/inc\s+([a-z]+)/)
  let arg0 = data[1]; // register to inc
  let newState = JSON.parse(JSON.stringify(state));
  newState[arg0]++;
  newState.pc ++;
  return newState;
}

let i_dec = function(s,state) {
  let data = s.match(/dec\s+([a-z]+)/)
  let arg0 = data[1];
  let newState = JSON.parse(JSON.stringify(state));
  newState[arg0]--;
  newState.pc++;
  return newState;
}

let i_jnz = function(s,state) {
  let data = s.match(/jnz\s+([a-z]+|\d+|-\d+)\s+([a-z]+|\d+|-\d+)/)
  let arg0 = data[1];
  let arg1 = data[2];
  let newState = JSON.parse(JSON.stringify(state));

  // arg0 is a number
  if (isNumeric(arg0)) {
    if (parseInt(arg0)!=0) {
      // need to jump!
      if (isNumeric(arg1)) {
        // arg1 is numeric just jump
        newState.pc += parseInt(arg1);
        return newState;
      } else {
        // arg1 is a register get the value
        // first then set the pc
        newState.pc += parseInt(state[arg1]);
      }
    } else {
      newState.pc++;
    }
  } else {
    // arg0 is a register
    if (state[arg0]!=0) {
      //if it is 0 we need to jump
      if (isNumeric(arg1)) {
        // arg1 is numeric just jump
        newState.pc += parseInt(arg1);
        return newState;
      } else {
        // arg1 is a register get the value
        // first then set the pc
        newState.pc += parseInt(state[arg1]);
      }
    } else {
      newState.pc ++;
    }
  }
  return newState;
}

let cpu = function(s,state) {
    //console.log("CPU",s);
    if (s.startsWith("cpy")) {
      state = i_cpy(s,state);
    } else if (s.startsWith("inc")) {
      state = i_inc(s,state);
    } else if (s.startsWith("dec")) {
      state = i_dec(s,state);
    } else if (s.startsWith("jnz")) {
      state = i_jnz(s,state);
    }
    return state;
}

let cpu2 = function(s) {
  let state = {};
  let newState = cpu(s,state);
  return newState;
}

let state = {pc : 0, a: 0, b : 0, c : 1, d : 0};
/*
let s = ["cpy 41 a", "inc a", "inc a",
  "dec a", "jnz a 2", "dec a"];
*/

let s = ["cpy 1 a",
"cpy 1 b",
"cpy 26 d",
"jnz c 2",
"jnz 1 5",
"cpy 7 c",
"inc d",
"dec c",
"jnz c -2",
"cpy a c",
"inc a",
"dec b",
"jnz b -2",
"cpy c b",
"dec d",
"jnz d -6",
"cpy 17 c",
"cpy 18 d",
"inc a",
"dec d",
"jnz d -2",
"dec c",
"jnz c -5"]

/*
let s = ["cpy 1 a",
        "cpy 1 b",
        "cpy 1 c",
        "dec b",
        "jnz b -2"];
*/
let count = 0;
console.log("starting state",state);
while(true) {
  state = cpu(s[state.pc],state);
  //console.log("state after step",state);
  if (state.pc>=s.length) {
    console.log("end of program");
    break;
  }
  count++;
  if (count%10000==0) {
    console.log(count);
  }
  if (count>28959500) {
    console.log("broke for count");
    break;
  }
}
console.log("final state",state);
