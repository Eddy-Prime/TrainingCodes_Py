#Exercise: Calculate Average
#Write a Python program that calculates the average of a list of numbers. The program should:

#Prompt the user to enter the number of elements they want in the list.
#Prompt the user to enter each number individually.
#Calculate and print the average of the numbers.

#Hint: Use a for loop to prompt the user to enter each number individually. Use the sum() function to calculate the sum of the numbers in the list.

#Sample output:

def calculate_Average(num_list):
    total = sum(num_list)
    average = total/len(num_list)
    return average

def main():
    num_elements = int(input("Enter the number of elements you want in the list: "))
    num_list = []

    for i in range(num_elements):
        num = int(input("Enter a number: "))
        num_list.append(num)

    average = calculate_Average(num_list)
    print(f"The average of the numbers is {average}")

if __name__ == "__main__":
    main()