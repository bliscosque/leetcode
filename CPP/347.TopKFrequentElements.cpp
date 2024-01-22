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
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int,int> m{};
    for (int n:nums) {
        if (m.count(n)>0) {
            m[n]++;
        }
        else{
            m[n]=1;
        }
    }

    vector<int> ans{};
    for (int i=0;i<k;i++) {
        auto maxEl=max_element(m.begin(),m.end(), [](const auto& lhs, const auto& rhs) {return lhs.second < rhs.second;});
        //cout << maxEl->first << endl;
        ans.push_back(maxEl->first);
        m.erase(maxEl);
    }

    return ans;
}

int main() {
    vector<int> n1={1,1,1,2,2,3};
    cout << topKFrequent(n1,2) << endl; //[1,2]

    vector<int> n2={1};
    cout << topKFrequent(n2,1) << endl; //[1]
    return 0;
}