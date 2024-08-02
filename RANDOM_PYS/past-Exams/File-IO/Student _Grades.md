# Processing Student Grades Data

You have received a text file called `grades.txt` with the following formatting:
 ```plaintext
        Alice, 85
        Bob, 90
        Charlie, 78
        David, 92
        Eve, 88
        Frank, 75
        Grace, 91 
```



Write Python code to process this data according to the following requirements:

1. **Define a function `calculate_average(grades)`**
    - Takes as a parameter a dictionary containing student names and their grades.
    - Returns the average grade rounded to an integer value.
    - You can calculate the average by adding up the grades and dividing by the number of students.

2. **Define a function `highest_scorer(grades)`**
    - Takes as a parameter a dictionary containing student names and their grades.
    - Returns a list with the name(s) of the student(s) who have the highest grade.
    - If multiple students have the same highest grade, the list contains the names of all these students.

3. **Define a function `calculate_stats(input_file)`**
    - Takes as input the name of a text file and processes it as follows:
        - Opens the text file given as input and reads in the student names and grades. You can assume it follows the pattern shown above.
        - Store the information in a dictionary where each entry has a student's name and grade.
        - Use the functions you've defined above to find the average grade and the highest scorers.
        - Write the results to a file called `results.txt` according to the following format:
     ```plaintext
        Total number of students: 7
        Average grade: 85
        Highest scorers:
        - David
        - Grace
    ```