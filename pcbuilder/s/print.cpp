#include <iostream>
using namespace std;
void hold(int n)
 {
for(int i=0; i<n;i++){
    for (int j=0; j<n;j++){
        cout<<"$";
    }
    cout<<endl;
}}
int main()
{
    int n;
    cin>>n;
    hold(n);

}
