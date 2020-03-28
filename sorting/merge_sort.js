const mergeSort = (array) => {
 const arrayLength = array.length;
 let leftHalf = array.slice(0, arrayLength/2);
 let rightHalf = array.slice(arrayLength/2, arrayLength);
 if (arrayLength === 1){
  return array;
 } 
 leftHalf = mergeSort(leftHalf); 
 rightHalf = mergeSort(rightHalf);

 return merge(leftHalf, rightHalf); 
}

const merge = (leftHalf, rightHalf) => {
 let mergedArray = [];
 while (leftHalf.length > 0 && rightHalf.length > 0) {
  if (leftHalf[0] > rightHalf[0]) {
   mergedArray.push(rightHalf[0]);
   rightHalf.shift();
  } else {
   mergedArray.push(leftHalf[0]);
   leftHalf.shift();
  }
 }

 mergedArray = [...mergedArray, ...rightHalf, ...leftHalf];
 return mergedArray;
}

const arrayToSort = [2,1,3,7,9,8,4];

console.log('Array to sort: ', arrayToSort);
const sortedArray = mergeSort(arrayToSort);
console.log('Sorted array: ',sortedArray);
