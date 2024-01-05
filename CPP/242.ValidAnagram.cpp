#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool isAnagram(string s, string t) {
    vector<char> v1(s.begin(),s.end());
    vector<char> v2(t.begin(),t.end());
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    return v1==v2;    
}

int main() {
    cout << isAnagram("anagram","nagaram") << endl; //true
    cout << isAnagram("rat","car") << endl; //false
    
    return 0;
}