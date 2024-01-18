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

vector<int> countBits(int n) {
    vector<int> ans{0};
    for (int i=1;i<=n;i++) {
        ans.push_back(hammingWeight(i));
    }
    return ans;
}

int main() {
    cout << countBits(2) << endl;
    cout << countBits(5) << endl;

    return 0;
}