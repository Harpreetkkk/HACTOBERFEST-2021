#include<iostream>
using namespace std;
class temperature{
    int lower,upper,step;
    float cel,fahr;
    public:
    void input(){
        cout<<"Enter lower value of temperature scale for celsius\n";
        cin>>lower;
        cout<<"Enter upper value of table\n";
        cin>>upper;
        cout<<"Enter increasing step for table\n";
        cin>>step;
    }
    void display(){
        cout<<"Fahrenheit  celsius\n";
        for(cel=lower;cel<=upper;cel+=step){
            fahr=(9/5)*(cel-32);
            cout<<""<<fahr<<"  "<<cel<<"\n";
        }
    }
};
int main(){
    temperature t;
    t.input();
    t.display();
    return 0;
}
