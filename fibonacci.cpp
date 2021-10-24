#include<iostream>
using namespace std;
class fibo{
    int a,b,c,d;
    public:
    void input(){
        cout<<"Enter number\n";
        cin>>a;
    }
    int fib(int e){
        if(e==0)
        return 0;
        else if(e==1)
        return 1;
        else {
            return (fib(e-1)+fib(e-2));
        }
    }
    void display(){
        d=0;
        for(b=0;b<=a;b++){
            c=fib(b);
            d+=c;
            cout<<""<<c<<"\n";
        }
        cout<<"sum is "<<d<<"\n";
    }
};
int main(){
    fibo f;
    f.input();
    f.display();
    return 0;
}
