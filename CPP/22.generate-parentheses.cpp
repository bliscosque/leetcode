#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec) {
    os << "[";
    if (!vec.empty()) {
        // Print the first element outside the loop to avoid a trailing comma
        os << vec[0];

        // Print the rest of the elements with a comma separator
        for (size_t i = 1; i < vec.size(); ++i) {
            os << ", " << vec[i];
        }
    }
    os << "]";
    return os;
}

// --------------------------------------------------------------- //

class Solution {
public:
    vector<char> stack;
    vector<string> res;
    int N;

    void backtrack(int openN, int closedN) {
        if (openN==closedN and openN==N) {
            string s(stack.begin(),stack.end());
            res.push_back(s);
            return;
        }
        if (openN<N) {
            stack.push_back('(');
            backtrack(openN+1,closedN);
            stack.pop_back();
        }
        if (closedN<openN) {
            stack.push_back(')');
            backtrack(openN,closedN+1);
            stack.pop_back();
        }
        
    }

    vector<string> generateParenthesis(int n) {
        N=n;
        backtrack(0,0);
        return res;
    }
};

int main() {
    Solution s;
    cout << s.generateParenthesis(2) << endl;
    cout << s.generateParenthesis(3) << endl;
    return 0;
}