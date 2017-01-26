def alphabet_position(letter):
    if len(letter) != 1:
        return 0
    new = ord(letter)
    if 65 <= new <= 90:
        # Upper case letter
        return new - 65
    elif 97 <= new <= 122:
        # Lower case letter
        return new - 97
    # Unrecognized character
    return 0


def rotate_character(char,rot):
    new_ord = (alphabet_position(char)+rot) % 26
    if char.isupper():
        if new_ord > ord('Z'):
            new_ord -= 65
        elif new_ord < ord('A'):
            new_ord += 65
        return chr(new_ord)
    elif char.islower():
        if new_ord > ord('z'):
            new_ord -= 97
        elif new_ord < ord('a'):
            new_ord += 97
        return chr(new_ord)
    return char


def encrypt(message, rot):
    encrypted = ''
    for char in message:
        a = rotate_character(char, rot)
        encrypted = encrypted + a

    return encrypted
