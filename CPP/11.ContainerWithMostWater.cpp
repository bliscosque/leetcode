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

int maxArea(vector<int>& height) {
    int l=0,r=height.size()-1;
    int ans=0;
    while (l<r) {
        int area=min(height[l],height[r])*(r-l);
        //cout << l << " " << r << " Area: " << area << endl;
        ans=max(ans,area);
        if (height[l]<height[r]) l++;
        else r--;
    }
    return ans;
}

int main() {
    vector<int> v1{1,8,6,2,5,4,8,3,7};
    cout << maxArea(v1) << endl; //49
    return 0;
}