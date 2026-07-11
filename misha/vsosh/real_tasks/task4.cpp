#include <iostream>
#include <algorithm>
#include <chrono>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<long long> a(n);

    for (int i = 0;i < n;i++){
        cin >> a[i];
    }

    sort(a.begin(),a.end());
    int ans = 0;
    for (int k = 1;k <= n;k++){
        if (a[n-k] >= k){
            ans = k;
        }
        else{
            ans = k-1;
            break;
        }
    }

    cout << ans << '\n';
    return 0;
}