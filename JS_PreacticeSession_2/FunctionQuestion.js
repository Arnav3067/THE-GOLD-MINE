

function MinuetsToHours(time) {
    return time / 60;
}

function GetAverage(numberSet) {

    var result = 0;

    for (let i = 0; i < numberSet.length; i++) {
        result += numberSet[i];
    }

    return result/numberSet.length;
}

function GetGasAmount(distanceToDestination, consumption) {
    return distanceToDestination  * consumption/100;
}


console.log(GetGasAmount(1000, 100));
