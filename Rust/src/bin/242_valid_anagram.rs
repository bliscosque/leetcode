use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut h1=HashMap::new();
        let mut h2=HashMap::new();
        for ch in s.chars() {
            let cnt=h1.entry(ch).or_insert(0);
            *cnt += 1;
        }
        for ch in t.chars() {
            let cnt=h2.entry(ch).or_insert(0);
            *cnt += 1;
        }
        h1==h2
    }
}


struct Solution { }
fn main() {
    println!("{}",Solution::is_anagram("anagram".to_string(), "nagaram".to_string())); // true
    println!("{}",Solution::is_anagram("rat".to_string(), "cat".to_string())); // false
}