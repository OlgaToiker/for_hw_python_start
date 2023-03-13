poem_1 = "пара-ра-рам рам-пам-папам па-ра-па-дам"

def rhyme(poem):
    poem = poem.upper().split()
    lst = [sum(i in "ЁУЕЫАОЭЯИЮ" for i in phrase) for phrase in poem]
    if len(set(lst)) == 1:
        res = "Парам пам-пам"
    else:
        res = "Пам парам"
    print(res)

rhyme(poem_1)