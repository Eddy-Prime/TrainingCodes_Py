import math

def calculate_average(grades):
    if not grades:
        return 0
    total = sum(grades.values())
    return round(total / len(grades))

def highest_scorer(grades):
    if not grades:
        return []
    highest_grade = max(grades.values())
    return [name for name, grade in grades.items() if grade == highest_grade]

def calculate_stats(input):
    grades = {}

    # Read the input file and store grades in a dictionary
    with open(input, 'r') as file:
        for line in file:
            name, grade = line.strip().split(',')
            grades[name.strip()] = int(grade.strip())

    # Calculate average and find highest grades
    avg_grade = calculate_average(grades)
    top_scorers = highest_scorer(grades)

    # Write results to output file
    with open('results.txt', 'w') as output_file:
        output_file.write(f"Average Grade: {avg_grade}\n")
        output_file.write("Top Scorers:\n")
        for scorer in top_scorers:
            output_file.write(f"{scorer}\n")

if __name__ == "__main__":
    calculate_stats("grades.txt")
