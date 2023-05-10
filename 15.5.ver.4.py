# раздел 15.5 Шифр Цезаря
text_in = input()
text_1 = ''
for i in range(len(text_in)):
    if text_in[i].lower() in 'abcdefghijklmnopqrstuvwxyz ':
        text_1 += text_in[i]
text_2 = text_1.split()
text_out = ''
counter = 0


def latin_low(char_):
    a = ord(char_) + int(key)
    if a > 122:
        a = 96 + (a - 122)
    return (chr(a))


for i in range(len(text_in)):
    key = len(text_2[counter])
    if text_in[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        text_out += latin_low(text_in[i].lower()).upper()
    elif text_in[i] in 'abcdefghigklmnopqrstuvwxyz':
        text_out += latin_low(text_in[i])
    elif text_in[i] in ' ':
        text_out += text_in[i]
        counter += 1
    else:
        text_out += text_in[i]


print(text_out)
