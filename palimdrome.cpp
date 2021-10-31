#include<iostream>
using namespace std;
class palimdrome{
    int a,b,c;
    public:
    void input(){
        cout<<"Enter number\n";
        cin>>a;
        while(a!=0){
            b=a%10;
            c=c*10+b;
            a/=10;
        };
    }
    void output(){
        if(c!=a){
            cout<<"It is a palimdrome\n";
        }
        else{
            cout<<"Not a palimdrome\n";
        }
    }
};
int main(){
    palimdrome p;
    p.input();
    p.output();
    return 0;
}
