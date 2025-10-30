import struct

FILENAME = 'players.dat'
RECORD_SIZE = 14
FMT = 'i10s'

def add_player(id, name):
    with open(FILENAME, 'ab') as file:
        name = name.encode().ljust(10)
        record = struct.pack(FMT, id, name)
        file.write(record)

def remove_all_players():
    with open(FILENAME, 'wb') as file:
        pass

def find_player(index):
    with open(FILENAME, 'rb') as file:
        file.seek(index * RECORD_SIZE)
        record = file.read(RECORD_SIZE)
        if record:
            id, name = struct.unpack(FMT, record)
            print(f'ID: {id} | Name: {name.decode().strip()}')
        else:
            print('No record at that index.')

def show_players():
    print('========== PLAYERS DATA : ==========')
    with open(FILENAME, 'rb') as file:
        while True:
            record = file.read(RECORD_SIZE)
            if record:
                id, name = struct.unpack(FMT, record)
                print(f'ID: {id} \t| Name: {name.decode().strip()}')
            else:
                break

    print('====================================')




'''
TODO :
1. remove_player()
2. update_player()
'''

# Example usage
remove_all_players()
add_player(14, 'Smith')
add_player(16, 'Varun')
add_player(1, 'Ravi')
add_player(20, 'Ali')
show_players()

show_players()