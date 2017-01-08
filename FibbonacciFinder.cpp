//lab9_1_Weinstein.cpp

#include <iostream>
#include <vector>

using namespace std;

int n;
void fib_fill(vector<int> & fibbo, int n);
int main()
{
    vector<int> fibbo; //array to hold fibbonacci numbers
    cout << "How many fibbonacci numbers would you like to find? ";  //getuser input
    cin >> n;
    fib_fill(fibbo, n); //fill fibbonacci array
    int i;
    for(i=0; i<n; i++)
    {
        cout << "Fib #" << i+1 << ": " << fibbo[i] << endl; //Display fibbonacci sequence
    }
    
    return 0;
}

void fib_fill(vector<int> & fibbo, int n)  //for calculating the fibbonacci sequence
{
    int i;
    fibbo.push_back(0);
    fibbo.push_back(1);
    int fib1 = 0; //set first two fibbonacci numbers
    int fib2 = 1;
    int fib;
    for(i = 2; i < n; i++) //calculate up to specified value
    {
        fib = fib1 + fib2;
        fibbo.push_back(fib);
        fib1 = fib2;
        fib2 = fib;
    }
}
