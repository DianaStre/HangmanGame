import random


def alege_cuvant():
    cuvinte = ["apple", "banana", "orange", "grape", "watermelon",
               "pineapple", "strawberry", "blueberry", "peach", "cherry"]
    return random.choice(cuvinte)


#def afiseaza_cuvant(cuvant_de_ghicit, litere_ghicite):
    #return ' '.join([litera if litera in litere_ghicite else '_' for litera in cuvant_de_ghicit])

def afiseaza_cuvant(cuvant_de_ghicit, litere_ghicite):
    rezultat = []
    for litera in cuvant_de_ghicit:
        if litera in litere_ghicite:
            rezultat.append(litera)  # Adaugă litera ghicită
        else:
            rezultat.append('_')  # Adaugă sublinierea pentru litera negicită
    return ' '.join(rezultat)


def joaca_spanzuratoarea():
    cuvant_de_ghicit = alege_cuvant()
    litere_ghicite = set()
    incercari_ramase = 6

    print("Bine ai venit la Spânzurătoarea! Ghicește cuvântul în engleză.")

    while incercari_ramase > 0:
        print(f"\nCuvânt de ghicit: {afiseaza_cuvant(cuvant_de_ghicit, litere_ghicite)}")
        print(f"Încercări rămase: {incercari_ramase}")

        ghiceste = input("Ghiceste o literă: ").lower()

        if ghiceste in litere_ghicite:
            print("Ai ghicit deja această literă!")
        elif ghiceste in cuvant_de_ghicit:
            litere_ghicite.add(ghiceste)
            print(f"Bine! Litera '{ghiceste}' este în cuvânt.")
        else:
            incercari_ramase -= 1
            print(f"Litera '{ghiceste}' nu este în cuvânt.")

        if set(cuvant_de_ghicit) == litere_ghicite:
            print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
            break
    else:
        print(f"Joc terminat! Cuvântul era: {cuvant_de_ghicit}")

    # Oferă posibilitatea de a juca din nou
    if input("\nVrei să mai joci o dată? (da/nu): ").lower() == "da":
        joaca_spanzuratoarea()


# Pornește jocul
joaca_spanzuratoarea()
