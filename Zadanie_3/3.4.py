# ZADANIE 3.4
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i
# wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:
    x = input("Podaj liczbe rzeczywista: ")
    if x == "stop":
        break
    try:
        x = float(x)
    except ValueError:
        print("To nie jest liczba!")
    else:
        print(x, pow(x, 3))
