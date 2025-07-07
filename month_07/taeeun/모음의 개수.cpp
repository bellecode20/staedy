// https://www.acmicpc.net/submit/10807

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int v;
    cin >> v;

    int res = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == v) res++;
    }

    cout << res << '\n';
    return 0;
}
