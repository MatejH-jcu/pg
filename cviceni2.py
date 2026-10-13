def vynasob_xty_prvek(seznam, x, nasobek):


    if len(seznam) < x:
        print("V seznamu není tolik prvků")
        return seznam

    x -= 1
    if x < 0:
        print("index mensi nez 0")
        return seznam
    
    seznam[x] *= nasobek
    return seznam


def spocitej_součet(seznam):
    pocet = len(seznam)
    if pocet <= 0:
        print("Seznam je prázdný")
        return None
    suma = sum(seznam)
    return suma / pocet 

    
if __name__ == "__main__":
    seznam = vynasob_xty_prvek([1, 2, 3, 4, 5], 3, 10)
    print(seznam)
    prumer = spocitej_součet(seznam)
    print(prumer)

def formatuj_text(student):
    prumer = round(student['prumer'], 1)
    return f"Student: {student['jmeno']} {student['prijmeni']}, Vek: {student['vek']} let, prumer: {prumer}"
if __name__ == "__main__":
    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }

    student['prumer'] = spocitej_součet(student['znamky'])
print(formatuj_text(student))