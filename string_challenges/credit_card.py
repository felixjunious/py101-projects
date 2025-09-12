card_no = input('Enter Card No : ')

last_digits = card_no[15:]
four = 'X'*4 + ' '
disp_no = four*3 + last_digits

print(disp_no)