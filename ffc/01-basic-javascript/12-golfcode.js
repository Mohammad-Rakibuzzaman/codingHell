
const golfNickname = ["Hole-in-one!","Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]

function golfRank(par, strokes) {

    if (strokes == 1) { 
        return "Hole-in-one!"
    } else if (strokes <= par-2) {
        return "Eagle";
    } else if (strokes == par - 1) {
        return "Birdie";
    } else if (strokes == par) { 
        return names[3];
    } else if (strokes == par + 1) { 
        return names[4];
    } else if (strokes == par + 2) { 
        return names[5];
    } else { 
        return names[6];
    }

}


console.log(golfRank(5,4))