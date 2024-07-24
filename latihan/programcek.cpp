#include <iostream>
#include <array>

using namespace std;

int main(int argc, char const *argv[])
{
    array<int, 5> numberA = {1,2,3,4,5};
    array<int, 5> numberB = {1,2,3,4,5};

    numberA == numberB? cout << "True" << endl : cout << "False" << endl; 
    
    int arrayA[5] = {1,2,3,4,5};
    int arrayB[5] = {1,2,4,4,5};

    for (int i = 0; i < 5; i++){
        bool hasil = arrayA[i] == arrayB[i];
        if (hasil == false){
            break;
        }
        cout << "peti harta terbuka" << endl;
    }
    
        
    return 0;
}
