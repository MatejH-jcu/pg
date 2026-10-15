def my_zip(*oterable):



    if __name__ == "__main__":

        jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
        vek =   [   30,     20,     24,     18,     27   ]
        vaha =  [   50,     80,     90,     55,     67   ]

        vysledek = list(zip(jmena, vek, vaha))
        print(vysledek)

        vysledek = my_zip(jmena, vek, vaha)
        for jmena, vek, vaha in vysledek:
            print("f' {jmena}, je {vek} let a vazi {vaha} kg'")
        print(vysledek)

        # u zkousky implentace a jak to funguje co se stane kdyz neco zmenim 