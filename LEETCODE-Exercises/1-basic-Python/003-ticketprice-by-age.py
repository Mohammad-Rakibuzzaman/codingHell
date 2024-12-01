enterAge = int(input("Enter your age please to get the discount: "))
areStudent = input("Are you a student? (yes/ no): ").lower()

ticketPrice = 100

if enterAge < 10:
    print("Ticket is free!")
elif enterAge <= 15:
    ticketPrice = 10
    print(f"Your ticket price is: {ticketPrice}$.")
elif enterAge <= 18:
    if areStudent == "yes":
        ticketPrice = 20
        print(f"Your ticket price is: {ticketPrice}$.")
    else:
        ticketPrice = 30
        print(f"Your ticket price is: {ticketPrice}$.")

else:
    if areStudent == "yes":
        ticketPrice = 50
        print(f"Your ticket price is: {ticketPrice}$.")

    else:
        print(f"Your ticket price is: {ticketPrice}$.")
