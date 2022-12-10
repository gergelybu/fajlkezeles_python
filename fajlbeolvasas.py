import random

nevek = []
nemek = []
korok = []

def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='UTF-8')
    print(fajlom)
    # fajl_tartalma = fajlom.read()
    # print(fajl_tartalma)
    fejlec = fajlom.readline().strip()
    print(fejlec)
    # sor = fajlom.readline().strip()
    # print(sor)
    # sor = fajlom.readline().strip()
    # print(sor)
    sorok = fajlom.readlines()
    print(sorok)
    feldolgoz(sorok)
    print(f"{len(nevek)} adatsor van a fájlban!")
    atl = atlag()
    print(f"Az átlag életkor: {atl}")
    m = nem()
    print(f"{m} nő van a listában")
    j = fiatalno()
    print(f"{nevek[j]} a legfiatalabb nő")
    ujsor()
    fajlom.close()

def feldolgoz(sorok):
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split(", ")
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        print(nevek[i])
        print(nemek[i])
        print(korok[i])
        i += 1


def atlag():
    ossz = 0
    i = 0
    while i < len(korok):
        ossz += korok[i]
        i +=1
    atl = int(ossz/i)
    return atl


# Hány nő van alistában?
def nem():
    i = 0
    n = 0
    while i < len(nemek):
        if nemek[i] == "nő":
            n += 1
        i +=1
    return n

# Hány éves a legfiatalabb nő?
def fiatalno():
    i = 0
    n = 100
    j = 0
    while i < len(nemek):
        if nemek[i] == "nő":
            if korok[i] < n:
                j = i
        i += 1
    return j

# Hozz étre egy új adatsort!
#     Kérd be a felahsználótól a nevet!
#     A nemet addig kérd be, amíg a "férfi" vagy a "nő" szöveget nem adja meg! Minden más válasz esetén kérd be újra a nem értékét! és a nemet.
#     A kor értékének beállításához generálj egy véletlen számot 10 és 80 között!

def ujsor():
    nev =input("adj meg egy nevet! ")
    neme = input("Férfi vagy nő? ")
    # kor =(random.Random()*80)+10
    print(nev, neme, kor)
# Az új adatsort csatold a meglévő fáj végére!