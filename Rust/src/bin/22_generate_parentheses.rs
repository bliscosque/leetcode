//acceted but has some performance issues

pub fn generate_parenthesis(n: i32) -> Vec<String> {
    let mut ans:Vec<String>=Vec::new();
    generate_parenthesis_int(2*n, &mut ans, "".to_string(),0);
    ans
}

pub fn generate_parenthesis_int(n: i32, ans:&mut Vec<String>, p:String,opencnt:i32) {
    if n==0 && opencnt==0 {
        ans.push(p.clone())
    }
    //op1 = (
    if n>=1 {
        generate_parenthesis_int(n-1, ans, p.clone()+"(",opencnt+1);
    }    
    //op2 = )
    if n>=1 && opencnt >=1 {
        generate_parenthesis_int(n-1, ans, p.clone()+")",opencnt-1);
    }
}

fn main() {
    println!("{:?}",generate_parenthesis(3));
    println!("{:?}",generate_parenthesis(1));
}