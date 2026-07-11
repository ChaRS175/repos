#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Включаем супер-скорость для ввода и вывода данных:
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,m;
    cin >> n >> m;

    vector<vector<int>> a(n);
    int u,v;
    for (int i = 0;i < m;i++){
        cin >> u >> v;

        a[u].push_back(v);
        a[v].push_back(u);
    }

    for (int i = 0;i < n;i++){
        cout << i << ' ' << a[i].size() << '\n';
    }

    
    return 0;
}
