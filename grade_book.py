print("=== Student Grade Book ===\n")

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

total = 0
for score in grades.values():
    total += score

class_average = total / len(grades)
print(f"Class Average: {class_average}\n")

top_name = ""
top_score = 0

for name, score in grades.items():
    if score > top_score:
        top_score = score
        top_name = name

print(f"Highest Scorer: {top_name} with a score of {top_score}\n")

search_name = input("Enter student name to look up: ")
score_result = grades.get(search_name, "Not found")
print(f"Score for {search_name}: {score_result}")
