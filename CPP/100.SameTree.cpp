#include <bits/stdc++.h>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p==nullptr && q==nullptr) return true;
    else if (p==nullptr || q==nullptr) return false;
    else if (p->val != q->val) return false;
    else {
        bool left=isSameTree(p->left,q->left);
        bool right=isSameTree(p->right,q->right);
        return left && right;
    }
}

int main() {
    TreeNode *bt1 = new TreeNode(1,new TreeNode(2),new TreeNode(3));
    TreeNode *bt2 = new TreeNode(1,new TreeNode(2),new TreeNode(3));
    cout << isSameTree(bt1,bt2) << endl; // true

    TreeNode *bt3 = new TreeNode(1,new TreeNode(2),nullptr);
    TreeNode *bt4 = new TreeNode(1,nullptr,new TreeNode(2));
    cout << isSameTree(bt3,bt4) << endl; // false

    TreeNode *bt5 = new TreeNode(1,new TreeNode(2),new TreeNode(1));
    TreeNode *bt6 = new TreeNode(1,new TreeNode(1),new TreeNode(2));
    cout << isSameTree(bt5,bt6) << endl; // false
    
    return 0;
}