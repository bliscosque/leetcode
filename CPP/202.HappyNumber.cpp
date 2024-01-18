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

bool isHappy(int n) {
    bool flag=false;
    set<int> nums;
    nums.insert(n);
    while (!flag) {
        std::vector<int> digits;
        string nstr=to_string(n);
        for (char ch: nstr) {
            digits.push_back(ch-'0');
        }
        //cout << digits << endl;
        int newn = 0;
        for (int i:digits) {
            newn+=i*i;
        }
        if (newn==1) return true;
        n=newn;
        if (nums.count(n)>0) {
            flag=true;
        }
        nums.insert(n);
        //cout << n << endl;
    }
    return false;
}

int main() {
    cout << isHappy(19) << endl;
    cout << isHappy(2) << endl;
    return 0;
}