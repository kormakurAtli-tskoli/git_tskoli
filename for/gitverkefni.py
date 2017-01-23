#Gitverkefni

#Valmynd
#Valmynd
valmynd = 0
while valmynd != 4:
    print("*---------- VALMYND ----------*")
    print("1 = Summa og margföldun")
    print("2 = Nafn")
    print("3 = Hástafir og lágstafir")
    print("4 = Hætta")
    print(" ")
    # Notandi slær inn valmöguleikann sem hann vill
    valmynd = int(input("Sláðu inn valmöguleikann sem þú vilt: "))
    print(" ")

    if valmynd == 1:
        summa = 0
        margfeldi = 1
        for i in range(2):
            tala = int(input("Sláðu inn tölu: "))
            summa = summa + tala
            margfeldi = margfeldi * tala
        print("Summa talnanna er",summa,"\nMargfeldi talnanna er",margfeldi)
        print(" ")

    if valmynd == 2:
        fornafn = input("Fornafn: ")
        eftirnafn = input("Eftirnafn:")
        print("Halló",fornafn,eftirnafn)