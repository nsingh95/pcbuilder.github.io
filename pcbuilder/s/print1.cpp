#include <iostream>
using namespace std;
int main()
{
  int n;
  cin >> n;
  for (int i = 1; i < n - i + 1; i++)
  {
    cout << " 88";
    for (int j = 0; j < 2 * n - 1; j++)
    {
      cout << "*" << n;
      for (int i = 1; i < n - i + 1; i++)
      {
        cout << "88 ";
      }
    }
    cout << " " << endl;
  }
  return 0;
}