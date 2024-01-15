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
int minCostClimbingStairs(vector<int>& cost) {
    int n=cost.size();
    vector<int> dp(n+2,0);
    dp[0]=cost[0];
    dp[1]=cost[1];

    for (int i=2;i<n;i++) {
        int op1=dp[i-1]+cost[i];
        int op2=dp[i-2]+cost[i];
        dp[i]=min(op1,op2);
    }
    dp[n]=min(dp[n-1],dp[n-2]);
    //cout << dp << endl;
    return dp[n];
}

int main() {
    vector<int> v1{10,15,20};
    cout << minCostClimbingStairs(v1) << endl; //15

    vector<int> v2{1,100,1,1,1,100,1,1,100,1};
    cout << minCostClimbingStairs(v2) << endl; //6
}