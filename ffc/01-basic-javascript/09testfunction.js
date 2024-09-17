// function testFun(param1, param2) {
//     console.log(param1, param2);
// }

// testFun("Hi", "Invoker!");
// testFun("Hi", "Lion!");
// testFun("Hi", "Axe!");


// function functionWithArgs(a, b) {
  
//     console.log(a + b);
  
// }


// function timesFive(mul){
//     return mul * 5;
// }
  
// const valueOne = timesFive(3);
  
// console.log(valueOne)



// Declare the myGlobal variable below this line
let myGlobal = 10;

function fun1() {
  // Assign 5 to oopsGlobal here
  oopsGlobal = 5;
  return oopsGlobal;
}

// Only change code above this line

// function fun2() {
//   let output = "";
//   if (typeof myGlobal != "undefined") {
//     output += "myGlobal: " + myGlobal;
//   }
//   if (typeof oopsGlobal != "undefined") {
//     output += " oopsGlobal: " + oopsGlobal;
//   }
//   console.log(output);
// }


// fun2()

// var gg = fun1()
// console.log(typeof gg)


// function myTest() {
//     const loc = "foo";
//     console.log(loc);
//   }
  
// myTest();
// console.log(loc);


// //local scope
// function myLocalScope() {
//     // Only change code below this line
//     let myVar;
//     console.log('inside myLocalScope', myVar);
// }
// myLocalScope();
  
// // myVar is not defined outside of myLocalScope
// // Run and check the console
// console.log('outside myLocalScope', myVar);



// Setup
// const outerWear = "T-Shirt";

// function myOutfit() {
//   // Only change code below this line
//   const outerWear = "sweater";
//   // Only change code above this line
//   return outerWear;
// }

// console.log(outerWear)
// console.log(myOutfit());



// var createHelloWorld = function() {
    
//     return function(...args) {
//         return "Hello World"
//     }       
// };

// const f = createHelloWorld()
// console.log(f())



// let sum = 0;

// function addSum(num) {
//   sum += num;
//   return sum;
// }

// console.log(addSum(3));


let sum = 5;

const addSum = function() {
  sum += 5;
  return sum;
}

console.log(addSum(3));
