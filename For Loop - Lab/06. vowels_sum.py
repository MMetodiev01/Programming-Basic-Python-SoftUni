text = input()
vowel_values = {"a": 1, "e": 2, "o": 3, "i": 4, "u": 5}
sum = 0


for letter in text:
    if letter in vowel_values:
        sum += vowel_values[letter]
print(sum)
