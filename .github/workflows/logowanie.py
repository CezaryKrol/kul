uzytkownik = {}
status = ""

def displayMenu():
    status = input("Jestes zarejestrowany? t/n? ")
    if status == "t":
        zarejestrowany()
    elif status == "n":
        nowy()

def nowy():
    stworzLogin = input("Stworz login: ")

    if stworzLogin in uzytkownik:
        print("\nLogin utworzony!\n")
    else:
        podajHaslo = input("Stworz haslo: ")
        uzytkownik[stworzLogin] = podajHaslo
        print("\nUzytkownik utworzony\n")

def zarejestrowany():
    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")

    if login in uzytkownik and uzytkownik[login] == haslo:
        print("\nZalogowany!\n")
    else:
        print("\nZla nazwa uzytkownika lub haslo!\n")

while status != "q":
    displayMenu()
