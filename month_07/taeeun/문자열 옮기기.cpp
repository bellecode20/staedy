// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZPOBiaqNo8DFAWB
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string left_rotate(const string& src, int s) {
    int n = static_cast<int>(src.size());
    if (n == 0 || s == 0) return src;
    return src.substr(s) + src.substr(0, s);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;                   
    if (!(cin >> T)) return 0;

    while (T--) {
        string M;         
        cin >> M;
        int L = static_cast<int>(M.size());

        int K;         
        cin >> K;
        vector<long long> commands(K);
        for (auto& x : commands) cin >> x;

        long long net_shift = 0;          
        for (long long x : commands) net_shift += x;

        int s = static_cast<int>((net_shift % L + L) % L);

        cout << left_rotate(M, s) << '\n';
    }
    return 0;
}