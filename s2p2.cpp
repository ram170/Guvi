#include <iostream>
#include <vector>
using namespace std;
vector<bool>a(10001,true);
void prime()
{
    for(int i=2;i*i<10001;i++)
    {
        if(a[i])
        for(int j=i*i;j<=10001;j+=i)
        a[j]={false};

    }
}
int main()
{
    long n;
    prime();
    cin>>n;
    if(a[n]==true)
        cout<<"yes";
    else cout<<"no";
}
