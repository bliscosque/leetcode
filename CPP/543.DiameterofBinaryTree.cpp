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


map<TreeNode*,pair<int,int>> m;

void preOrderVisit(TreeNode* root) {
    if (root==nullptr) return;
    cout << root->val << " has heights: " << m[root].first << " and " << m[root].second << endl;
    preOrderVisit(root->left);
    preOrderVisit(root->right);
}

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

int diameterOfBinaryTree(TreeNode* root) {
    m.clear();
    calcHeight(root);
    //preOrderVisit(root);
    int maxDiam=0;
    for (auto entry: m) {
        auto el=entry.second;
        //cout << el.first << " " << el.second << endl;
        maxDiam=max(maxDiam,el.first+el.second);
    }
    return maxDiam;
}

int main() {
    TreeNode *bt1 = new TreeNode(1,new TreeNode(2,new TreeNode(4),new TreeNode(5)),new TreeNode(3));
    cout << diameterOfBinaryTree(bt1) << endl;

    return 0;
}