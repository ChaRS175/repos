#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Включаем супер-скорость для ввода и вывода данных:
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long w,h,n;
    cin >> w >> h >> n;

    long long l,r;
    l = 1;
    r = 2000000000000000000LL;
    long long answ = 0;
    while (l <= r){
        long long mid = l + (r - l) / 2;
        long long max_dips_w = mid / w;
        long long max_dips_h = mid / h;

        if (max_dips_w >= n || max_dips_h >= n){
            answ = mid;
            r = mid - 1;
        }
        else if (max_dips_w * max_dips_h >= n){
            answ = mid;
            r = mid - 1;
        }
        else{
            l = mid + 1;
        }
        

    }

    cout << answ << '\n';
    return 0;
}
