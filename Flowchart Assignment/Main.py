class FlowChartToCodeAssignment :

    def CelciustoFahrenheit(self, celcius) :
      return (9/5 * celcius) + 32

    def FahrenheitToCelcius(self, fahrenheit) :
      return (fahrenheit - 32) * (5/9)

    def AreaAndPerimeter(self, side) :
        return (side * side, side * 4)
    
    def SmallestOfTwoNumber(self, a, b):
        return a if a < b else b
            


def main() :

    assignment = FlowChartToCodeAssignment()
    
    print(assignment.SmallestOfTwoNumber(4, 3))


if __name__ == "__main__" :
    main()