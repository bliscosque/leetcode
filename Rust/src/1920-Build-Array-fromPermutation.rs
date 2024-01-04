//impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans=Vec::new();
        for i in &nums {
            let ipos=*i as usize;
            //let ipos1=nums[ipos] as usize;
            ans.push(nums[ipos]);
        }
        ans
    }
//}

fn main() {
    let ans=build_array([0,2,1,5,3,4].to_vec());
    println!("{:?}",ans); //[0,1,2,4,5,3] - ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]

    let ans2=build_array([5,0,1,2,3,4].to_vec());
    println!("{:?}",ans2); //[4,5,0,1,2,3]
}