#1.	Write a function called swap that given a list of numbers and an index i  changes this list so that from index i to the end of the list, for every 2 consecutive elements x and y where x is greater than y, these elements are swapped. 
#The function will return if at least 1 mix-up has occurred.
 
#For example:
#- list = [1,2,8,7,4,3] , i = 3 --> list becomes [1,2,8,4,3,7] and returns True
#- list = [1,2,8,7,4,3] , i = 2 --> list becomes [1,2,7,4,3,8] and returns True
#- list = [2,1,3,4,5] and i = 1 --> list does not change and returns False

#2.	Write  a sort function  that for a given  list calls the swap function from  previous point for every i going from 0 to the end of list or until the swap function  returns False.

#///////////ANSWER/////////////////////

def swap(lst, i):
    swapped = False
    for j in range(i, len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            swapped = True
    return swapped

def sort(lst):
    for i in range(len(lst)):
        if not swap(lst, i):
            break
    return lst

lst = [1,2,8,7,4,3]
print(swap(lst, 3))  # Output: True
print(lst)  # Output: [1, 2, 8, 4, 3, 7]

lst = [1,2,8,7,4,3]
print(swap(lst, 2))  # Output: True
print(lst)  # Output: [1, 2, 7, 4, 3, 8]

lst = [2,1,3,4,5]
print(swap(lst, 1))  # Output: False
print(lst)  # Output: [2, 1, 3, 4, 5]

lst = [1,2,8,7,4,3]
print(sort(lst))  # Output: [1, 2, 3, 4, 7, 8]
