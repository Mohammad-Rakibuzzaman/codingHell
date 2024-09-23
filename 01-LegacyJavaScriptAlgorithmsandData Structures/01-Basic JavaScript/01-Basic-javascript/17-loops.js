// // Setup
// const myArray = [];

// // Only change code below this line

// let i = 5;
// while (i > -1) {
//   myArray.push(i);
//   i--;
// }
// console.log(myArray);

// // Setup
// const myArr = [2, 3, 4, 5, 6];

// // Only change code below this line
// let total = 0;

// for (let i = 0; i < myArr.length; i++) {
//   total += myArr[i];
// }

// console.log(total);

// const arr = [
//   [1, 2],
//   [3, 4],
//   [5, 6],
// ];

// for (let i = 0; i < arr.length; i++) {
//   for (let j = 0; j < arr[i].length; j++) {
//     console.log(arr[i][j]);
//   }
// }

// function multiplyAll(arr) {
//   let product = 1;
//   // Only change code below this line

//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < arr[i].length; j++) {
//       product *= arr[i][j];
//       console.log(product);
//     }
//   }

//   // Only change code above this line
//   return product;
// }

// console.log(
//   multiplyAll([
//     [1, 2],
//     [3, 4],
//     [5, 6, 7],
//   ])
// );

// function multiply(arr, n) {
//   let product = 1;
//   for (let i = 0; i < n; i++) {
//     product *= arr[i];
//   }
//   return product;
// }

// function multiply(arr, n) {
//   if (n <= 0) {
//     return 1;
//   } else {
//     return multiply(arr, n - 1) * arr[n - 1];
//   }
// }

// const arrayyy = [7, 2, 4, 5];
// console.log(multiply(arrayyy, 3));

function sum(arr, n) {
  // Only change code below this line

  if (n <= 0) {
    return 0;
  } else {
    return sum(arr, n - 1) + arr[n - 1];
  }

  // Only change code above this line
}
const arrayyy = [7, 2, 4, 5, 6];
console.log(sum(arrayyy, 3));
