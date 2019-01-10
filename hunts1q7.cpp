#include <iostream>
#include<vector>

using namespace std;
vector<int>v;
int a[1000000];

int main()
{
    long long n,x;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n;i++)
    {
        if(a[i]%2==0 and i%2!=0)
             v.push_back(a[i]);
        else if(a[i]%2!=0 and i%2==0)
                v.push_back(a[i]);
        //cout<<v[i];
    }
    for(int i=0;i<v.size();i++)
    {
        if(i!=(v.size()-1))
            cout<<v[i]<<" ";
        else cout<<v[i];
    }
}
