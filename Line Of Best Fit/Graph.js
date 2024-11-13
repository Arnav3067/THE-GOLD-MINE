import { Point } from "./Point";

export class Graph {

    coordinates;

    constructor (coordinates) {
        this.coordinates = coordinates;
    }

    GetMeanPointOfGraph() {
        let totalX = 0, totalY = 0;
        for (let point of this.coordinates) {
            totalX += point.x;
            totalY += point.y;
        }

        return new Point(totalX/this.coordinates.length, totalY/this.coordinates.length);
    }

    #GetAverageSlope(decimalPlaces, xMean, yMean) {

        let numerator = 0, denominator = 0;

        for (let point of this.coordinates) {
            numerator += (point.x - xMean) * (point.y - yMean);
            denominator += Math.pow(point.x - xMean, 2);
        }

        let result = parseFloat((numerator/denominator).toFixed(decimalPlaces))
        return result;
    }

    GetLineOfBestFit(decimalPlaces) {

        if (this.coordinates.length < 2) {
            console.error("IncompleteGraphDataException: Not enough points in the graph to create a line of best fit");
            return;
        }
        
        let meanPoint = this.GetMeanPointOfGraph()
        let slope = this.#GetAverageSlope(decimalPlaces, meanPoint.x, meanPoint.y);
        let yIntercept = parseFloat((meanPoint.y - (slope * meanPoint.x)).toFixed(decimalPlaces));

        return `y =${this.GetStringRepresentationOf(slope)}x ${this.GetStringRepresentationOf(yIntercept)}`
    }

    GetStringRepresentationOf(number) {

        if (number == 0) return number.toString();
        else if (number > 0) return " + " + Math.abs(number) 
        else return " - " + Math.abs(number)

    }

    AddPoint(point) {
        this.coordinates.push(point);
    }

    RemovePointAt(index) {
        this.coordinates = this.coordinates.splice(index, 1);
    }
}

