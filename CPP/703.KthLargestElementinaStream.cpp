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

int K;
vector<int> NUMS_SMALLER;
vector<int> NUMS_BIGGER;

void KthLargest(int k, vector<int>& nums) {
    
    K=k;
    sort(nums.begin(),nums.end());
    int n=nums.size();
    
    //NUMS_BIGGER.resize(n);
    cout << "k: " << k << ", n: " << n << ", nums: "<< nums << endl;
    if (k<=n) {
        NUMS_SMALLER.resize(n-k);
        copy(begin(nums),begin(nums)+n-k,begin(NUMS_SMALLER));
        //cout << NUMS_SMALLER << endl;
    }
    int nBig=min(k,n);
    NUMS_BIGGER.resize(nBig);
    copy(begin(nums)+n-nBig,end(nums),begin(NUMS_BIGGER));
    cout << NUMS_BIGGER << endl;
    
    make_heap(NUMS_BIGGER.begin(),NUMS_BIGGER.end(), std::greater<int>()); //min heap
}

int add(int val) {
    if (NUMS_BIGGER.size() < K) {
        NUMS_BIGGER.push_back(val);
        push_heap(NUMS_BIGGER.begin(), NUMS_BIGGER.end(), std::greater<int>());
    }
    else if (val>NUMS_BIGGER[0]) {
        if (NUMS_BIGGER.size()>0) {
            pop_heap(NUMS_BIGGER.begin(), NUMS_BIGGER.end(), std::greater<int>());
            NUMS_BIGGER.pop_back();
        }
        NUMS_BIGGER.push_back(val);
        push_heap(NUMS_BIGGER.begin(), NUMS_BIGGER.end(), std::greater<int>());
    }
    
    //cout << NUMS_BIGGER << endl;
    return NUMS_BIGGER[0];
}

//TODO: COM ERRO!!
//["KthLargest","add","add","add","add","add"]
//[[2,[0]],[-1],[1],[-2],[-4],[3]]

int main() {
    vector<int> n{4, 5, 8, 2};
    KthLargest(3,n);
    vector<int> adds{3,5,10,9,4};
    for (int a:adds) {
        cout << add(a) << " ";
    }
    cout << endl; // [null,4,5,5,8,8]

    vector<int> n2{};
    KthLargest(1,n2);
    vector<int> adds2{-3,-2,-4,0,4};
    for (int a:adds2) {
        cout << add(a) << " ";
    }
    cout << endl; // [null,-3,-2,-2,0,4]

    vector<int> n3{0};
    KthLargest(2,n3);
    vector<int> adds3{-1,1,-2,-4,3};
    for (int a:adds3) {
        cout << add(a) << " ";
    }
    cout << endl; // [null,-1,0,0,0,1]

    return 0;
}