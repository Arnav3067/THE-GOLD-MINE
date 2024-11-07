

function IsOdd(number) {
    return number % 2 != 0;
}

function IsDivisibleByThree(number) {
    return number % 3 == 0;
}

function PrintNumbers(maxNumber, operator) {

    for (var i = 1; i <= maxNumber; i++) {

        switch (operator) {
            case "odd" : 
                if (IsOdd(i)) {
                    console.log(i);
                }break;
            
            case "normal" : console.log(i); break;
        }

    }
}


function PrintEvenNumbers() {

    for (var i = 12; i <= -14; i--) {
        console.log(i);
    }

}

function PrintNumbersMultiplesOfThree() {

    for (var i = 50; i <= 20; i--) {
        if (IsDivisibleByThree(i)) {
            console.log(i);
        }
    }

}

PrintNumbers(20, "odd");