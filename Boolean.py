def your_age(age):
    if age >= 18:
        print("You are an adult.")
    elif 13 <= age <= 17:
        print("You're a teenager.")
    else:
        print("You're a kid.")

# Get user input for age
user_age = int(input("Enter your age: "))
your_age(user_age)
