import random

print("""\t\t\t\t\t\t\t\t\t\t==============================
\t\t\t\t\t\t\t\t\t\t       ŞİFRE OLUŞTURUCU
\t\t\t\t\t\t\t\t\t\t==============================""")
print("DİKKAT: BÜYÜK VE KÜÇÜK HARFLER OLMALIDIR")
u = "_______________________________________________________"
print("")
bh = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş",
      "T", "U", "Ü", "V", "Y", "Z"]
BH = random.choice(bh)
kh = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş",
      "T", "U", "Ü", "V", "Y", "Z"]
kh = [alfabe.lower() for alfabe in kh]
KH = random.choice(kh)

sa = ["0", "1", "2", "3", "4""5", "6", "7", "8", "9", "10"]
SA = random.choice(sa)

sem = ["<*", "+>", "!.", "',", "%;", "/_", ":-", "&^", "+#", "=/", "-*", "_'"]
SEM = random.choice(sem)

#hane = str(input("Şifreniz kaç haneli olsun :"))
#print(u)

bh = input("Büyük harf olsunmu? :")
print(u)
if bh == "evet":

    kh = input("Küçük harf olsunmu? :")
    print(u)
    if kh == "evet":
        sa = input("Sayı olsunmu? :")
        print(u)
        if sa == "evet":
            sem = input("Sembol olsunmu? :")
            print(u)
            if sem == "evet":
                tum = [SA + KH + SEM + BH + KH + SEM]
                tim = random.choice(tum)
                tam = ["123", "asVer", "kaRa", "kuf", "tars", "As", "lAs", "Adil", "keh", "MEhter"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)
            elif sem == "hayır":
                tum = [SA + KH + BH + KH]
                tim = random.choice(tum)
                tam = ["123", "asVer", "kaRa", "kuf", "tars", "As", "lAs", "Adil", "keh", "MEhter"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)

        elif sa == "hayır":
            sem = input("Sembol olsunmu? :")
            print(u)
            if sem == "evet":
                tum = [SEM + KH + BH + KH]
                tim = random.choice(tum)
                tam = ["aester", "kaadfer", "kfaus", "toreopfk", "mestrs", "lesös", "oldil", "keh", "mesahter",
                       "kerdeh", "balela"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)
            elif sem == "hayır":
                tum = [KH + BH + KH]
                tim = random.choice(tum)
                tam = ["aester", "kaadfer", "kfaus", "toreopfk", "mestrs", "lesös", "oldil", "keh", "mesahter",
                       "kerdeh", "balela"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)


        elif kh == "hayır":
            sa = input("Sayı olsunmu? :")
            print(u)
        if sa == "evet":
            sem = input("Sembol olsunmu? :")
            print(u)
            if sem == "evet":
                tum = [SA + SEM + SEM]
                tim = random.choice(tum)
                tam = ["123", "SEDRAR", "KATRET", "CEDCİV", "MEYRITY", "KETOR", "LİWOS", "MAROIT", "ESERK", "LEWİES",
                       "LOQEX"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)

        elif sa == "hayır":
            if sem == "evet":
                tum = [KH + SEM + KH + SEM]
                tim = random.choice(tum)
                tam = ["asmaver", "aemkra", "gkuef", "tertars", "maswert", "lieas", "admuil", "kehtuy"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)


elif bh == "hayır":
    kh = input("Küçük harf olsunmu? :")
    print(u)
    if kh == "evet":
        sa = input("Sayı olsunmu? :")
        print(u)
        if sa == "evet":
            sem = input("Sembol olsunmu? :")
            print(u)
            if sem == "evet":
                tum = [SA + KH + SEM + KH]
                tim = random.choice(tum)
                tam = ["123956", "asverde", "karada", "kufter", "tarsman", "aslan", "lasna", "adilc", "kehre"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)

    elif kh == "hayır":
        sa = input("Sayı olsunmu? :")
        print(u)
        if sa == "evet":
            sem = input("Sembol olsunmu? :")
            print(u)
            if sem == "evet":
                tum = [SA + SEM]
                tim = random.choice(tum)
                tam = ["123956", "512364"]
                tem = random.choice(tam)
                print(f"şifreniz:",tim + tem)


            elif sem == "hayır":
                tum = [SA + KH + KH]
                tim = random.choice(tum)
                tam = ["123", "asver", "kara", "kuf", "tars", "as", "las", "adil", "keh"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)


        elif sa == "hayır":
            sem = input("Sembol olsunmu? :")
            print(u)
            if sem == "evet":
                tum = [SA + KH + SEM + KH + SEM]
                tim = random.choice(tum)
                tam = ["123", "asver", "kara", "kuf", "tars", "as", "las", "adil", "keh"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)

            elif sem == "hayır":
                tum = [SA + KH + KH]
                tim = random.choice(tum)
                tam = ["123", "asver", "kara", "kuf", "tars", "as", "las", "adil", "keh"]
                tem = random.choice(tam)
                print(f"şifreniz:", tim + tem)




else:
    print("Gerekli olanları girin ")
