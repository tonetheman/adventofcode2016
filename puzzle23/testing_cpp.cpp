#include <iostream>

using std::cout;
using std::endl;

char* program[] = {
"cpy a b",
"dec b",
"cpy a d",
"cpy 0 a",
"cpy b c",
"inc a",
"dec c",
"jnz c -2",
"dec d",
"jnz d -5",
"dec b",
"cpy b c",
"cpy c d",
"dec d",
"inc c",
"jnz d -2",
"tgl c",
"cpy -16 c",
"jnz 1 c",
"cpy 96 c",
"jnz 91 d",
"inc a",
"inc d",
"jnz d -2",
"inc c",
"jnz c -5",
};

struct State {
    int pc;
    int a,b,c,d;
};

void state_init(struct State& state) {
  state.pc = state.a = state.b = state.c = state.d = 0;
}

std::ostream& operator<<(std::ostream& os, struct State& src) {
  os << "pc:" << src.pc << " " <<
  "a:" << src.a << " " <<
    "b:" << src.b << " " <<
      "c:" << src.c << " " <<
        "d:" << src.d;
  return os;
}

bool chk_int(char * s) {
  if (s[0]=='a' || s[0]=='b' ||
  s[0]=='c' || s[0]=='d') {
    return false;
  }
  return true;
}

int cvt_to_int(char * s) {
  int tmp = 0,dec=0;
  int len = strlen(s);
  for(int i=0; i<len; i++){
    dec = dec * 10 + ( s[i] - '0' );
  }
  return dec;
}

void i_cpy(struct State & state) {
  char saved[32];
  strcpy(saved, program[state.pc]);
  char instr[32];
  char arg1[32];
  char arg2[32];

  int count = 0;
  char * pch = strtok (saved," ");
  while (pch != NULL)
  {
    if (count==0) strcpy(instr,pch);
    pch = strtok (NULL, " ");
    count++;
    if (count==1) strcpy(arg1,pch);
    if (count==2) strcpy(arg2,pch);
  }

  int srcval = -1;

  if (chk_int(arg1)) {
    // src is a number
    srcval = atoi(arg1);
  } else {
    // src is a register name
    if (arg1[0]=='a') {
      srcval = state.a;
    } else if (arg1[0]=='b') {
      srcval = state.b;
    } else if (arg1[0]=='c') {
      srcval = state.c;
    } else if (arg1[0]=='d') {
      srcval = state.d;
    } else {
      cout << "ERR(2) invalid arg1 for cpy" << arg1 << endl;
      exit(0);
    }
  }

  char * dst = arg2;
  if (dst[0]=='a') {
    state.a = srcval;
  } else if (dst[0]=='b') {
    state.b = srcval;
  } else if (dst[0]=='c') {
    state.c = srcval;
  } else if (dst[0]=='d') {
    state.d = srcval;
  } else {
    cout << "ERR invalid arg1 for cpy" << arg1 << endl;
    exit(0);
  }

  state.pc ++;

}

void i_inc(struct State & state) {
  char saved[32];
  strcpy(saved, program[state.pc]);
  char instr[32];
  char arg1[32];

  int count = 0;
  char * pch = strtok (saved," ");
  while (pch != NULL)
  {
    if (count==0) strcpy(instr,pch);
    pch = strtok (NULL, " ");
    count++;
    if (count==1) strcpy(arg1,pch);
  }

  if (arg1[0]=='a') {
    state.a++;
  } else if (arg1[0]=='b') {
    state.b++;
  } else if (arg1[0]=='c') {
    state.c++;
  } else if (arg1[0]=='d') {
    state.d++;
  } else {
    cout << "invalid inc" << endl;
    exit(0);
  }

  state.pc ++;

}

void i_dec(struct State & state) {
  char saved[32];
  strcpy(saved, program[state.pc]);
  char instr[32];
  char arg1[32];

  int count = 0;
  char * pch = strtok (saved," ");
  while (pch != NULL)
  {
    if (count==0) strcpy(instr,pch);
    pch = strtok (NULL, " ");
    count++;
    if (count==1) strcpy(arg1,pch);
  }

  //cout << "dec called - " << instr << " " << arg1 << endl;
  if (arg1[0]=='a') {
    state.a--;
  } else if (arg1[0]=='b') {
    state.b--;
  } else if (arg1[0]=='c') {
    state.c--;
  } else if (arg1[0]=='d') {
    state.d--;
  } else {
    cout << "invalid dec" << endl;
    exit(0);
  }

  state.pc ++;
}

void i_jnz(struct State & state) {
  char saved[32];
  strcpy(saved, program[state.pc]);
  char instr[32];
  char arg1[32];
  char arg2[32];

  int count = 0;
  char * pch = strtok (saved," ");
  while (pch != NULL)
  {
    if (count==0) strcpy(instr,pch);
    pch = strtok (NULL, " ");
    count++;
    if (count==1) strcpy(arg1,pch);
    if (count==2) strcpy(arg2,pch);
  }

  // TODO: NEED TO FINISH THIS PART
  int xval = -1;
  if (chk_int(arg1)) {
    // arg1 is a number
    xval = atoi(arg1);
  } else {
    // arg1 is not a number
    if (arg1[0]=='a') {
      xval = state.a;
    } else if (arg1[0]=='b'){
      xval = state.b;
    } else if (arg1[0]=='c') {
      xval = state.c;
    } else if (arg1[0]=='d') {
      xval = state.d;
    }
  }

  if (xval!=0) {
    // NEED TO MAKE THE JUMP FIGURE
    // OUT the number of steps
    int yval = -1;

    if (chk_int(arg2)) {
      yval = atoi(arg2);
    } else {
      if (arg2[0]=='a') {
        yval = state.a;
      } else if (arg2[0]=='b') {
        yval = state.b;
      } else if (arg2[0]=='c') {
        yval = state.c;
      } else if (arg2[0]=='d') {
        yval = state.d;
      }
    }

    state.pc = state.pc + yval;

  }

}

void execute(struct State & state) {
  char * current_instruction = program[state.pc];
  cout << "current_instruction is " << current_instruction << endl;
  if (strncmp(current_instruction,"cpy",3)==0) {
    i_cpy(state);
  }
  if (strncmp(current_instruction,"inc",3)==0) {
    i_inc(state);
  }
  if (strncmp(current_instruction,"dec",3)==0) {
    i_dec(state);
  }
  if (strncmp(current_instruction,"jnz",3)==0) {
    i_jnz(state);
  }
  cout << "state at end of execute: " << state << endl;
}

int main() {

  State state;
  state_init(state);
  state.a = 7;

  while (true) {
    execute(state);
  }

  return 0;
}
