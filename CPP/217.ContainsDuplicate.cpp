#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool containsDuplicate(vector<int>& nums) {
    int oldamt=nums.size();
    sort(nums.begin(),nums.end());
    nums.erase(unique(nums.begin(),nums.end()),nums.end());
    //for (int i : nums)
    //    cout << i << " ";
    //cout << endl;
    return oldamt!=nums.size();
}

int main() {
    vector<int> v1({1,2,3,1});
    cout << containsDuplicate(v1) << endl; //true
    vector<int> v2({1,2,3,4});
    cout << containsDuplicate(v2) << endl; //false
    vector<int> v3({1,1,1,3,3,4,3,2,4,2});
    cout << containsDuplicate(v3) << endl; //true
    
    return 0;
}