use std::collections::btree_map::Keys;
use std::collections::HashMap;
use std::collections::BTreeMap;

#[derive(Debug)]
struct TimeMap {
    els: HashMap<String,BTreeMap<i32,String>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {

    fn new() -> Self {
        Self {
            els: HashMap::new()
        }
    }
    
    fn set(&mut self, key: String, value: String, timestamp: i32) {
        if self.els.contains_key(&key) {
            self.els.get_mut(&key).unwrap().insert(timestamp,value);
        }
        else {
            self.els.insert(key.clone(), BTreeMap::new());
            self.els.get_mut(&key).unwrap().insert(timestamp,value);
        }
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        if ! self.els.contains_key(&key) {
            return "".to_string();
        }
        let el = self.els.get(&key).unwrap();
        let mut interv = el.range(..=timestamp);
        if let Some((k, v)) = interv.next_back() {
            // println!("Chave: {}, Valor: {}", k, v);
            return v.to_string();
        }
        "".to_string()
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */

fn main() {
    let mut s=TimeMap::new();
    s.set("foo".to_string(), "bar".to_string(), 1);
    println!("{}",s.get("foo".to_string(),1));
    println!("{}",s.get("foo".to_string(),3));
    s.set("foo".to_string(),"bar2".to_string(),4);
    println!("{}",s.get("foo".to_string(),4));
    println!("{}",s.get("foo".to_string(),5));

    println!();

    let mut s2=TimeMap::new();
    s2.set("a".to_string(),"bar".to_string(),1);
    s2.set("x".to_string(),"b".to_string(),3);
    println!("{}",s2.get("b".to_string(),3));
    s2.set("foo".to_string(),"bar2".to_string(),4);
    println!("{}",s2.get("foo".to_string(),4));
    println!("{}",s2.get("foo".to_string(),5));

}