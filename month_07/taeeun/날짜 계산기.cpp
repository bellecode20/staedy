// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq
#include <iostream>
#include <array>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) return 0;

   
    const array<int, 13> days = {
        0,  
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    };

    for (int tc = 1; tc <= T; ++tc) {
        int am, ad, bm, bd;       
        cin >> am >> ad >> bm >> bd;

        long long total = 0;        

        if (am == bm) {
            total = bd - ad + 1;    
        } else {
            total += days[am] - ad + 1; 
            for (int m = am + 1; m < bm; ++m)
                total += days[m];      
            total += bd;                
        }

        cout << '#' << tc << ' ' << total << '\n';
    }
    return 0;