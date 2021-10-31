#include<iostream>
using namespace std;
int factorial(int);
int main(){
    int a,b;
    cout<<"Enter number\n";
    cin>>a;
    if(a>=0){
    b=factorial(a);
    cout<<"Factorial is "<<b<<"\n";
    }
    else{
        cout<<"Negative number\n";
    }
    return 0;
}
int factorial(int a){
    if(a==0 || a==1)
    return 1;
    else 
    return a*factorial(a-1);
}
