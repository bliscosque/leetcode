#include <bits/stdc++.h>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    for (char ch: s) {
        if (ch=='(' or ch=='[' or ch=='{') {
            st.push(ch);
        }
        else {
            if (st.size()<=0) return false;
            char lchar=st.top();
            st.pop();
            if (ch==')' and lchar!='(') return false;
            else if (ch==']' and lchar!='[') return false;
            else if (ch=='}' and lchar!='{') return false;
        }
    }
    if (st.size()==0) return true;
    return false;
}

int main() {
    cout << isValid("()") << endl; //true

    cout << isValid("()[]{}") << endl; //true

    cout << isValid("(]") << endl; //false

    cout << isValid("]") << endl; //false
    
    return 0;
}