#include<stdio.h>

int main(){
    int n;
    int ele;
    int arr[100];
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        printf("Enter element: ");
        scanf("%d",&ele);
        arr[i]=ele;
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    printf("Second largest element: %d",arr[1]);
}
