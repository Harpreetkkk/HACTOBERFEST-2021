#include<iostream>
using namespace std;
class reverse{
    int a,b,c;
    public:
    void input(){
        cout<<"Enter number\n";
        cin>>a;
    }
    void display(){
        c=0;
        while(a!=0){
            b=a%10;
            c=c*10+b;
            a/=10;
        };
        cout<<c;
    }
};
int main(){
    reverse r;
    r.input();
    r.display();
    return 0;
}
