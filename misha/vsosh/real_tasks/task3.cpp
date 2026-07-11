#include <iostream>
#include <algorithm>
#include <chrono>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int a,b;
    cin >> a >> b;
    auto start = chrono::high_resolution_clock::now();
    int x,y;
    x = 0;
    y = 0;

    bool step_x = (a >= b);
    while (x != a || y != b){
        if (step_x){
            if (x < a){
                x++;
                cout << x << " " << y << "\n";
            }
            else if(x > a){
                x--;
                cout << x << " " << y << "\n";
            }
            else {
                if(x > 0){
                    x--;
                    cout << x << " " << y << "\n";
                }
                else{
                    x++;
                    cout << x << " " << y << "\n";
                }
            }
        }
        else {
            if(y < b){
                y++;
                cout << x << " " << y << "\n";
            }
            else if(y > b){
                y--;
                cout << x << " " << y << "\n";
            }
            else{
                if(y > 0){
                    y--;
                    cout << x << " " << y << "\n";
                }
                else{
                    y++;
                    cout << x << " " << y << "\n";
                }
            }

        }
        step_x = !step_x;
    }
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> duration = end - start;
    cout << "Время:" << duration << '\n';
    return 0;
}