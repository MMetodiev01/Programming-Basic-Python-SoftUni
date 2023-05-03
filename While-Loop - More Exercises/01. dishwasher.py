detergent_bottles = int(input())
detergent_ml = detergent_bottles * 750

plate_ml = 5
pot_ml = 15
load_count = 0
clean_plates = 0
clean_pots = 0

while True:
    dishes = input()
    if dishes == "End":
        break
    dishes = int(dishes)
    load_count += 1

    if load_count % 3 == 0:
        detergent_needed = dishes * pot_ml
        clean_pots += dishes
    else:
        detergent_needed = dishes * plate_ml
        clean_plates += dishes

    detergent_ml -= detergent_needed
    if detergent_ml < 0:
        print(f"Not enough detergent, {abs(detergent_ml)} ml. more necessary!")
        break

print("Detergent was enough!")
print(f"{clean_plates} dishes and {clean_pots} pots were washed.")
print(f"{detergent_ml} ml. leftover detergent")
