#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	int edad = 25;
    float precio = 99.99;
    string nombre = "Leay";
    
    if (edad > 18 && precio < 100) {
        cout << "Hola " << nombre << endl;
        cout << "Mundo" << endl;
		cout << "Como estamosS" << endl;


    }
    
    for(int i = 0; i < 5; i++) {
        cout << "Numero: " << i << endl;
    }
	
	return 0;
}
