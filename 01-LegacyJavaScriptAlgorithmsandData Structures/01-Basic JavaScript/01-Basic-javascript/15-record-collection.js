// // Setup
// const recordCollection = {
//     2548: {
//         albumTitle: 'Slippery When Wet',
//         artist: 'Bon Jovi',
//         tracks: ['Let It Rock', 'You Give Love a Bad Name']
//     },
//     2468: {
//         albumTitle: '1999',
//         artist: 'Prince',
//         tracks: ['1999', 'Little Red Corvette']
//     },
//     1245: {
//         artist: 'Robert Palmer',
//         tracks: []
//     },
//     5439: {
//         albumTitle: 'ABBA Gold'
//     }
// };

// function updateRecords(records, id, prop, value) {

//     if (value == "") {
//         delete records[id][prop];

//     } else if (prop != "tracks" && value) {

//         records[id][prop] = value;

//     } else if (prop === "tracks") {
//         if (!records[id].hasOwnProperty("tracks")) {
//             records[id]["tracks"] = [];
//         }

//         records[id]["tracks"].push(value);

//     }

//     return records;
// }

// // console.log(updateRecords(recordCollection, 5439, 'artist', 'ABBA'));
// // console.log(updateRecords(recordCollection, 5439, "artist", "ABBA"));
// // console.log(updateRecords(recordCollection, 5439, "tracks", "Take a Chance on Me"));
// console.log(updateRecords(recordCollection, 2548, "artist", ""));



// Setup
const recordCollection = {
    2548: {
        albumTitle: 'Slippery When Wet',
        artist: 'Bon Jovi',
        tracks: ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
        albumTitle: '1999',
        artist: 'Prince',
        tracks: ['1999', 'Little Red Corvette']
    },
    1245: {
        artist: 'Robert Palmer',
        tracks: []
    },
    5439: {
        albumTitle: 'ABBA Gold'
    }
};

function updateRecords(records, id, prop, value) {

    // if (records.hasOwnProperty(id)) {
    //     if (value == "") {
    //         delete records[id][prop];
    //     } else if (prop != "tracks" && value) {
    //         records[id][prop] = value;
    //     } else if (prop === "tracks") {
    //         if (records[id].hasOwnProperty(prop) === false) {
    //             records[id][prop] = [];
    //         }
    //         records[id][prop].push(value);
    //     }

    //     return records;
    // } else {
    //     return "Id not found";
    // }
    if (records.hasOwnProperty(id)) {
        if (value == "") {
            delete records[id][prop];
        } else if (prop != "tracks" && value) {
            records[id][prop] = value;
        } else if (prop === "tracks") {
            if (records[id].hasOwnProperty(prop) === false) {
                records[id][prop] = [];
            }
            records[id][prop].push(value);
        }

        return records;
    } else {
        return "Id not found";
    }




}

// console.log(updateRecords(recordCollection, 5439, 'artist', 'ABBA'));
// console.log(updateRecords(recordCollection, 5439, "artist", "ABBA"));
// console.log(updateRecords(recordCollection, 5439, "tracks", "Take a Chance on Me"));
console.log(updateRecords(recordCollection, 5439, "tracks"));



// const car = {
//     make: "Toyota",
//     model: "Camry",
//     specs: {
//         engine: "2.5L",
//         horsepower: 203
//     }
// };

// console.log(car["specs"]["engine"]); // Output: "2.5L"