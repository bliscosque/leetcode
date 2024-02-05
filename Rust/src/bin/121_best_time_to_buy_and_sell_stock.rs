impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // l=0, r=1
        // while r<n
        //      if price[l] < price[r]
        //          calcular profit, maxprofit
        //      else l=r
        //      r++
        let mut l=0;
        let mut r=0;
        let mut max_profit=0;
        let n=prices.len();
        while r<n {
            if prices[l]<prices[r] {
                let profit=prices[r]-prices[l];
                max_profit=max_profit.max(profit);
            }
            else {l=r}
            r+=1;
        }
        max_profit

    }
}

struct Solution { }
fn main() {
    println!("{}",Solution::max_profit([7,1,5,3,6,4].to_vec())); // 6-1=5

    println!("{}",Solution::max_profit([7,6,4,3,1].to_vec())); // 0
}