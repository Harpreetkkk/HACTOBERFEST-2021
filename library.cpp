#include<iostream>
using namespace std;
class library{
    int id;
    char name[100];
    char book[100];
    float price;
    public:
    void input(){
        cout<<"Enter name of author\n";
        cin>>name;
        cout<<"Enter book name\n";
        cin>>book;
        cout<<"Enter id\n";
        cin>>id;
        cout<<"Enter price\n";
        cin>>price;
    }
    void display(){
        cout<<"Author Name:- "<<name<<"\n";
        cout<<"Book name:- "<<book<<"\n";
        cout<<"Id:- "<<id<<"\n";
        cout<<"Price:-"<<price<<"\n";
    }
};
int main(){
    library l;
    l.input();
    l.display();
    return 0;
}
