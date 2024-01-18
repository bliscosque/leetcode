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

uint32_t reverseBits(uint32_t n) {
    //bitset<32> binaryRepresentationn(n);
    //cout << "Bin n: " << binaryRepresentationn << endl;
    uint32_t ans=n|(n&1);
    n=n>>1;
    for (int i=1;i<32;i++) {
        ans=ans<<1;
        ans = ans | (n&1);
        n=n>>1;
    }
    //bitset<32> binaryRepresentation(ans);
    //cout << "Bin ans: " << binaryRepresentation << endl;
    return ans;
}

int main() {
    cout << reverseBits(43261596) << endl; //00000010100101000001111010011100 => 00111001011110000010100101000000 (964176192)
    cout << reverseBits(4294967293) << endl; // 11111111111111111111111111111101 => 10111111111111111111111111111111 (3221225471)
    return 0;
}