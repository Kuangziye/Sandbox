MIN_PASSWORD = 8

password = str(input("Enter your password: "))
while len(password) < MIN_PASSWORD:
    print("The password length does not meet the requirements")
    password = str(input("Enter your password: "))

print("*" * len(password))

