def free_ticket(age) :
    if age < 12 or age > 65:
        return True
    else:
        return False
    
age = int(input("Enter your age please: "))

if free_ticket(age):
    print("Here is your thicket.")
else:
    print("Sorry but you ass can't get a free Ticket.")

