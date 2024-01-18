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

int hammingWeight(uint32_t n) {
    int ans=0;
    while (n) {
        ans+= n&1;
        n=n>>1;
    }
    return ans;
}

int main() {
    cout << hammingWeight(11) << endl; //3
    cout << hammingWeight(128) << endl; //1
    return 0;
}