scores = [88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85]

valid_scores = []

grades = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

print("Student Grades")
print("-" * 30)

for index, score in enumerate(scores):

    if score == -999:
        print("\nSentinel value encountered")
    
    if score < 0:
        print("Invalid score skipped")
        continue

    if score >= 90:
        grade = "A"
    
    elif score >= 80:
        grade = "B"

    elif score >= 70:
        grade = "C"

    elif score >= 60:
        grade = "D"

    else:
        grade = "F"

    valid_scores.append(score)
    grades[grade] += 1

    print(f"Student {index}: Score = {score}, Grade = {grade}")


print("\nClass Stats")
print("-" * 30)

if valid_scores:

    average = sum(valid_scores) / len(valid_scores)

    highest = max(valid_scores)

    lowest = min(valid_scores)

    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    
    print(f"\nGrade Distribution")

    for grade, count in grades.items():
        print(f"{grade}: {count}")

else:
    print("No valid grades")
