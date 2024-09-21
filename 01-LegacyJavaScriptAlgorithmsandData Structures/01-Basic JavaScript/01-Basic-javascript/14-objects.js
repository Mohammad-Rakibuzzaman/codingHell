// // Setup
// function phoneticLookup(val) {
//     let result = "";
  
//     // Only change code below this line
//     // switch(val) {
//     //   case "alpha":
//     //     result = "Adams";
//     //     break;
//     //   case "bravo":
//     //     result = "Boston";
//     //     break;
//     //   case "charlie":
//     //     result = "Chicago";
//     //     break;
//     //   case "delta":
//     //     result = "Denver";
//     //     break;
//     //   case "echo":
//     //     result = "Easy";
//     //     break;
//     //   case "foxtrot":
//     //     result = "Frank";
//     // }
  
//     const lookup = {
  
//       "alpha": "Adams",
//       "bravo": "Boston", 
//       "charlie": "Chicago", 
//       "delta": "Denver", 
//       "echo": "Easy",
//       "foxtrot": "Frank"
  
//     };
  
//     result = lookup[val]
  
  
  
//     // Only change code above this line
//     return result;
//   }
  
// console.log(phoneticLookup("charlie"));





// function checkObj(obj, checkProp) {
//     // Only change code below this line
  
//     // if(obj.hasOwnProperty(checkProp)){
//     //   return obj[checkProp];
//     // } else {
//     //   return "Not Found";
//     // }
    
//     switch (true) {

//         case obj.hasOwnProperty(checkProp):
//             return obj[checkProp];

//         default: 
//             return "Not Found";
//     }

//     // Only change code above this line
//   }
  
// console.log(checkObj({Ance: 'Hisoka', Rabbae: 'Aegon', Crescent: 'Cressy'}, 'Rattt'));




const ourStorage = {
  "desk": {
    "drawer": "stapler"
  },
  "cabinet": {
    "top drawer": { 
      "folder1": {
        folder3: "castle0",
        folder4: "Keywaredrop"
      },
      "folder0 2": {
        cloths: "shirt",
        hairstyle: "gelspike"
      }
     
    },
    "bottom drawer": "soda"
  }
};



function retunObj(obj){
  return obj;
}

const addGroom = ourStorage.cabinet["top drawer"]["folder0 2"]["AddGroom"];
const updatedObj = ourStorage.cabinet["top drawer"]["folder0 2"]["AddGroom"]= "clean shave";
const newObj = ourStorage.cabinet["top drawer"]["folder0 2"]
console.log(retunObj(newObj));




// console.log(ourStorage.cabinet["top drawer"].folder1["folder3"]);

// console.log(ourStorage.cabinet["top drawer"].folder02["hairstyle"])
// console.log(ourStorage.cabinet["top drawer"]["folder0 2"].hairstyle);
// console.log(ourStorage.cabinet["top drawer"].);



// console.log(ourStorage.desk.drawer);
