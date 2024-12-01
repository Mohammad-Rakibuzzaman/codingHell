// // // Setup
// // function phoneticLookup(val) {
// //     let result = "";

// //     // Only change code below this line
// //     // switch(val) {
// //     //   case "alpha":
// //     //     result = "Adams";
// //     //     break;
// //     //   case "bravo":
// //     //     result = "Boston";
// //     //     break;
// //     //   case "charlie":
// //     //     result = "Chicago";
// //     //     break;
// //     //   case "delta":
// //     //     result = "Denver";
// //     //     break;
// //     //   case "echo":
// //     //     result = "Easy";
// //     //     break;
// //     //   case "foxtrot":
// //     //     result = "Frank";
// //     // }

// //     const lookup = {

// //       "alpha": "Adams",
// //       "bravo": "Boston",
// //       "charlie": "Chicago",
// //       "delta": "Denver",
// //       "echo": "Easy",
// //       "foxtrot": "Frank"

// //     };

// //     result = lookup[val]

// //     // Only change code above this line
// //     return result;
// //   }

// // console.log(phoneticLookup("charlie"));

// // function checkObj(obj, checkProp) {
// //     // Only change code below this line

// //     // if(obj.hasOwnProperty(checkProp)){
// //     //   return obj[checkProp];
// //     // } else {
// //     //   return "Not Found";
// //     // }

// //     switch (true) {

// //         case obj.hasOwnProperty(checkProp):
// //             return obj[checkProp];

// //         default:
// //             return "Not Found";
// //     }

// //     // Only change code above this line
// //   }

// // console.log(checkObj({Ance: 'Hisoka', Rabbae: 'Aegon', Crescent: 'Cressy'}, 'Rattt'));

// const ourStorage = {
//   "desk": {
//     "drawer": "stapler"
//   },
//   "cabinet": {
//     "top drawer": {
//       "folder1": {
//         folder3: "castle0",
//         folder4: "Keywaredrop"
//       },
//       "folder0 2": {
//         cloths: "shirt",
//         hairstyle: "gelspike"
//       }

//     },
//     "bottom drawer": "soda"
//   }
// };

// function retunObj(obj){
//   return obj;
// }

// const addGroom = ourStorage.cabinet["top drawer"]["folder0 2"]["AddGroom"];
// const updatedObj = ourStorage.cabinet["top drawer"]["folder0 2"]["AddGroom"]= "clean shave";
// const newObj = ourStorage.cabinet["top drawer"]["folder0 2"]
// console.log(retunObj(newObj));

// // console.log(ourStorage.cabinet["top drawer"].folder1["folder3"]);

// // console.log(ourStorage.cabinet["top drawer"].folder02["hairstyle"])
// // console.log(ourStorage.cabinet["top drawer"]["folder0 2"].hairstyle);
// // console.log(ourStorage.cabinet["top drawer"].);

// // console.log(ourStorage.desk.drawer);

// Setup
const recordCollection = {
  2548: {
    albumTitle: "Slippery When Wet",
    artist: "Bon Jovi",
    tracks: ["Let It Rock", "You Give Love a Bad Name"],
  },
  2468: {
    albumTitle: "1999",
    artist: "Prince",
    tracks: ["1999", "Little Red Corvette"],
  },
  1245: {
    artist: "Robert Palmer",
    tracks: [],
  },
  5439: {
    albumTitle: "ABBA Gold",
  },
};

// console.log(recordCollection[5439]["albumTitle"]);
// console.log(recordCollection[5439].hasOwnProperty("albumTitle"));

function updateRecords(records, id, prop, value) {
  if (value == "") {
    delete records[id][prop];
  } else if (prop != "tracks" && value != "") {
    records[id][prop] = value;
  } else if (prop == "tracks" && value != "") {
    if (!records[id].hasOwnProperty(prop)) {
      records[id][prop] = [];
    }
    records[id][prop].push(value);
  }

  return records;
}

console.log(
  updateRecords(recordCollection, 5439, "tracks", "Take a Chance on Me")
);
// console.log(updateRecords(recordCollection, 1245, "tracks", "Addicted to Love"));
// console.log(
//   updateRecords(recordCollection, 2468, "tracks", "love you today or never")
// );
