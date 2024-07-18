#include <iostream>

using namespace std;


bool isEven(int value){
    int leftover = value & 1;
    bool res = (leftover == 0);
    return res;
}

bool isEven2(int value){
    int leftover = value % 2;
    bool res = (leftover == 0);
    return res;
}

int main(){
    return 0;
}