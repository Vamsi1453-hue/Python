#3. Student Top K Ranking (Medium)
n = int(input("Enter number of students: "))
students = [(name, int(marks)) for name, marks in (input("Enter name and marks: ").split() for _ in range(n))]
k = int(input("Enter k: "))

students.sort(key=lambda x: (-x[1], x[0]))

print(f"\nTop {k} Students:")
for i, (name, marks) in enumerate(students[:k], start=1):
    print(f"{i}. {name} - {marks}")

