use std::collections::HashSet;

pub fn length_of_longest_substring(s: String) -> i32 {
    let mut hs:HashSet<char>=HashSet::new();
    let mut last_idx=0;
    let mut ans=0;
    for ch in s.chars() {
        if !hs.contains(&ch) {
            hs.insert(ch);
            ans=ans.max(hs.len() as i32);
        }
        else {
            let mut l_char=s.chars().nth(last_idx).unwrap();
            while l_char!=ch {
                hs.remove(&l_char);
                last_idx+=1;
                l_char=s.chars().nth(last_idx).unwrap();
            }
            last_idx+=1;
        }
        //println!("{} {:?} {}",ch, hs, ans)
    }
    ans
}

fn main() {
    println!("{}",length_of_longest_substring("abcabcbb".to_string())); //3
    println!("{}",length_of_longest_substring("bbbbb".to_string())); //1
    println!("{}",length_of_longest_substring("pwwkew".to_string())); //3
    println!("{}",length_of_longest_substring("aabaab!bb".to_string())); //3
}