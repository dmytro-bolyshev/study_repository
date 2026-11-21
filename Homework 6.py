text = input("Введіть слово (малі латинські літери): ")
shift = 3
encrypted = ""
for ch in text:
    position = ord(ch) - ord('a')
    new_position = (position + shift) % 26
    encrypted += chr(new_position + ord('a'))

print(f'Зашифрований текст: "{encrypted}"')