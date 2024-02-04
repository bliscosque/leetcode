use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut ans_hm:HashMap<Vec<i32>, Vec<String>>=HashMap::new();
        
        for s in strs {
            let mut k=vec![0;26];
            for ch in s.chars() {
                let pos= ch as i32 -'a' as i32;
                k[pos as usize] +=1;
            }
            ans_hm.entry(k).or_insert(Vec::new()).push(s);
        }
        let ans=ans_hm.values().cloned().collect();
        ans
    }
}

struct Solution { }
fn main() {
    let strs1=["eat".to_string(),"tea".to_string(),"tan".to_string(),"ate".to_string(),"nat".to_string(),"bat".to_string()].to_vec();
    println!("{:?}",Solution::group_anagrams(strs1)); // [["bat"],["nat","tan"],["ate","eat","tea"]]

    let strs2=["".to_string()].to_vec();
    println!("{:?}",Solution::group_anagrams(strs2)); // [[""]]

    let strs3=["a".to_string()].to_vec();
    println!("{:?}",Solution::group_anagrams(strs3)); // [["a"]]
    
}