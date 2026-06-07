# a devops at saas company recieves a server log as a list of status from past 24 hrs . she need to extract only the last 5 log entries most recent for quick incident review and identify if any of them is 500 error
log = list(map(int, input("Enter the log: ").split()))
last_five = log[-5:]
for entry in last_five:
    if entry == 500:
        print(f"Critical Error Found: True (Status {entry})")
    else:
        print(f"Critical Error Found: False (Status {entry})")

# other logic
Score=list(map(int,input('Enter the HTTP codes: ').split()))
print("new: {login[-5:]}| Critical error Found  {True} if 500 {in} Last_five else {False}")