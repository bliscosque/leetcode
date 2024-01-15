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

int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> maxHeap(stones.begin(), stones.end());
    while (maxHeap.size()>=2) {
        int el1=maxHeap.top(); maxHeap.pop();
        int el2=maxHeap.top(); maxHeap.pop();
        if (el1!=el2) {
            maxHeap.push(abs(el1-el2));
        }
    }
    if (maxHeap.size()==1) return maxHeap.top();
    return 0;
}

int main() {
    vector<int> v1{2,7,4,1,8,1};
    cout << lastStoneWeight(v1) << endl; // 1

    vector<int> v2{1};
    cout << lastStoneWeight(v2) << endl; // 1
}