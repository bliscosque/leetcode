impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut ans=Vec::new();
        let n=temperatures.len();
        for (idx,t) in temperatures.iter().enumerate() {
            let mut p=idx+1;
            while p<n && temperatures[p]<=*t { 
                p+=1;
            }
            if p==n {
                ans.push(0);
            }
            else {
                ans.push((p-idx) as i32);
            }
        }
        ans
    }
}

struct Solution { }
fn main() {
    println!("{:?}",Solution::daily_temperatures([73,74,75,71,69,72,76,73].to_vec())); // [1,1,4,2,1,1,0,0]
    println!("{:?}",Solution::daily_temperatures([30,40,50,60].to_vec())); // [1,1,1,0]
    println!("{:?}",Solution::daily_temperatures([30,60,90].to_vec())); // [1,1,0]
    println!("{:?}",Solution::daily_temperatures([89,62,70,58,47,47,46,76,100,70].to_vec())); // [8,1,5,4,3,2,1,1,0,0]
}