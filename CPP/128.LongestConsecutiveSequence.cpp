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

int longestConsecutive(vector<int>& nums) {
    int ans=0;
    unordered_map<int,bool> um;
    for (int el:nums) {
        um[el]=false;
    }
    for (auto [el,visited]:um) {
        if (!visited) {
            um[el]=true;
            int count=1;
            int search=el-1;
            while (um.count(search)>0) {
                um[search]=true;
                count+=1;
                search-=1;
            }
            search=el+1;
            while (um.count(search)>0) {
                um[search]=true;
                count+=1;
                search+=1;
            }
            ans=max(ans,count);
        }
    }
    return ans;
}

int main() {
    vector<int> v1{100,4,200,1,3,2};
    cout << longestConsecutive(v1) << endl; //4 [1..4]

    vector<int> v2{0,3,7,2,5,8,4,6,0,1};
    cout << longestConsecutive(v2) << endl; //9 [0..8]

    return 0;
}