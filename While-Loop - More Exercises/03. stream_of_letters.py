command = input()

word = ""
n_count = 0
c_count = 0
o_count = 0

while command != "End":
    letter = ord(command)
    secret_word = 0
    if 65 <= letter <= 90 or 97 <= letter <= 122:
        if letter == 110 and n_count < 1:
            n_count += 1
        elif letter == 99 and c_count < 1:
            c_count += 1
        elif letter == 111 and o_count < 1:
            o_count += 1
        else:
            secret_word = letter
            word += chr(secret_word)
    if n_count == 1 and c_count == 1 and o_count == 1:
        print(word, end=" ")
        word = ""
        n_count = 0
        c_count = 0
        o_count = 0
    command = input()

