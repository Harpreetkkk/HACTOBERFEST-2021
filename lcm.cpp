#include<iostream>
using namespace std;
class lcm{
    int a,b;
    public:
    void input(){
        cout<<"Enter two numbers\n";
        cin>>a>>b;
    }
    void display(){
        int c,d;
        for(c=1;c<=a || c<=b;c++){
            if(a%c==0 && b%c==0){
                d=c;
            }
        };
        cout<<"lcm is "<<((a*b)/d)<<"\n";
    }
};
int main(){
    lcm h;
    h.input();
    h.display();
    return 0;
} 
