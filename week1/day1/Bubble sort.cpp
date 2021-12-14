#include<iostream>
#include<stdlib.h>
using namespace std;


void swape(int& a, int& b){
    int temp=a;
    a=b;
    b=temp;
}

void countSwaps(int a[],int n) {

int counter=0;


for(int i=0; i<n; i++){

    for(int j=0; j<n-i; j++)

        if(a[j] > a[j+1]){
         swape(a[j],  a[j+1]);

         counter++;
        }


}

cout<<"Array is sorted in "<<counter<<" swaps.\n";
cout<<"First Element: "<<a[0]<<"\n";
cout<<"Last Element: "<<a[n-1];


}

int main(){
int n;
cin>>n;
int a[n];
for(int i=0; i<n;i++)
  cin>>a[i];


countSwaps(a,n);

}
