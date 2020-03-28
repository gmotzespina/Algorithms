const array = [1, 3, 4, 5, 8, 9 ,12, 14];

const binarySearch = (elementToSearch, array) => {
 console.log('Current Arrray: ', array); 
 if (!array) { 
  console.log('Element doesnt exist');
  return;
 }
 
 if (array.length == 1 && array[0] === elementToSearch) {
  console.log('Element found at position 0');
  return; 
 }
 
 const halfArrayIndex = array.length/2;
 
 if (array[halfArrayIndex] === elementToSearch) {
  console.log(`Element found at index ${halfArrayIndex}`);
  return;
 } 

 if (array[halfArrayIndex] > elementToSearch) {
  binarySearch(elementToSearch, array.slice(0, array.length/2));
 } else {
  binarySearch(elementToSearch, array.slice(halfArrayIndex, array.length));
 }

}

binarySearch(3, array);

