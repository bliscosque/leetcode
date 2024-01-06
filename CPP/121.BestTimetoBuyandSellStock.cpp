#include <bits/stdc++.h>
using namespace std;

int maxProfit(vector<int>& prices) {
    int min_price=prices[0];
    int max_profit=0;
    for (int price:prices) {
        int profit=price-min_price;
        max_profit=max(max_profit,profit);
        min_price=min(min_price,price);
    }
    return max_profit;
}

int main() {
    vector<int> v1 {7,1,5,3,6,4};
    cout << maxProfit(v1) << endl; //5 (buy day 2 (price=1, sell day 6(price=6))

    vector<int> v2 {7,6,4,3,1};
    cout << maxProfit(v2) << endl; //5 (buy day 2 (price=1, sell day 6(price=6))

    return 0;
}