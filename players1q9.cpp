#include <iostream>
#include<vector>
using namespace std;
#define c 10000
vector<bool>a(c,true);
void def()
{
    for(int i=2;i*i<=c;i++)
        if(a[i])
        for(int j=2*i;j<=c;j=j+i)
        a[j]=false;
}

int main()
{
    long n,m,u=0;
   def();
   cin>>n>>m;
   for(int i=n;i<=m;i++)
   {
      // cout<<a[i];
    if(a[i])
     u++;
   }
  cout<<u;
  return 0;

}
