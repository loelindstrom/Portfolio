def createGlosor(filename):
    fin = open(filename, "r")
    linesList = fin.readlines()


    glosor = dict()
    words = []
    definitions = []

    key = -1
    for line in linesList:
        if line[0] == "*":
            key = line[1:-1]
            words = []
            definitions = []
            glosor[key] = (words, definitions)


        elif line != "\n":
            glosor[key] = (words, definitions)
            start, stop = getDivider(line)
            word = line[:start]
            definition = line[stop:-1]
            glosor[key][0].append(word)
            glosor[key][1].append(definition)

        # if line!="\n":
        #     start, stop = getDivider(line)
        #     word = line[:start]
        #     definition = line[stop:]
        #     words.append(word)
        #     definitions.append(definition)

    # for word, definition in zip(words, definitions):
    #     print(word+":", definition)

    # return words, definitions

    return glosor

def getDivider(string):
    divStart = string.find(" - ")
    divStop = divStart+3
    return divStart, divStop

minaglosor = createGlosor("glosorStor.txt")

# print(minaglosor)

# for entry in minaglosor:
#     print(entry)
#     words = minaglosor[entry][0]
#     definitions = minaglosor[entry][1]
#     for word, definition in zip(words, definitions):
#             print(word+" :", definition)