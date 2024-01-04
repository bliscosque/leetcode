//impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut ans=nums.clone();
        ans.extend(&nums);
        ans
    }
//}

fn main() {
    let ans=get_concatenation([1,2,1].to_vec());
    println!("{:?}",ans); //[1,2,1,1,2,1]

    let ans2=get_concatenation([1,3,2,1].to_vec());
    println!("{:?}",ans); //[1,3,2,1,1,3,2,1]
}