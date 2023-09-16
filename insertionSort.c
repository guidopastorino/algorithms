void insertionSort(int arr[], int size){
  for(int i = 0; i<size; i++){
    int key = arr[i];
    int j = i - 1;

    while(j >= 0 && key < arr[j]){
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}