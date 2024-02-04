use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut hs=HashSet::new();
        for el in nums {
            if hs.contains(&el) {
                return true;
            }
            else {
                hs.insert(el);
            }
        }
        return false;
    }
}


struct Solution { }
fn main() {
    println!("{}",Solution::contains_duplicate([1,2,3,1].to_vec())); // true
    println!("{}",Solution::contains_duplicate([1,2,3,4].to_vec())); // false
    println!("{}",Solution::contains_duplicate([1,1,1,3,3,4,3,2,4,2].to_vec())); // true
}