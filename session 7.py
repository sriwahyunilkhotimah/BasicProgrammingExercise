while(True):
    print("menu")
    print("1. menghitung luas segitiga")
    print("2. menghitung luas persegi panjang")
    print("3. menghitung ganjil dan genap")
    print("4. keluar aplikasi")
    menu=input("masukan menu pilihan anda")
    if(menu=="1"):
        
        a = float(input("masukan panjang alas : "))
        t = float (input("masukan tinggi segitiga : "))
        luas = 0.5*a*t
        print("luas segitiga adalah : "+ str (luas))

    if(menu=="2"):
        p = float(input("masukan panjang ps : "))
        L = float (input(" masukan lebar ps : "))
        luas = p*L
        print("luas persegi panjang adalah : " +str (luas))

    if(menu=="3"):
        number = int (input ("number : "))
        if number % 2 ==0 :
            print(f"{number} is even")
        else :
            print(f"{number} is odd")

    if(menu=="4"):
        break