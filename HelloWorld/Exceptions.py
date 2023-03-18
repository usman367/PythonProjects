try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:  # Catching the exceptions
    print("Age cannot be 0")
except ValueError:
    print("Invalid Value")  # When the user doesn't enter an int for age
