'''
score=list(map(int,input("Enter the score of students")))
print(score.sort(reverse='True'))
top_Scorer=int(input())==True
print(top_Scorer)
value=sorted(reverse='True')
print(value)
'''
'''
Score=list(map(int,input('ENter the scores: ').split()))
new=Score.sort(reverse=True)
print(f"Ranked: {Score.sort(reverse=True)} | Top Scorer : {Score[0]}")
'''
scores = list(map(int, input("Enter the scores of students: ").split()))
scores.sort(reverse=True)
print(scores)
top_scorer = scores[0]
print(top_scorer)
value = sorted(scores, reverse=True)
print(value)

Score=list(map(int,input('Enter the score: ').split()))
print(f"Ranked :{sorted(Score,reverse=True)}| Top Scorer :{max(Score)}")