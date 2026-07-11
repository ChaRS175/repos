#include <iostream>
#include <algorithm>
#include <chrono>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int x,y,z,t,v;
    cin >> x >> y >> z >> t >> v;
    auto start = chrono::high_resolution_clock::now();
    int tar_1 = x;
    int tar_2 = y * t;
    int tar_3 = z * v;

    cout << min({tar_1,tar_2,tar_3}) << '\n';
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;
    cout << "Время:" << duration << '\n';
    return 0;
}