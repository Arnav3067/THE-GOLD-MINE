import utility

password = utility.entryCheck("Enter a password: ",
                              r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{0,8}$",
                              "ValidationError: Does not meet the requirements",
                              Type="string")

print("Validated!")