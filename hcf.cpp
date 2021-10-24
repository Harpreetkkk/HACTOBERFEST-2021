#include<iostream>
using namespace std;
class hcf{
    int a,b;
    public:
    void input(){
        cout<<"Enter two number\n";
        cin>>a>>b;
    }
    void display(){
        int c,d;
        for(c=1;c<=a||c<=b;c++){
            if(c%a==0 && c%b==0){
                d=c;
            }
        }
        cout<<"hcf is "<<((a*b)/d)<<"\n";
    }
};
int main(){
    hcf h;
    h.input();
    h.display();
    return 0;
}
