#include <iostream>
using namespace std;

// Simple function to calculate factorial
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    float x = 3.14;
    // This is a comment
    cout << "Hello, World!" << endl;
    
    int num = 5;
    int result = factorial(num);
    
    if (result > 0) {
        cout << "Factorial of " << num << " is " << result << endl;
    }
    
    /* This is a 
       multi-line comment */
    
    for (int i = 0; i < 10; i++) {
        x += 0.5;
    }
    
    return 0;
}