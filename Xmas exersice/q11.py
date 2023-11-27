import math

storage = {
    "principle": int(input("Enter a Principle amount: ")),
    "rate": float(input("Enter a rate: ")),
    "time": int(input("Enter a time: "))
}

CI = storage["principle"] * (math.pow(1 + (storage["rate"]/100), storage["time"])) - storage["principle"]

print("CI: ", CI)

