#use count() to check atttendence.count(absent), you can also use loop with counter variable, ensure case consistency 'absent'!-'Absent'
attendance=list(map(str,input('Enter the prices: ').lower().split()))
print(f"Number of Absentees are{attendance.count('absent')}")