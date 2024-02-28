// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}
 
impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
      let (mut prev,mut cur)=(None,head);
      while let Some(mut node) = cur {
        cur=node.next;
        node.next=prev;
        prev=Some(node);
      }
      prev
    }
}

struct Solution {}

fn main() {
    let values=vec![1,2,3,4,5];
    let mut dummy=ListNode::new(0);
    let mut current=&mut dummy;
    for &val in &values {
        current.next=Some(Box::new(ListNode::new(val)));
        current=current.next.as_mut().unwrap();
    }
    let l1=dummy.next;
    println!("{:?}",l1);
    
    println!("{:?}",Solution::reverse_list(l1));
}