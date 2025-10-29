import struct

RECORD_SIZE = 14

def add_player(id, name):
    with open('players.dat', 'ab') as file:
        name = name.encode().ljust(10)
        record = struct.pack('i10s', id, name)
        file.write(record)

def find_player(index):
    with open('players.dat', 'rb') as file:
        file.seek(index * RECORD_SIZE)
        record = file.read(RECORD_SIZE)
        if record:
            id, name = struct.unpack('i10s', record)
            print(f'ID: {id} | Name: {name.decode().strip()}')
        else:
            print('No record at that index.')

def show_players():
    print('========== PLAYERS DATA : ==========')
    with open('players.dat', 'rb') as file:
        while True:
            record = file.read(RECORD_SIZE)
            if record:
                id, name = struct.unpack('i10s', record)
                print(f'ID: {id} \t| Name: {name.decode().strip()}')
            else:
                break

    print('====================================')


def clear_records():
    with open('players.dat', 'wb') as file:
        pass

clear_records()
add_player(14, 'Smith')
add_player(16, 'Varun')
add_player(1, 'Ravi')
add_player(20, 'Ali')
show_players()