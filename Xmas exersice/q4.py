storage = {
    "principle": int(input("Enter a Principle amount: ")),
    "rate": float(input("Enter a rate: ")),
    "time": int(input("Enter a time: "))
}

SI = (storage["principle"] * storage["rate"] * storage["time"])/100
print(SI)