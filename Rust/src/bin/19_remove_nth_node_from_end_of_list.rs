// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}
// 
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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, mut n: i32) -> Option<Box<ListNode>> {
      let old_head=head.clone();
      let n_head=head.unwrap();
      let d_val=n_head;

      while n>0 {
        n_head=n_head.next.as_mut().unwrap();
        n-=1
      }

      old_head
    }
}

struct Solution {}

fn main() {
  let values = vec![1, 2, 3, 4, 5];

  let mut dummy = ListNode::new(0);
  let mut current = &mut dummy;

  for &val in &values {
    current.next = Some(Box::new(ListNode::new(val)));
    current = current.next.as_mut().unwrap();
  }

  let l = dummy.next;    
  println!("{:?}",l);

  Solution::remove_nth_from_end(l, 2);


}