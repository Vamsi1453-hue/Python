def classify_password(pwd):
    if len(pwd) < 8:
        return "Weak"
        
    checks = [
        any(c.isupper() for c in pwd),
        any(c.islower() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(not c.isalnum() for c in pwd)
    ]
    
    score = sum(checks)
    
    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

try:
    n = int(input("Enter the number of words: "))
except KeyboardInterrupt:
    n = 0
    print("\nNo input provided")

if n > 0:
    passwords = [input().strip() for _ in range(n)]
else:
    passwords = []

counts = {"Strong": 0, "Medium": 0, "Weak": 0}

for p in passwords:
    category = classify_password(p)
    counts[category] += 1

print("Strong", counts["Strong"])
print("Medium", counts["Medium"])
print("Weak", counts["Weak"])