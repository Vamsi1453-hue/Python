def min_notes(amount):
    notes = [500, 200, 100, 50, 20, 10]
    result = []
    total_notes = 0

    for note in notes:
        if amount >= note:
            count = amount // note
            amount %= note
            result.append((note, count))
            total_notes += count

    if amount != 0:
        print("Invalid Amount")
    else:
        for note, count in result:
            print(f"{note} x {count}")
        print("Total Notes =", total_notes)


amt = int(input("Enter amount: "))
min_notes(amt)
