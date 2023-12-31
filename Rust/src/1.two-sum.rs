/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
use std::collections::HashMap;
//impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm=HashMap::new();
        let mut ans: Vec<i32>=Vec::new();
        for (i,el) in nums.iter().enumerate() {
            //println!("{} {}",i,el);
            let search=target-el;
            if hm.contains_key(&search) {
                ans.push(i as i32);
                ans.push(hm[&search]);
                ans.sort();
                return ans;
            }
            hm.insert(el,i as i32);
        }
        ans

    }
//}
// @lc code=end

#[cfg(test)]
mod tests {
    use super::two_sum;

    #[test]
    fn test_two_sum() {
        // Standard case.
        assert_eq!(two_sum(vec![1, 2, 3, 4, 5], 9), vec![3, 4]);
    }
}