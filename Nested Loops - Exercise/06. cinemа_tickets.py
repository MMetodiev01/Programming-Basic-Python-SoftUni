command = input()

open_seats = int(input())
type_ticked = input()
student = 0
standard = 0
kid = 0
total_seats = 0
while command != "Finish":
    movie_name = command

    if type_ticked == "student":
        student += 1
    elif type_ticked == "standard":
        standard += 1
    else:
        kid += 1
    type_ticked = input()
    total_seats = student + standard + kid
    percent_cinema_seats = (open_seats / total_seats) * 100
    if command == "End":
        print(f"{movie_name} - {percent_cinema_seats}% full.")
        command = input()
        student = 0
        standard = 0
        kid = 0
percent_student = student / 100
percent_standard = standard / 100
percent_kid = kid / 100


# ---------------------------------------------------
# inputLine = input()
#
# totalTickets=0
# studentTickets = 0
# standardTickets = 0
# kidsTickets = 0
#
# while inputLine != "Finish":
#     curMoiveName= inputLine
#
#     seats = int(input())
#     command = input()
#     counterTickets = 0
#
#     while command != "End":
#         typeTicket = command
#         counterTickets += 1
#         if typeTicket == "standard":
#             standardTickets += 1
#         elif typeTicket == "student":
#             studentTickets += 1
#         elif typeTicket == "kid":
#             kidsTickets += 1
#         if counterTickets >= seats:
#             break
#         command = input()
#
#     currentMovie = counterTickets / seats * 100
#     totalTickets+=counterTickets
#     print(f"{curMoiveName} - {currentMovie:.2f}% full.")
#     inputLine=input()
#
# standartPercent= standardTickets / totalTickets * 100
# studentPercent= studentTickets / totalTickets * 100
# kidPercent= kidsTickets / totalTickets * 100
# print(f"Total tickets: {totalTickets}")
# print(f"{studentPercent:.2f}% student tickets.")
# print(f"{standartPercent:.2f}% standard tickets.")
# print(f"{kidPercent:.2f}% kids tickets.")