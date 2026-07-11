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
    long long max_val = -2e9;
    long max_idx = -1;
    vector<long long> a(n);

    for (int i = 0;i < n; i++){
        cin >> a[i];
        
        if (a[i] > max_val){
            max_val = a[i];
            max_idx = i;
        }
    }

    cout << max_val << '\n';
    cout << max_idx << '\n';




    return 0;
}
