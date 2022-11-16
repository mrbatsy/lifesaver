#include<iostream>
using namespace std;

void printNFibonacci(int n) {
    int num1 = 0;
    int num2 = 1;
    if(n < 2) {
        cout << num1 << " " << num2 << " ";
        return;
    }
    int num3 = num1 + num2;
    for(int i=2; i<n; i++) {
        num1 = num2;
        num2 = num3;
        num3 = num1 + num2;
        cout << num3 << " ";
    }
    cout << endl;
}

// fibonacci series 
int main() {
    // print first n fibonnaci numbers
    int n;
    cin >> n;
    printNFibonacci(n);
    return 0;
}