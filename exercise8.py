def vokon_zählen(wort):
    vokalen = "aeiou"
    wort_lower = wort.lower ()
    
    bn = [i for i in wort_lower if i.isalpha()]
    Vn = [k for k in wort_lower if k in vokalen]
    
    print(f"Es gibt {len(Vn)} Vokalen und {len(bn) - len(Vn)} Konsonanten. ")
    
vokon_zählen("HI, &%/ Berlin!!")