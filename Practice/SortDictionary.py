# Function to sort students by marks
def sort_students(students):
    # Sorting the list of dictionaries using 'marks' key in descending order
    sorted_students = sorted(students, key=lambda x: x['marks'], reverse=True)
    return sorted_students

# List of students with their marks
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 87},
    {"name": "David", "marks": 90}
]

# Call the function and print the sorted list
sorted_students = sort_students(students)
for student in sorted_students:
    print(student)
