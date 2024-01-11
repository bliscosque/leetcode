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

void preOrderVisit(TreeNode* root) {
    if (root==nullptr) return;
    cout << root->val << " ";
    preOrderVisit(root->left);
    preOrderVisit(root->right);
}


bool isSameTree(TreeNode* p, TreeNode* q) {
    // cout << "Testing" << endl;
    // preOrderVisit(p);
    // cout << endl;
    // preOrderVisit(q);
    // cout << endl;

    if (p==nullptr && q==nullptr) return true;
    else if (p==nullptr || q==nullptr) return false;
    else if (p->val != q->val) return false;
    else {
        bool left=isSameTree(p->left,q->left);
        bool right=isSameTree(p->right,q->right);
        return left && right;
    }
}

bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    if (root==nullptr) return false;
    if (root->val==subRoot->val) {
        if (isSameTree(root,subRoot)) return true;
    }
    return isSubtree(root->left,subRoot) || isSubtree(root->right,subRoot);
}

int main() {
    TreeNode *bt1 = new TreeNode(3,new TreeNode(4,new TreeNode(1),new TreeNode(2)),new TreeNode(5));
    TreeNode *bt2 = new TreeNode(4,new TreeNode(1),new TreeNode(2));
    cout << isSubtree(bt1,bt2) << endl; // true

    TreeNode *bt3 = new TreeNode(3,new TreeNode(4,new TreeNode(1),new TreeNode(2,new TreeNode(0),nullptr)),new TreeNode(5));
    TreeNode *bt4 = new TreeNode(4,new TreeNode(1),new TreeNode(2));
    cout << isSubtree(bt3,bt4) << endl; // false

    TreeNode *bt5 = new TreeNode(1,new TreeNode(1),nullptr);
    TreeNode *bt6 = new TreeNode(1);
    cout << isSubtree(bt5,bt6) << endl; // true
    
    return 0;
}