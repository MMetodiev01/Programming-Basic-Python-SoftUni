count_easter_bred = int(input())
number_of_eggshells = int(input())
kg_cookies = int(input())

price_for_easter_bread = count_easter_bred * 3.20
price_for_eggshells = number_of_eggshells * 4.35
price_for_cookies = kg_cookies * 5.40
price_for_paint_eggs = number_of_eggshells * 12 * 0.15
final_price = price_for_easter_bread + price_for_eggshells + price_for_cookies + price_for_paint_eggs
print(f"{final_price:.2f}")