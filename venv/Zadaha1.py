answers = []
with open("input", 'r') as file:
      answers += [i.replace("\n", " ").split(" ") for i in file]
str = ""
bool = 0


for j in answers[0]:
    l = list(j)
    lenl = len(l)
    lenlrange = lenl
    for elem in l:
        if (((ord(elem) < 97) | (ord(elem) > 122)) & ((ord(elem) < 65) | (ord(elem) > 90))):
            lenlrange -= 1
    if (lenlrange >= 26):
        lenlrange = (lenl - (26 * (lenl // 26)))
    for i in range(lenl):
        if (l[i] == "#"):
            bool = 1
        if ((((ord(l[i]) >= 97) & (ord(l[i]) <= 122)) | ((ord(l[i]) >= 65) & (ord(l[i]) <= 90)))):
            if (lenlrange > 0) & (l[i] == 'z'):
                l[i] = 'a'
                l[i] = chr(ord(l[i]) + lenlrange - 1)
            elif (lenlrange > 0) & (l[i] == 'Z'):
                l[i] = 'A'
                l[i] = chr(ord(l[i]) + lenlrange - 1)
            else:
                if ord(l[i]) <= 90:
                    if ord(l[i]) + lenlrange > 90:
                        l[i] = chr(65 + ord(l[i]) + lenlrange - 91)
                    else:
                        l[i] = chr(ord(l[i]) + lenlrange)
                elif ord(l[i]) <= 122:
                    if (ord(l[i]) + lenlrange > 122):
                        l[i] = chr(97 + ord(l[i]) + lenlrange - 123)
                    else:
                        l[i] = chr(ord(l[i]) + lenlrange)
            str += l[i]
        else:
            str += l[i]
    str += " "

with open("output", 'w') as file:
    file.write(str)
