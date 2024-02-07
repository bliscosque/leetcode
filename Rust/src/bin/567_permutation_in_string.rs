use std::collections::HashMap;

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {

        let mut hm_s1=HashMap::new();
        let mut hm_s2=HashMap::new();
        s1.chars().for_each(|c| *hm_s1.entry(c).or_insert(0)+=1);
        //println!("{:?}",hm_s1);

        let n1=s1.len();
        let n2=s2.len();
        
        if n1>n2 {return false;}
        
        let s2_c:Vec<char>=s2.chars().collect();

        for i in 0..n1 {
            *hm_s2.entry(s2_c[i]).or_insert(0) +=1;
        }
        if hm_s1==hm_s2 {return true}

        for i in n1..n2 {
            *hm_s2.entry(s2_c[i-n1]).or_insert(0) -=1;
            if hm_s2[&s2_c[i-n1]]==0 {
                hm_s2.remove(&s2_c[i-n1]);
            }
            
            *hm_s2.entry(s2_c[i]).or_insert(0) +=1;

            if hm_s1==hm_s2 {return true}
        }

        return hm_s1==hm_s2
    }
}

struct Solution {}
fn main() {
    println!("{}",Solution::check_inclusion("ab".to_string(), "eidbaooo".to_string()));
    println!("{}",Solution::check_inclusion("ab".to_string(), "eidboaoo".to_string()));
    println!("{}",Solution::check_inclusion("ab".to_string(), "a".to_string()));
}