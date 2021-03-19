#include <iostream>
#include<windows.h>
#include<stdio.h>
#include<conio.h>

using namespace std;

int main()
{
    int h,m,s;
    cout<<"Enter Current Hour : "<<endl;
    cin>>h;
    cout<<"Enter Current Minute : "<<endl;
    cin>>m;
    cout<<"Enter Current Second : "<<endl;
    cin>>s;
    while(true){
        system("cls");
        printf("%d : %d : %d",h,m,s);
        Sleep(1000);
        s++;
        if(s>59){
            s = 0;
            m++;
        }
        if(m>59){
            m = 0;
            h++;
        }
        if(h>23){
            h = 0;
        }
    }
}
