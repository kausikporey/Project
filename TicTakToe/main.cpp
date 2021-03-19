#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<windows.h>

using namespace std;
void disp(char arr[3][3]){
    cout<<"\t\tPLAYER1[X]\n\t\tPLAYER2[O]\n\n";
    cout<<"\t\t     |     |     \n";
    printf("\t\t  %c  |  %c  |  %c  \n",arr[0][0],arr[0][1],arr[0][2]);
    cout<<"\t\t_____|_____|_____\n";
    cout<<"\t\t     |     |     \n";
    printf("\t\t  %c  |  %c  |  %c  \n",arr[1][0],arr[1][1],arr[1][2]);
    cout<<"\t\t_____|_____|_____\n";
    cout<<"\t\t     |     |     \n";
    printf("\t\t  %c  |  %c  |  %c  \n",arr[2][0],arr[2][1],arr[2][2]);
    cout<<"\t\t     |     |     \n";
}
void choice(char arr[3][3],int pl,int x){
if(x == 1){
    switch(pl){
    case 1:
        arr[0][0] = 'X';
        break;
    case 2:
        arr[0][1] = 'X';
        break;
    case 3:
        arr[0][2] = 'X';
        break;
    case 4:
        arr[1][0] = 'X';
        break;
    case 5:
        arr[1][1] = 'X';
        break;
    case 6:
        arr[1][2] = 'X';
        break;
    case 7:
        arr[2][0] = 'X';
        break;
    case 8:
        arr[2][1] = 'X';
        break;
    case 9:
        arr[2][2] = 'X';
    }
}
if(x == 2){
    switch(pl){
    case 1:
        arr[0][0] = 'O';
        break;
    case 2:
        arr[0][1] = 'O';
        break;
    case 3:
        arr[0][2] = 'O';
        break;
    case 4:
        arr[1][0] = 'O';
        break;
    case 5:
        arr[1][1] = 'O';
        break;
    case 6:
        arr[1][2] = 'O';
        break;
    case 7:
        arr[2][0] = 'O';
        break;
    case 8:
        arr[2][1] = 'O';
        break;
    case 9:
        arr[2][2] = 'O';
    }
  }
}
int check(char arr[3][3]){
  if((arr[0][0]=='X'&&arr[0][1]=='X'&&arr[0][2]=='X')||(arr[1][0]=='X'&&arr[1][1]=='X'&&arr[1][2]=='X')||(arr[2][0]=='X'&&arr[2][1]=='X'&&arr[2][2]=='X')||(arr[0][0]=='X'&&arr[1][1]=='X'&&arr[2][2]=='X')||(arr[0][2]=='X'&&arr[1][1]=='X'&&arr[2][1]=='X')||(arr[0][1]=='X'&&arr[1][1]=='X'&&arr[2][1]=='X')){
        cout<<"\t\t *****  G A M E   O V E R  *****\n";
        cout<<"Player 1 Wins the Game\n";
        return 1;
  }
if((arr[0][0]=='O'&&arr[0][1]=='O'&&arr[0][2]=='O')||(arr[1][0]=='O'&&arr[1][1]=='O'&&arr[1][2]=='O')||(arr[2][0]=='O'&&arr[2][1]=='O'&&arr[2][2]=='O')||(arr[0][0]=='O'&&arr[1][1]=='O'&&arr[2][2]=='O')||(arr[0][2]=='O'&&arr[1][1]=='O'&&arr[2][1]=='O')||(arr[0][1]=='O'&&arr[1][1]=='O'&&arr[2][1]=='O')){
        cout<<"\t\t *****  G A M E   O V E R  *****\n";
        cout<<"Player 2 Wins the Game\n";
        return 1;
  }
}



int main(){
    char arr[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
    int player1,player2;
    system("cls");
    cout<<"\n\t ******** T  I  K      T  A  K    T  O  E ********\n\n";
    disp(arr);
    for(int i=0;i<4;i++){
    cout<<"Player 1 Turn : \n";
    cin>>player1;
    choice(arr,player1,1);
    disp(arr);
    if(i>=2){
       int c = check(arr);
    }
    cout<<"Player 2 Turn : \n";
    cin>>player2;
    choice(arr,player2,2);
    disp(arr);
    if(i>=2){
     int c = check(arr);
    }
}
    cout<<"Player 1 Turn : \n";
    cin>>player1;
    choice(arr,player1,1);
    disp(arr);
    check(arr);
    cout<<"\t\t *****  M A T C H   T I E D  *****\n";
}

