#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Включаем супер-скорость для ввода и вывода данных:
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    int x;
    cin >> n;
    cin >> x;

    vector<long> a(n);
    for (int i = 0;i < n;i++){
        cin >> a[i];
    }

    sort(a.begin(),a.end());
    
    int l,r;
    l = 0;
    r = n-1;
    bool found = false;

    while (l < r){
        if (a[l] + a[r] == x){
            cout << a[l] << ' ' << a[r] << '\n';
            found = true;
            break;
        }
        else if (a[l] + a[r] > x){
            r--;
        }
        else {
            l++;
        }
    }
    if (!found){
        cout << -1;
    }


    return 0;
}
