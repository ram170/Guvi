#include <iostream>
#include<set>

using namespace std;
int b[1000000];

int main()
{
    set<int>s;
    long long n,m,u=0,temp=0,x;
    cin>>n>>m;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        s.insert(x);
    }
    for(int j=0;j<m;j++)
        cin>>b[j];
    for(int i=0;i<m;i++)
    {
        temp=s.size();
        s.insert(b[i]);
        if(s.size()==temp)
            u++;
    }
    if(u==m)
        cout<<"YES";
    else cout<<"NO";

}
