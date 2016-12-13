
let _ = require("ramda");

function isNumeric(n) {
  let c = n[0];
  if (c=="-" || c=="0" ||
  c=="1"||c=="2"||c=="3"||
  c=="4"||c=="5"||c=="6"||
  c=="7"||c=="8"||c=="9"
  ) return true;
  return false;
}

function merge(state,o) {
  let res = {pc:state.pc, a:state.a,
  b:state.b, c:state.c, d:state.d};
  if (o.a) res.a = o.a;
  if (o.b) res.b = o.b;
  if (o.c) res.c = o.c;
  if (o.d) res.d = o.d;
  return res;
}

let i_cpy = function(s,state) {
  let data = s;
  let arg0 = data[1]; // src register or value
  let arg1 = data[2]; // dst register

  if (isNumeric(arg0)) {
    let o = {};
    o[arg1] = parseInt(arg0);
    let newState = merge(state,o);//_.merge(state,o);
    newState.pc++;
    return newState;
  } else {
    let o = {};
    o[arg1] = state[arg0];
    let newState = merge(state,o); //_.merge(state,o);
    newState.pc++;
    return newState;
  }
}

let simp_assign = function(state) {
  let res = { pc : state.pc,
    a : state.a, b : state.b, c : state.c, d : state.d };
  return res;
}

let i_inc = function(s,state) {
  let data = s;
  let arg0 = data[1]; // register to inc
  let newState = simp_assign(state);
  newState[arg0]++;
  newState.pc ++;
  return newState;
}

let i_dec = function(s,state) {
  let data = s;
  let arg0 = data[1];
  let newState = simp_assign(state);
  newState[arg0]--;
  newState.pc++;
  return newState;
}

let i_jnz = function(s,state) {
  let data = s;
  let arg0 = data[1];
  let arg1 = data[2];
  let newState = simp_assign(state)

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
    let data = s.split(" ");
    if (data[0]=="cpy") {
      state = i_cpy(data,state);
    } else if (data[0] == "inc") {
      state = i_inc(data,state);
    } else if (data[0] == "dec") {
      state = i_dec(data,state);
    } else if (data[0] == "jnz") {
      state = i_jnz(data,state);
    }
    return state;
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
console.log("starting state",state);
let ALEN = s.length;
while(true) {
  state = cpu(s[state.pc],state);
  //console.log("state after step",state);
  if (state.pc>=ALEN) {
    console.log("end of program");
    break;
  }
}
console.log("final state",state);
