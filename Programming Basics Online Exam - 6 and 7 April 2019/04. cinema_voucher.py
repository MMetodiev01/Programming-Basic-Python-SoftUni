voucher_price = int(input())
command = input()

count_tickets = 0
count_others = 0
while command != "End":
    input_line = len(command)
    if input_line > 8:
        sim01 = ord(command[0])
        sim02 = ord(command[1])
        ticket_price = sim01 + sim02
        voucher_price -= ticket_price
        if voucher_price < 0:
            break
        else:
            count_tickets += 1
    else:
        ticket_price = ord(command[0])
        voucher_price -= ticket_price
        if voucher_price < 0:
            break
        else:
            count_others += 1
    command = input()
print(count_tickets)
print(count_others)


