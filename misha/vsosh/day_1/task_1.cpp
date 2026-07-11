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
    
    long long sum = 0;

    vector<int> a(n);
    for (int i = 0;i < n;i++){
        cin >> a[i];

        if (a[i] % 2 == 0){
            sum += a[i];
        }
    }

    cout << sum << '\n';
    return 0;
}
