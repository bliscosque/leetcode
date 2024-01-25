#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec) {
    os << "[";
    if (!vec.empty()) {
        // Print the first element outside the loop to avoid a trailing comma
        os << vec[0];

        // Print the rest of the elements with a comma separator
        for (size_t i = 1; i < vec.size(); ++i) {
            os << ", " << vec[i];
        }
    }
    os << "]";
    return os;
}

// --------------------------------------------------------------- //

string encode(vector<string>& strs) {
    string ans="";
    for (string s:strs) {
        string n=to_string(s.length());
        n=string(3-n.length(),'0')+n;

        ans.append(n);
        ans.append(s);
    }
    return ans;
}

vector<string> decode(string s) {
    vector<string> ans{};
    while (s!="") {
        string n=s.substr(0,3);
        n.erase(0, std::min(n.find_first_not_of('0'), n.size()-1)); //remove leading 0
        if (n=="") n="0";
        int ni=stoi(n);
        string found_string=s.substr(3,ni);
        s=s.substr(3+ni);
        ans.push_back(found_string);
    }
    return ans;
}

int main() {
    vector<string> t1{"neet","code","love","you"};
    string e1=encode(t1);
    //cout << e1 << endl;
    cout << decode(e1) << endl;

    vector<string> t2{"we","say",":","yes"};
    string e2=encode(t2);
    cout << decode(e2) << endl;

    return 0;
}