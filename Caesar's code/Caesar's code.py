def shifrator_en(text, k_text):
    cnt = 0
    text_2 = ""
    for i in range(len(text)):
        if len(k_text) > 0:
            k = len(k_text[cnt])
        if text[i].isalpha() and text[i] == text[i].upper():
            if ord(text[i]) + k > 90:
                text_2 += chr(65 + (ord(text[i]) + k - 90) - 1)
            else:
                text_2 += chr(ord(text[i]) + k)
        elif text[i].isalpha() and text[i] == text[i].lower():
            if ord(text[i]) + k > 122:
                text_2 += chr(97 + (ord(text[i]) + k - 122) - 1)
            else:
                text_2 += chr(ord(text[i]) + k)
        else:
            if text[i - 1].isalpha() and cnt < len(k_text) - 1:
                cnt += 1
            text_2 += text[i]
    return text_2


text = input()

text2 = text.split()
k_text = []
for c in text2:
    h = ""
    for i in range(len(c)):
        if c[i].isalpha():
            h += c[i]
        else:
            continue
    k_text.append(h)
    k_text = [c for c in k_text if len(c) > 0]


print(shifrator_en(text, k_text))
