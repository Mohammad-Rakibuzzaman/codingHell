// function test(myCondition) {
//     if (myCondition) {
//       return "It was true";
//     }
//     return "It was false";
// }

// console.log(test(true));
// // console.log(test(false));



function testGreaterThan(val) {
  if (val > 100) {  // Change this line
    return "Over 100";
  }

  if (val > 10) {  // Change this line
    return "Over 10";
  }

  return function(){

    return "10 or Under";
  } 

}

// console.log(testGreaterThan(10));


const answer = testGreaterThan(10)

console.log(answer());