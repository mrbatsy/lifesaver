#include<iostream>
using namespace std;
int recursiveFibonacci(int n) {
    if(n == 0) return 0;
    if (n == 1) return 1;
    
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2);
}

int main() {
    int n;
    cin >> n;
    cout << recursiveFibonacci(n) << "\n";
    return 0;
}