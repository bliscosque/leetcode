impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let l=matrix.len();
        let c=matrix[0].len();
        let size=l*c;
        //println!("{} {} {}", l, c, size);
        let mut i=0;
        let mut j=size-1;
        while i<=j {
            let half=(i+j)/2;
            let n_l=half/c;
            let n_c=half%c;
            let curr=matrix[n_l][n_c];
            //println!("{} {} {}", n_l, n_c, curr);
            if curr == target { 
                return true;
            }
            else if curr > target {
                //case with single elem
                if half==0 {
                    return false;
                }
                j=half-1;
            }
            else {
                i=half+1;
            }
        }
        return false;
    }
}

struct Solution{}
fn main() {
    println!("{}",Solution::search_matrix([[1,3,5,7].to_vec(),[10,11,16,20].to_vec(),[23,30,34,60].to_vec()].to_vec(), 3));
    println!("{}",Solution::search_matrix([[1,3,5,7].to_vec(),[10,11,16,20].to_vec(),[23,30,34,60].to_vec()].to_vec(), 13));
    println!("{}",Solution::search_matrix([[1].to_vec()].to_vec(), 0));
}