#include <iostream>
#include <string>

using namespace std;

string testResultSmiley(bool result) {
    return result ? "(^o^) PASS" : "(>_<) FAIL";
}

string boolString(bool b) {
    return b ? "true" : "false";
}

bool testBool(bool testVal, bool expected) {
    cout << "Testing " << boolString(testVal)
         << " expecting " << boolString(expected)
         << '\n';
    
    cout << testResultSmiley(testVal == expected);
    cout << "\n\n";
}

bool testString(string testVal, string expected) {
    cout << "Testing " << testVal
         << " expecting " << expected
         << '\n';
    
    cout << testResultSmiley(testVal == expected);
    cout << "\n\n";
}

bool isSquare(int n) {
    if (n == 1 || n == 4 || n == 9) {
        return true;
    }
    return false;
}

int main() {
    testBool(1 == 1, true);
    testBool(isSquare(3), false);
    testBool(isSquare(9), true);
    testBool(isSquare(25), true);
    testString("abc", "abc");
}
        
