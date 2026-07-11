#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Включаем супер-скорость для ввода и вывода данных:
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int n = s.length();
   
    vector<int> pref(n+1,0);
    for (int i = 1;i <= n; i++){
        if (s[i-1] == '0'){
            pref[i] = pref[i-1] + 1;
        } else{
            pref[i] = pref[i-1];
        }
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
