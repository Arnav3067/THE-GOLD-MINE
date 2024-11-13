import { Graph } from "./Graph";
import { Point } from "./Point";

function Main() {

    let graph = new Graph
    ([   
        new Point(8, 3),
        new Point(2, 10), 
        new Point(11, 3), 
        new Point(6, 6), 
        new Point(5, 8), 
        new Point(4, 12), 
        new Point(9, 4), 
        new Point(12, 1), 
        new Point(1, 14), 
        new Point(6, 9)
    ]);

    console.log(graph.GetLineOfBestFit(1));
}


Main();