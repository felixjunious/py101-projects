FILENAME = 'journal.txt'

def write_entry():
    entry = input('Write your journal entry : ')
    with open(FILENAME, 'a') as file:
        file.write('\n' + entry)

def read_all():
    with open(FILENAME, 'r') as file:
        print('All Journal Entries : ')
        print(file.read())
        print()

def search():
    keyword = input('Enter keyword to search : ')

    with open(FILENAME, 'r') as file:
        found_match = False
        for line in file.readlines():
            if keyword.lower() in line.lower():
                found_match = True
                print(line.strip())

        if not found_match:
            print('No matching entries.')

        print()

def main_menu():
    while True:
        print('===== File Journal Menu =====')
        print('1. Add Entry')
        print('2. Read All Entries')
        print('3. Search Entries')
        print('4. Exit')
        option = int(input('Choose option (1-4): '))
        print()

        if option == 1:
            write_entry()
        elif option == 2:
            read_all()
        elif option == 3:
            search()
        elif option == 4:
            print('Bye!')
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main_menu()