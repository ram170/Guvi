#include <iostream>
#include<set>

using namespace std;

int main()
{
    long long n,x,t;
    long long a='\0';
    set<long>s;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        t=s.size();
        s.insert(x);
        if(s.size()==t && a=='\0')
                a=x;
    }
    if(a!='\0')
        cout<<a;
    else cout<<"unique";

}
