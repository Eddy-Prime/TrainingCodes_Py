from math import ceil

def movie_ticket(discount):

    duration = int(input("How long is the movie?"))
    if duration <= 90:
        price = 10
    elif duration <=120:
        price = 12
    else:
        price = 15

    imax_response = input("Is it an IMAX movie?")
    if imax_response.lower() == "yes":
        imax = True
        price = ceil(price * 1.2)

    student_response = input("Are you a student?")
    if student_response.lower() == "yes":
        student = True
        price -=3

    return price * discount    


todo_list = {
    "movie": movie_ticket(1),
    "groceries": 100,
    "rent": 1000,
    "bills": 200
}

#for loop

for i, thing in enumerate(todo_list):
    print(i, thing.title())