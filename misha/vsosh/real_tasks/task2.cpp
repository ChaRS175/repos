#include <iostream>
#include <algorithm>
#include <chrono>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long a,b,c;
    cin >> a >> b >> c;
    auto start = chrono::high_resolution_clock::now();
    long long strangers = b + c;

    if (strangers >= a) {
        cout << a + (a / 2) << '\n';
    }
    else{
        cout << strangers + a << '\n';
    }

    
    
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;
    cout << "Время:" << duration << '\n';
    return 0;
}