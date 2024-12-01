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

// // Only change code below this line
// function updateRecords(records, id, prop, value) {
//     if (prop !== 'tracks') {
//         if (value == '') {
//             delete records[id][prop]
//         } else {
//             records[id][prop] = value
//         }
//     } else { // when prop == 'tracks
//         if (value == '') {
//             delete records[id][prop]
//         } else {
//             if (!Array.isArray(records[id].tracks)) {
//                 records[id][prop] = []
//                 records[id][prop].push(value);
//             } else {
//                 records[id].tracks.push(value);
//             }
//         }

//     }
//     return records;
// }

// // console.log(updateRecords(recordCollection, 5439, 'artist', 'ABBA'));
// console.log(updateRecords(recordCollection, 5439, 'tracks'));



// const myStorage = {
//     "car": {
//         "inside": {
//             "glove box": "mapsxxxx",
//             "passenger seat": "crumbs"
//         },
//         "outside": {
//             "trunk": "jack"
//         }
//     }
// };

// const gloveBoxContents = myStorage["car"]["inside"]["glove box"];

// console.log(gloveBoxContents);


const myPlants = [
    {
        type: "flowers",
        list: [
            "rose",
            "tulip",
            "dandelion"
        ]
    },
    {
        type: "trees",
        list: [
            "fir",
            "pine",
            "birch"
        ]
    }
];

const secondTree = myPlants[1].list[1];
console.log(secondTree);
