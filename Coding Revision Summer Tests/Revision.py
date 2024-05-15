class SummerCodingRevision:

    daysOfTheWeek = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "friday",
        5: "saturday",
        6: "sunday"
    }
    
    name = []
    sales = []

    def Question1(self):
        entryList = input("Enter five numbers (with spaces):  ").strip().split()
        print("Her is your list ", entryList)
        
        def AddOne(i: str) :
            return int(i) + 1

        entryList = list(map(AddOne, entryList))

        print(entryList)

    def Question2(self):
        Hours = [12.0, 7.0, 9.0, 9.0, 6.0, 8.0, 2.0]
        # every hour it spends 0.675
        for i in range(len(Hours)):
            Hours[i] *= 0.675

        total = sum(Hours)
        print(f"{total:.1f}")

    def Question3(self):
        rainfall = []
        for i in range(7):
            recorded = float(
                input(f"Enter the rainfall on {self.daysOfTheWeek[i]}: ").strip())
            rainfall.append(recorded)

        average = sum(rainfall) / len(rainfall)
        print(f"\nThe total is {sum(rainfall)} and the average is {average} \n")

        for i, element in enumerate(rainfall):
            if (element > 3.5):
                print(f"it exceeded by {element-3.5} on {self.daysOfTheWeek[i]}")

    def Question4(self):
        print("***Welcome***")
        running = True
        
        while running:
            choice = int(input("""
Choose what you would like to do

1. Enter Sales data
2. View the total sales made up to date
3. View the maximum amount of sales to date of a staff member
4. View the minimum amount of sales to date of a staff member
5. View the average amount of sales to date of a staff member
0. Exit the programme

Enter here: """))

            match choice:
                case 1: self._Choice1()
                case 2: self._Choice2()
                case 3: self._Choice3()
                case 4: self._Choice4()
                case 5: self._Choice5()
                case 0: running = False

        print("\nThank you for visiting")

    def _Choice1(self):
        employee = input("\nEnter thy name: ").lower()
        contribution = float(input("Ente thy sales values: "))
        self.name.append(employee)
        self.sales.append(contribution)

    def _Choice2(self):
        print(f"\nThe total sales made to date {sum(self.sales)} \n")

    def _Choice3(self):
        targetSales = self._GetTargetSales()
        print(f"Their maximum sales value is : {max(targetSales):.2f}")

    def _Choice4(self):
        targetSales = self._GetTargetSales()
        print(f"Their minimum sales value is : {min(targetSales):.2f}")

    def _Choice5(self):
        targetSales = self._GetTargetSales()
        print(f"Their average sales value is : {sum(targetSales)/2:.2f}")

    
    def _GetTargetSales(self) -> list[float]:
        target = ""
        while target not in self.name:
            target = input("Enter the name of the employer you wanna mugg: ").lower().strip()

        targetSales = []
        for i, element in enumerate(self.name):
            if (element == target):
                targetSales.append(self.sales[i])

        return targetSales




def main():
    answers = SummerCodingRevision()
    answers.Question4()


if __name__ == "__main__" :
    main()
