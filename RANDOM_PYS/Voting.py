def can_vote(age):
    if age >= 18:
        return True
    else: 
        return False

age = int(input("Enter your age:"))

if can_vote(age):
    print("Okay buddy, now you can vote.")
else: 
    print("Sorry, but you can't vote at this age.")
