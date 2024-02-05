use std::collections::HashMap;

pub fn character_replacement(s: String, k: i32) -> i32 {
    let s_c:Vec<char>=s.chars().collect();
    let mut ans=0;
    let mut hm=HashMap::new();
    let mut l=0;
    for i in 0..s_c.len() {
        /*
        if hm.contains_key(&ch) {
            hm[ch]+1;
        }
        else {
            hm[ch]=1;
        }
        */
        let ch=s_c[i];
        *hm.entry(ch).or_insert(0) += 1;
        let mut max_val=*hm.values().max().unwrap();
        let mut num_el=i as i32 - l as i32 + 1;
        if num_el - max_val > k  { //elements need to be removed from left
            *hm.get_mut(&s_c[l]).unwrap()-=1;
            l+=1;
        }
        ans=ans.max(i as i32 - l as i32 + 1);
    }
    ans
}

fn main() {
    println!("{}",character_replacement("ABAB".to_string(), 2)); //4
    println!("{}",character_replacement("AABABBA".to_string(), 1)); //4
}