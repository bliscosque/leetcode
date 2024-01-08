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

TreeNode* invertTree(TreeNode* root) {
    if (root==nullptr) return nullptr;
    swap(root->right,root->left);
    invertTree(root->right);
    invertTree(root->left);
    return root;
}


int main() {
    TreeNode *bt1 = new TreeNode(2,new TreeNode(1),new TreeNode(3));
    //preOrderVisit(bt1);
    bt1=invertTree(bt1);
    preOrderVisit(bt1);

    cout << endl;

    TreeNode *bt2 = new TreeNode(4,new TreeNode(2,new TreeNode(1),new TreeNode(3)),new TreeNode(7,new TreeNode(6),new TreeNode(9)));
    //preOrderVisit(bt2);
    bt2=invertTree(bt2);
    preOrderVisit(bt2);
    
    return 0;
}