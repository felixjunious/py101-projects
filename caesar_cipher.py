def caesar(original_text, shift, encrypt_mode=True):
    if not encrypt_mode:
        shift *= -1

    def shift_alpha(alpha, shift):
        base = ord('a') if alpha.islower() else ord('A')
        return chr((ord(alpha) - base + shift) % 26 + base)

    encrypted_text  = ""
    for letter in original_text:
        if letter.isalpha():
            encrypted_text += shift_alpha(letter,shift)
        else:
            encrypted_text += letter

    return encrypted_text


if __name__ == "__main__":

    print('''
        ░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░░░░░░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗░░░░██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
        ██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝░░░░██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
        ██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗░░░░██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
        ╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║░░░░╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
        ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    ''')

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))

        encrypt_mode = direction == 'encode'

        output_text = caesar(text, shift, encrypt_mode)
        print(f"Here is the {direction}d result: {output_text}")

        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
        if restart == 'no':
            print("Bye Bye!")
            break