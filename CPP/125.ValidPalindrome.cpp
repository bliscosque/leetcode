#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(string s) {
    string ns="";
    for (char ch:s) {
        if (isalnum(ch)) {
            ns+=tolower(ch);
        }
    }
    //cout << ns << endl;
    string rev=string(ns.rbegin(),ns.rend());
    return ns==rev;
}

int main() {
    cout << isPalindrome("A man, a plan, a canal: Panama") << endl; //true
    cout << isPalindrome("race a car")  << endl; //false
    cout << isPalindrome(" ") << endl; //true
    cout << isPalindrome("0P") << endl; //false
    return 0;
}