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
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> ans;
    map<string,vector<string>> m;
    for (string s: strs) {
        string sorted=s;
        sort(sorted.begin(),sorted.end());
        if (m.count(sorted)>0) { //is this needed???
            m[sorted].push_back(s);
        }
        else {
            m[sorted].push_back(s);
        }
    }
    for (auto [k, v] : m) {
        ans.push_back(v);
    }
    return ans;
}
int main() {
    vector<string> v1{"eat","tea","tan","ate","nat","bat"};
    cout << groupAnagrams(v1) << endl;

    

    return 0;
}