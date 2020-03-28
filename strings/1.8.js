let zeroMatrix = [[1,0,4,5], [5,1,2,0], [2,2,3,4], [7,2,0,1], [0,8,9,1]];

console.log('Incomplete, check again later');
return

console.log(zeroMatrix);

const numberOfRows = zeroMatrix.length;
const numberOfColumns = zeroMatrix[0].length;

console.log('NumberOfRows: ', numberOfRows);
console.log('NumberOfColumns: ', numberOfColumns);

const changeToZeros = (row, column) => {

 console.log('row: ', row);
 console.log('column: ', column);


 for (let i = 0; i < numberOfColumns; i++){
   zeroMatrix[row][i] = 0;
 }
 
 for (let i = 0; i < numberOfRows; i++){
   zeroMatrix[i][column] = 0;
 }
 setTimeout(() => {},10000);
}

let rowNumber = 0;
let columnNumber = 0;
for (row of zeroMatrix) {
 for (number of row) {
  if (number === 0) {
   changeToZeros(rowNumber, columnNumber);
  }
  columnNumber += 1;
 }
 rowNumber += 1;
}

console.log(zeroMatrix);
