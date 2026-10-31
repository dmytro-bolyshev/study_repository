text = input("Введіть рядок англійською: ")
left, right = 0, len(text) - 1
palindrome = True

while left < right:
    a = ord(text[left])
    b = ord(text[right])
    if not (65 <= a <= 90 or 97 <= a <= 122):
        left += 1
        continue
    if not (65 <= b <= 90 or 97 <= b <= 122):
        right -= 1
        continue

    if 65 <= a <= 90:
        a += 32
    if 65 <= b <= 90:
        b += 32

    if a != b:
        palindrome = False
        break

    left += 1
    right -= 1
if palindrome == True:
    print("Паліндром")
else:
    print("Не паліндром")