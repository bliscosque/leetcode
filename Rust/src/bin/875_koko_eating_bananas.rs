impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut min_v = 1;
        let mut max_v = *piles.iter().max().unwrap();

        while min_v < max_v {
            let test = min_v + (max_v - min_v) / 2;
            let sum: i64 = piles.iter().map(|&val| (val as f64 / test as f64).ceil() as i64).sum();

            if sum > h as i64 {
                min_v = test + 1;
            } else {
                max_v = test;
            }
        }

        min_v
    }
}

struct Solution {}

fn main() {
    println!("{}", Solution::min_eating_speed([3, 6, 7, 11].to_vec(), 8)); // 4
    println!("{}", Solution::min_eating_speed([30, 11, 23, 4, 20].to_vec(), 5)); // 30
    println!("{}", Solution::min_eating_speed([30, 11, 23, 4, 20].to_vec(), 6)); // 23
    println!(
        "{}",
        Solution::min_eating_speed([805306368, 805306368, 805306368].to_vec(), 1000000000)
    ); // 3
}
