ticket = input("Enter the ticket number (6 digits): ")
if len(ticket) == 6 and ticket.isdigit():
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sum1 == sum2:
        print("Happy")
    else:
        print("Ordinary")
else:
    print("Invalid ticket number. Please enter a 6-digit number.")


