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
    vector<long long> a(n); // создание динамического массива

    // Ошибка 1 исправлена: знак изменен на <
    for (int i = 0; i < n; i++){ // заполнение массива
        cin >> a[i];
    }

    // Ошибка 2 исправлена: размер изменен на n + 1
    vector<long long> pref(n + 1, 0); // создание массива префиксных сумм

    // Ошибка 1 и 3 исправлены: знак изменен на <=, чтобы дойти до конца
    for (int i = 1; i <= n; i++){ // заполнение префиксов
        pref[i] = pref[i-1] + a[i-1];
    }

    int q; // обработка запросов
    cin >> q;

    for (int i = 0; i < q; i++){ 
        int l, r;
        cin >> l >> r;

        long long result = pref[r+1] - pref[l];
        cout << result << '\n';
    }

    return 0;
}
