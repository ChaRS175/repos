#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Включаем супер-скорость для ввода и вывода данных:
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,x;
    cin >> n >> x;

    vector<long long> a(n);
    for (int i = 0;i < n;i++){
        cin >> a[i];
    }
    bool found = false;
    int l = 0;
    int r = n - 1;
    while (l <= r){
        
        int mid = l + (r - l) / 2;

        if (a[mid] == x){
            cout << mid << '\n';
            found = true;
            break;
        } 
        else if (a[mid] < x){
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }

    if (!found){
        cout << -1 << '\n';
    }
    return 0;
}
