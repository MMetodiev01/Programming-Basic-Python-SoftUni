film_name = input()
type_room = input()
total_tickets = int(input())

final_sum = 0
if film_name == "A Star Is Born":
    if type_room == "normal":
        price_for_ticket = 7.50
        final_sum = total_tickets * price_for_ticket
    elif type_room == "luxury":
        price_for_ticket = 10.50
        final_sum = total_tickets * price_for_ticket
    else:
        price_for_ticket = 13.50
        final_sum = total_tickets * price_for_ticket
elif film_name == "Bohemian Rhapsody":
    if type_room == "normal":
        price_for_ticket = 7.35
        final_sum = total_tickets * price_for_ticket
    elif type_room == "luxury":
        price_for_ticket = 9.45
        final_sum = total_tickets * price_for_ticket
    else:
        price_for_ticket = 12.75
        final_sum = total_tickets * price_for_ticket
elif film_name == "Green Book":
    if type_room == "normal":
        price_for_ticket = 8.15
        final_sum = total_tickets * price_for_ticket
    elif type_room == "luxury":
        price_for_ticket = 10.25
        final_sum = total_tickets * price_for_ticket
    else:
        price_for_ticket = 13.25
        final_sum = total_tickets * price_for_ticket
elif film_name == "The Favourite":
    if type_room == "normal":
        price_for_ticket = 8.75
        final_sum = total_tickets * price_for_ticket
    elif type_room == "luxury":
        price_for_ticket = 11.55
        final_sum = total_tickets * price_for_ticket
    else:
        price_for_ticket = 13.95
        final_sum = total_tickets * price_for_ticket
print(f"{film_name} -> {final_sum:.2f} lv.")