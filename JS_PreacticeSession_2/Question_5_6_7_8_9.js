

function IsPositive(number) {
    return number >= 0;
}


function IsOdd(number) {
    return number % 2 != 0;
}

function GetMax(a, b) {
    
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}

function GetGrade(marks) {

    switch (marks) {
        case 10 : return "A";
        case 9 : return "B";
        case 8 : return "C";
        case 7 : return "D";
        case 6 : return "E";
        case 5 : return "F";
        default : return "back to foundation";
    }

}

function GetPriceWithAge(age) {

    if (age < 12) {
        return 5;
    }
    else if (age >= 12 && age < 18) {
        return 10;
    }
    else if (age >= 18 && age < 60) {
        return 20;
    }
    else {
        return 15;
    }

}


console.log(GetPriceWithAge(60))