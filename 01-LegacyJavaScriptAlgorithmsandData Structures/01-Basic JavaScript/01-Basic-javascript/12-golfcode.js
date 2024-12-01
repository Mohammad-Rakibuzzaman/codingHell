
// const golfNickname = ["Hole-in-one!","Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]

// function golfRank(par, strokes) {

//     if (strokes == 1) { 
//         return "Hole-in-one!"
//     } else if (strokes <= par-2) {
//         return "Eagle";
//     } else if (strokes == par - 1) {
//         return "Birdie";
//     } else if (strokes == par) { 
//         return names[3];
//     } else if (strokes == par + 1) { 
//         return names[4];
//     } else if (strokes == par + 2) { 
//         return names[5];
//     } else { 
//         return names[6];
//     }

// }


// console.log(golfRank(5,4))



// function isLess(a, b) {
//     // Only change code below this line
//     return a < b;
//     // Only change code above this line
// }
  
// console.log(isLess(100, 15));


// function myFun() {
//     console.log("Hello");
//     return "World";
//     console.log("byebye")
//   }
// console.log(myFun());


// Setup
function abTest(a, b) {
    // Only change code below this line
  
    if (a < 0 || b <0){
      return undefined;
    }
  
    // Only change code above this line
  
    return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
  }
  
  console.log(abTest(-2,-2));