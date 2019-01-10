#include <iostream>
#include<vector>

using namespace std;
vector<int>v;

int main()
{
    long long n,x;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        if(x%2==0 and i%2!=0)
             v.push_back(x);
        else if(x%2!=0 and i%2==0)
                v.push_back(x);
        //cout<<v[i];
    }
    for(int i=0;i<v.size();i++)
    {
        if(i!=(v.size()-1))
            cout<<v[i]<<" ";
        else cout<<v[i];
    }
}
