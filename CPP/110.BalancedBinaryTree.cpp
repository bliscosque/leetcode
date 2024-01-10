#include <bits/stdc++.h>
using namespace std;
/*
    bool isBalanced(TreeNode* root) {
        if(root==nullptr) return true;
        return abs(height(root->left)-height(root->right))<=1 && isBalanced(root->left) && isBalanced(root->right);
    }
    int height(TreeNode*root){
        if(root==nullptr) return 0;
        return max(height(root->left),height(root->right))+1;
    }
*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

map<TreeNode*,pair<int,int>> m;

//calculate maxHeight (left and right) for all nodes
int calcHeight(TreeNode* root) {
    if (root==nullptr) return -1;
    int lH=1+calcHeight(root->left);
    int rH=1+calcHeight(root->right);
    pair<int,int> p1=make_pair(lH,rH);
    //cout << p1.first << " " << p1.second << " " << endl;
    m[root]=p1;
    return max(lH,rH);
}

void preOrderVisit(TreeNode* root) {
    if (root==nullptr) return;
    cout << root->val << " ";
    preOrderVisit(root->left);
    preOrderVisit(root->right);
}

bool isBalanced(TreeNode* root) {
    m.clear();
    calcHeight(root);
    int maxDif=0;
    for (auto entry: m) {
        auto el=entry.second;
        //cout << el.first << " " << el.second << endl;
        maxDif=max(maxDif,abs(el.first-el.second));
    }
    return maxDif<=1;
}

int main() {
    TreeNode *bt1 = new TreeNode(3,new TreeNode(9),new TreeNode(20,new TreeNode(15),new TreeNode(7)));
    //preOrderVisit(bt1);
    cout << isBalanced(bt1) << endl; //true

    TreeNode *bt2 = new TreeNode(1,new TreeNode(2,new TreeNode(3,new TreeNode(4),new TreeNode(4)),new TreeNode(3)),new TreeNode(2));
    //preOrderVisit(bt2);
    cout << isBalanced(bt2) << endl; //false

    TreeNode *bt3 = new TreeNode();
    //preOrderVisit(bt2);
    cout << isBalanced(bt3) << endl; //false

    return 0;
}