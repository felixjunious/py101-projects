import struct

FILENAME = 'books.dat'
RECORD_SIZE = 60
FMT = 'i30s20si'

def pack_record(book_id, title, author, stock):
    title = title.strip().encode().ljust(30)
    author = author.strip().encode().ljust(20)

    return struct.pack(FMT, book_id, title, author, stock)

def unpack_record(record_bytes):
    book_id, title, author, stock = struct.unpack(FMT, record_bytes)

    return {
        'BookID' : book_id,
        'Title' : title.decode().strip(),
        'Author' : author.decode().strip(),
        'Stock' : stock
    }

def add_book():
    book_id = int(input('Enter Book ID : '))
    title = input('Enter Title : ')
    author = input('Enter Author : ')
    stock = int(input('Enter Stock : '))

    record_byte = pack_record(book_id, title, author, stock)

    with open(FILENAME, 'ab') as file:
        file.write(record_byte)
        print('Book added successfully.')

def view_books():
    print('===== BOOK RECORDS =====')
    with open(FILENAME, 'rb') as file:
        while True:
            record_byte = file.read(RECORD_SIZE)
            if not record_byte:
                break

            book = unpack_record(record_byte)
            print(book)

def search_book():
    search_id = int(input('Enter Book ID to search : '))

    with open(FILENAME, 'rb') as file:
        while True:
            record_byte = file.read(RECORD_SIZE)

            if not record_byte:
                break

            book = unpack_record(record_byte)

            if book['BookID'] == search_id:
                print(book)
                return

    print('Book not found.')


def delete_book():
    delete_id = int(input('Enter Book ID to delete : '))
    found = False

    with open(FILENAME, 'r+b') as file:
        index = 0
        while True:
            file.seek(index * RECORD_SIZE)
            record_byte = file.read(RECORD_SIZE)
            book = unpack_record(record_byte)

            if not book:
                break

            if book['BookID'] == delete_id:
                file.seek(index * RECORD_SIZE)
                book['Stock'] = 0
                file.write(pack_record(book['BookID'], book['Title'], book['Author'], book['Stock']))
                found = True
                print(f"{book['Title']} (ID: {book['BookID']}) deleted (stock = 0)")
                break
            index += 1

    if not found:
        print('Book not found')

def main_menu():
    while True:
        print('=== Library Management System ===')
        print('1. Add Book')
        print('2. View Books')
        print('3. Search Book by ID')
        print('4. Delete Book')
        print('5. Exit')
        choice = int(input('Enter your choice (1-5): '))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            delete_book()
        elif choice == 5:
            break
        else:
            print('Invalid Choice. Try Again.')
        input('\nPress Enter to continue...')

if __name__ == '__main__':
    main_menu()