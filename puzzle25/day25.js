
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

let simp_assign = function(state) {
  let res = { pc : state.pc,
    a : state.a, b : state.b, c : state.c, d : state.d };
  return res;
}

let i_cpy = function(s,state) {
  let data = s.split(" ");
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
  let data = s.split(" ");
  let arg0 = data[1]; // register to inc
  let newState = simp_assign(state);
  newState[arg0]++;
  newState.pc ++;
  return newState;
}

let i_dec = function(s,state) {
  let data = s.split(" ");
  let arg0 = data[1];
  let newState = simp_assign(state);
  newState[arg0]--;
  newState.pc++;
  return newState;
}

let i_jnz = function(s,state) {
  let data = s.split(" ")
  let arg0 = data[1];
  let arg1 = data[2];
  let newState = simp_assign(state);

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

let i_out = function(s,state) {
  let newState = simp_assign(state);
  let data = s.split(" ")
  let arg0 = data[1];
  if (isNumeric(arg0)) {
    console.log("OUT-NUM:", arg0);
  } else {
    console.log("OUT:", state[arg0]);
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
    } else if (s.startsWith("out")) {
      state = i_out(s,state);
    } else {
      console.log("ERR: state is", state);
      console.log("ERR: unknown instruction", s);
      process.exit();
	}
    return state;
}

let cpu2 = function(s) {
  let state = {};
  let newState = cpu(s,state);
  return newState;
}

let state = {pc : 0, a: 0, b : 0, c : 0, d : 0};

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

let s = read_file_as_array();
state.a = 158;

console.log("starting state",state);
while(true) {
  state = cpu(s[state.pc],state);
  console.log("DBG",state);
  if (state.pc>=s.length) {
    console.log("end of program");
    break;
  }
}
console.log("final state",state);
