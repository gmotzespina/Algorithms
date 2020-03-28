const arrayToSearch = [1,3,2,5,7,9,11,3,5]


const mergeSort = (array) => {
 if (array.length > 2) {
  mergeSort(array.splice(0, array.length/2)); 
 }
}

const sortedArray = mergeSort(array);

console.log(arrayToSearch);
console.log(sortedArray);
