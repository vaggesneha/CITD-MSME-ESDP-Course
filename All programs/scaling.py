# Marks Converter: 100 to 60

num_students = int(input("How many students? (max 10): "))

for i in range(num_students):
    mark = float(input(f"Student {i+1} marks (out of 100): "))
    converted = (mark / 100) * 60
    print(f"  Converted: {converted:.2f} out of 60")
    print()

print("Done!")

'''
print("=" * 50)
print("MARKS CONVERTER: 100 → 60")
print("=" * 50)

# Get number of students
while True:
    try:
        num_students = int(input("\nEnter number of students (max 10): "))
        if 1 <= num_students <= 30:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input! Please enter a number.")

print("\n" + "-" * 50)

# Store original and converted marks
original_marks = []
converted_marks = []

# Input marks for each student
for i in range(num_students):
    while True:
        try:
            mark = float(input(f"Enter marks for Student {i+1} (out of 100): "))
            if 0 <= mark <= 100:
                original_marks.append(mark)
                # Convert to marks out of 60
                converted = (mark / 100) * 60
                converted_marks.append(round(converted, 2))
                break
            else:
                print("Marks must be between 0 and 100!")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Display results
print("\n" + "=" * 50)
print("CONVERSION RESULTS")
print("=" * 50)
print(f"{'Student':<12} {'Original (/100)':<18} {'Converted (/60)':<15}")
print("-" * 50)

for i in range(num_students):
    print(f"Student {i+1:<5} {original_marks[i]:<18} {converted_marks[i]:<15}")

print("=" * 50)
print("Conversion Complete!")
print("=" * 50)
'''