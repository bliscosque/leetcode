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

int missingNumber(vector<int>& nums) {
    int n=nums.size();
    int ans=0;
    for (int i=1;i<=n;i++) {
        ans = ans ^ i ^ nums[i-1];
    }
    return ans;
}

int main() {
    vector<int> n1{3,0,1};
    cout << missingNumber(n1) << endl; //2

    vector<int> n2{0,1};
    cout << missingNumber(n2) << endl; //2

    vector<int> n3{9,6,4,2,3,5,7,0,1};
    cout << missingNumber(n3) << endl; //8
    return 0;
}