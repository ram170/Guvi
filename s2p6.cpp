#include <iostream>
#include <vector>
using namespace std;
vector<bool>a(10001,true);
vector<int>b;
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
    long n,m;
    prime();
    cin>>n>>m;
    for(int i=n+1;i<m;i++)
    {
        if(a[i])
        {
            b.push_back(i);
        }
    }
    for(int i=0;i<b.size();i++)
    {
        if(i!=(b.size()-1))
            cout<<b[i]<<" ";
        else cout<<b[i];
    }

}
