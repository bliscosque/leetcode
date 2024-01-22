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

vector<int> productExceptSelf(vector<int>& nums) {
    long long m=1;
    vector<int> ans;
    for (int el: nums) {
        m*=el;
    }
    for (int i=0;i<nums.size();i++) {
        if (nums[i]==0) {
            long m2=1;
            for (int k=0;k<nums.size();k++) {
                if (k==i) continue;
                m2*=nums[k];
            }
            ans.push_back(m2);
        }
        else {
            float rev=pow(nums[i],-1);
            ans.push_back(m*rev);
        }
        
    }
    return ans;
}

int main() {
    vector<int> n1{1,2,3,4};
    cout << productExceptSelf(n1) << endl; //[24,12,8,6]

    vector<int> n2{-1,1,0,-3,3};
    cout << productExceptSelf(n2) << endl; //[0,0,9,0,0]
    return 0;
}