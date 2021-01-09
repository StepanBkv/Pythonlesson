def intersection(lang1, lang2):
    result = []
    for i in range(0, len(lang1)):
        for j in range(0, len(lang2)):
            if(lang1[i] == lang2[j]):
                if(lang1[i] != ''):
                    result += lang1[i]
    return result

if __name__ == '__main__':
    languages = []
    line = ''
    max = 0
    try:
        with open("input.txt", 'r') as file:
            # languages = [i.strip() for i in file]
            # languages = [(i[0: -1], int(i[-1])) for i in languages]
            languages += [i.replace("\n", " ").split(" ") for i in file]
            print(languages)
    except:
        pass
    
    for i in range(0, len(languages) - 1):
        for j in range(i + 1, len(languages)):
            intersect = intersection(languages[i], languages[j])
            if(len(intersect) + 1 > max):
                max = len(intersect) + 1

    with open("output.txt", 'w') as file:
        file.write(str(max))