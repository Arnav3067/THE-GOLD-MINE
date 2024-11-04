function GetAreaOfCircle(radius) {
    return 3.14 * radius * radius;
}

function GetAreaOfTriangle(base, height) {
    return 0.5 * base * height;
}

function GetPower(n, exponent) {;

    for (var i = 1; i < exponent; i++) {
        n *= n;
    }

    return n
}

function GetVolume(radius) {
    return (4/3) * 3.14 * GetPower(radius, 3);
}

function GetEnergy(mass) {
    return mass * GetPower(3 * GetPower(18, 8), 2);
}
