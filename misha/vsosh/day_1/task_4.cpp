#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Включаем супер-скорость для ввода и вывода данных:
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<long long> a(n);

    for (int i = 0;i < n;i++){
        cin >> a[i];
    }

    vector<long long> pref(n+1,0);
    for (int i = 1;i <= n ;i++){
        pref[i] = pref[i-1] + a[i-1];
    }

    int q;
    cin >> q;

    for (int i = 0;i < q;i++){
        int l,r;
        cin >> l >> r;

        long long result = pref[r+1] - pref[l];
        cout << result << '\n';
    }

    return 0;
}
