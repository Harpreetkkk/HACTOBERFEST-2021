#include<iostream>
using namespace std;
class bank{
    int account_number;
    char name[100];
    int amount;
    int deposite;
    int withdrawe;
    public:
    void input(){
        cout<<"Enter name\n";
        cin>>name;
        cout<<"Enter account_number\n";
        cin>>account_number;
        cout<<"Enter initial amount\n";
        cin>>amount;
    }
    void deposit(){
        cout<<"Enter amount to be deposited\n";
        cin>>deposite;
    }
    void withdraw(){
        cout<<"Enter amount to be withdrawed\n";
        cin>>withdrawe;
    }
    void display1(){
        cout<<"Name            ->     "<<name<<"\n";
        cout<<"Account No.     ->     "<<account_number<<"\n";
        cout<<"Initial amount  ->     "<<amount<<"\n";
        cout<<"Amount deposited->     "<<deposite<<"\n";
        cout<<"Total amount    ->     "<<(amount+deposite)<<"\n";
    }
    void display2(){
        cout<<"Name            ->     "<<name<<"\n";
        cout<<"Account No.     ->     "<<account_number<<"\n";
        cout<<"Initial amount  ->     "<<amount<<"\n";
        cout<<"Amount withdrwed->     "<<withdrawe<<"\n";
        cout<<"Total amount    ->     "<<(amount-withdrawe)<<"\n";
    }
};
int main(){
    bank b;
    int a;
    cout<<"1-Deposit\n";
    cout<<"2-withdraw\n";
    cin>>a;
    b.input();
    switch(a){
        case 1:
        b.deposit();
        b.display1();
        break;
        case 2:
        b.withdraw();
        b.display2();
        break;
        default:
        cout<<"No match to your selection\n";
        break;
    }
    return 0;
}
