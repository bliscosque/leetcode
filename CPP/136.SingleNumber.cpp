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

int singleNumber(vector<int>& nums) {
    int n=nums.size();
    int ans=nums[0];
    for (int i=1;i<n;i++) {
        ans=ans^nums[i];
    }
    return ans;
}

int main() {
    vector<int> v1{2,2,1};
    cout << singleNumber(v1) << endl;

    vector<int> v2{4,1,2,1,2};
    cout << singleNumber(v2) << endl;

    vector<int> v3{1};
    cout << singleNumber(v3) << endl;
    return 0;
}