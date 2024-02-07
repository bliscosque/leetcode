use std::collections::BinaryHeap;

struct MinStack {
    els: Vec<i32>,
    els_heap: BinaryHeap<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        Self::new()
    }
    
    fn push(&self, val: i32) {
        self.els.push(val);
        self.els_heap.push(val);
    }
    
    fn pop(&self) {
        
    }
    
    fn top(&self) -> i32 {
        
    }
    
    fn get_min(&self) -> i32 {
        
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

}