#include <iostream>
#include <string>
#include <fstream>
#include <typeinfo>

using namespace std;

int main(int argc, char const *argv[])
{
    fstream myFile;

    cout << "=== PROGRAM TULIS DATA DAN BACA DATA ===" << endl;
    string data_input;

    while (true){
        string menu;
        cout << "Ketik 1 untuk input data" << endl;
        cout << "Ketik 2 untuk read data" << endl;
        cin >> menu;

        if(menu == "1"){
            cout << "==MASUKAN DATA INPUT==" << endl;
            cin >> data_input;
            myFile.open("data1.txt", ios::out);
            myFile << data_input << "\n";
        }

        string isLanjut;
        cout << "Lanjut? n/y";
        cin >> isLanjut;
        if (isLanjut == "n" || isLanjut == "N"){
            break;
        } else if (isLanjut == "y" || isLanjut == "Y"){
            continue;
        }
        
        
    }
    
}
