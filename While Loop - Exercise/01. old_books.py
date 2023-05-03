book_name = input()
book_counter = 0
is_book_found = False

while True:
    seconds_books = input()
    book_counter += 1
    if seconds_books == 'No More Books':
        book_counter -= 1
        print(f'The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break

    if seconds_books == book_name:
        is_book_found = True
        book_counter -= 1
        print(f'You checked {book_counter} books and found it.')
        break


