#include <iostream>
#include<set>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    long long n,x,t=0,u=0;
    set<int>s;
    vector<int>v;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        t=s.size();
        s.insert(x);
        if(s.size()==t)
            v.push_back(x);

    }
    if(v.size()>0)
    {
        sort(v.begin(),v.end());
        u=v[0];
        for(int i=0;i<v.size();i++)
        {
            if(i!=0 && u!=v[i])
            {
            cout<<v[i]<<" ";
            u=v[i];
            }
            if(i==0)
            cout<<v[i]<<" ";
        }
    }
    else cout<<"unique";
    return 0;
}
