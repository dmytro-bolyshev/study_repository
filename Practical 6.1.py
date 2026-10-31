text = "Hello World! 6767"
Upper_list = []
Lower_list = []
Number_list = []
Punctuation_list = []
Upper = 0
Lower = 0
Numbers = 0
Spaces = 0
Punctuation = 0

for x in text:
    symbol = ord(x)
    if 65 <= symbol <= 90:
        Upper += 1
        Upper_list.append(x)
    elif 97 <= symbol <= 122:
        Lower += 1
        Lower_list.append(x)
    elif 48 <= symbol <= 57:
        Numbers += 1
        Number_list.append(x)
    elif symbol == 32 or symbol == 9:
        Spaces += 1
    elif 33 <= symbol <= 47 or 58 <= symbol <= 64 or 91 <= symbol <= 96 or 123 <= symbol <= 126:
        Punctuation += 1
        Punctuation_list.append(x)
total = Upper + Lower + Numbers + Spaces + Punctuation
print(f"Загалом символів: {total} \nВеликі літери: {Upper}, {Upper_list}\nМалі літери: {Lower}, {Lower_list}")
print(f"Чисел: {Numbers}, {Number_list}\nРозділові знаки: {Punctuation}, {Punctuation_list}\nПробіли: {Spaces}")