let count = 0;

function cc(card) {
  // Only change code below this line

  switch (card){

    case 2:
    case 3: 
    case 4:
    case 5:
    case 6: 
    //   count += 1;
      count++;
      break;
    // case 7:
    // case 8:
    // case 9:
    //   count;
    //   break;
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
    //   count -= 1;
      count--;
      break;
  }

//   if (count > 0) {
//     return count + " Bet"   
//   } else {
//     return count + " Hold"
//   }

  var holdbet = 'Hold'
  if (count > 0) {
    holdbet = 'Bet'
  }


  return count + " " + holdbet;


  // return "Change Me";
  // Only change code above this line
}

// console.log(cc('J'));
// console.log(cc(3));
// console.log(cc(7));
// console.log(cc('K'));
// console.log(cc('A'));


// cc(2); cc('K'); cc(10); cc('K'); cc('A');
// console.log(cc(4))

console.log(cc(2)) 
console.log(cc('K'))
console.log(cc(10)) 
console.log(cc('K'))
console.log(cc('A'))
console.log(cc(4))