#[derive(Debug)]
struct MinStack {
    els: Vec<StackElem>,
    
}
#[derive(Debug)]
struct StackElem {
    el: i32,
    min_el: i32,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        MinStack {
            els: Vec::new(),
        }
    }
    
    fn push(&mut self, val: i32) {
        let lmin=self.get_min();
        self.els.push( StackElem
            {el:val,
             min_el: lmin.min(val),
            }
        );
    }
    
    fn pop(&mut self) {
        self.els.pop();
        
    }
    
    fn top(&self) -> i32 {
        let last=self.els.get(self.els.len()-1).unwrap();
        return last.el;
    }
    
    fn get_min(&self) -> i32 {
        if self.els.len()==0 {return i32::MAX};
        let last=self.els.get(self.els.len()-1).unwrap();
        return last.min_el;
    }
}

/*
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */

fn main() {
    let mut ms=MinStack::new();
    ms.push(-2);
    ms.push(0);
    ms.push(-3);
    //println!("{:?}",ms);
    println!("{}",ms.get_min());
    ms.pop();
    println!("{}",ms.top());
    println!("{}",ms.get_min());
}