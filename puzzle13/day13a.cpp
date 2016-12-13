#include <iostream>
#include <bitset>

int main() {

#define CHECK_BIT(var,pos) ((var) & (1<<(pos)))

  int a = 10;

  std::bitset<8> b(a);

  using namespace std;

  cout << "bitset: " << b << endl;
  cout << "b0: " << CHECK_BIT(a,0) << endl;
  cout << "b1: " << CHECK_BIT(a,1) << endl;
  cout << "b2: " << CHECK_BIT(a,2) << endl;
  cout << "b3: " << CHECK_BIT(a,3) << endl;

  return 0;
}
