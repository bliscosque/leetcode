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

bool isValidSudoku(vector<vector<char>>& board) {
    //validating line
    for (int i=0;i<9;i++) {
        set<char> s;
        for(int j=0;j<9;j++) {
            if (board[i][j]=='.') continue;
            if (s.count(board[i][j])>0) {
                //cout << "i: " << i << " j: " << j << " board: " << board[i][j] << endl;
                return false;
            }
            s.insert(board[i][j]);
        }
    }
    //validating column
    for (int j=0;j<9;j++) {
        set<char> s;
        for(int i=0;i<9;i++) {
            if (board[i][j]=='.') continue;
            if (s.count(board[i][j])>0) return false;
            s.insert(board[i][j]);
        }
    }
    //validating square
    for (int i=0;i<3;i++) {
        for (int j=0;j<3;j++) {
            //cout << endl;
            set<char> s;
            for (int k=0;k<3;k++) {
                for (int l=0;l<3;l++) {
                    int px=3*i+k;
                    int py=3*j+l;
                    if (board[px][py]=='.') continue;
                    // cout << "px: " << px << " py: " << py << " board: " << board[px][py] << endl;
                    if (s.count(board[px][py])>0) {
                        return false;
                    }
                    s.insert(board[px][py]);                    
                }
            }
        }
    }
    return true;
}

int main() {
    vector<vector<char>> board1 {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    cout << isValidSudoku(board1) << endl; //true

    vector<vector<char>> board2 {
        {'8','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    cout << isValidSudoku(board2) << endl; //false
    return 0;
}