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

class Interval {
public:
    int start, end;
    Interval(int start, int end) {
        this->start = start;
        this->end = end;
    }
};

bool canAttendMeetings(vector<Interval>& intervals) {
    sort(intervals.begin(),intervals.end(),[] (Interval e1, Interval e2){return e1.start < e2.start;});
    int last=0;
    for (auto i:intervals) {
        if (i.start<last) return false;
        last=i.end;
    }
    return true;
}

int main() {
    vector<Interval> v1{Interval(0,30),Interval(5,10),Interval(15,20)};
    cout << canAttendMeetings(v1) << endl; //false

    vector<Interval> v2{Interval(5,8),Interval(9,15)};
    cout << canAttendMeetings(v2) << endl; //true

    return 0;
}