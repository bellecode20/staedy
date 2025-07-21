// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;  cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        int N;  cin >> N;
        vector<int> numbers(N);
        for (int& x : numbers) cin >> x;

        unordered_set<int> sums = {0};
        for (int num : numbers) {
            unordered_set<int> newsums;
            for (int s : sums) newsums.insert(s + num);
            sums.insert(newsums.begin(), newsums.end());
        }

        cout << '#' << tc << ' ' << sums.size() << '\n';
    }
    return 0;
}
