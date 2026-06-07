#a corporate office uses a booking system where reserved time slots are stored in a list . when a employee tries to book a room , the system checks if their requested time slot is 
Time=list(map(str,input("Enter the time slot avaliable:").split()))
booking=list(map(str,input("Enter the booking time").split()))
print("slot already booked" if booking in Time else "Time slots is available")
#another logic
slots=list(map(str,input("Enter the booked slots: ").split()))
time_slot=input("Enter the requested slots: ")
print("Slot ALready Booked" if time_slot in slots else "Slot is Availabe")