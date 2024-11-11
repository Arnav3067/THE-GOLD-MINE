
let formSubmission = document.getElementById("practiceForm");

function PreventDefaultSubmission(event) {
    event.preventDefault();
    console.log("form submitted");
    let textInput = document.getElementById("generalInput");
    var userData = textInput.value.split(" ").map(Number);

    console.log(GetStandardDeviation(userData));

}

formSubmission.addEventListener("submit", PreventDefaultSubmission);


function _GetStatsOf(array) {

    let result = 0;
    for (let i of array) {
        result += i;
    }

    return {mean : result/array.length, size : array.length};
}

function GetStandardDeviation(array) {

    let stats = _GetStatsOf(array);
    let numerator = _GetNumerator(array, stats);
    let result = Math.sqrt(numerator/(stats.size - 1));
    return result.toFixed(2);

}

function _GetNumerator(array, stats) {

    let result = 0;

    for (let i of array) {
        result += Math.pow(i - stats.mean, 2);
    }

    return result;
}


