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
vector<int> twoSum(vector<int>& numbers, int target) {
    int n=numbers.size();
    int l=0,r=n-1;
    while (l<=r) {
        if (numbers[l]+numbers[r]==target) return vector<int>{l+1,r+1};
        else if (numbers[l]+numbers[r]>target) r--;
        else l++;
    }
    return vector<int>{0,0};
}

int main() {
    vector<int> v1{2,7,11,15};
    cout << twoSum(v1,9) << endl; // [1,2] = 2+7=9

    vector<int> v2{2,3,4};
    cout << twoSum(v2,6) << endl; // [1,3] 

    vector<int> v3{-1,0};
    cout << twoSum(v3,-1) << endl; // [1,2]
    return 0;
}