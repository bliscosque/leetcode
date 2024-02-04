pub fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut ans=Vec::new();
    for el in tokens {
        match el.as_str() {
            "+"|"-"|"*"|"/" => {
                let l=ans.pop().unwrap();
                let ll=ans.pop().unwrap();
                match el.as_str() {
                    "+" => ans.push(l+ll),
                    "-" => ans.push(ll-l),
                    "*" => ans.push(l*ll),
                    "/" => ans.push(ll/l),
                    _ => {},
                }
                
            },
            _ => ans.push(el.parse().unwrap()),            
        }
    }
    ans[0]
}

fn main() {
    println!("{}",eval_rpn(["2".to_string(),"1".to_string(),"+".to_string(),"3".to_string(),"*".to_string()].to_vec())); //9
    println!("{}",eval_rpn(["4".to_string(),"13".to_string(),"5".to_string(),"/".to_string(),"+".to_string()].to_vec())); //6
}