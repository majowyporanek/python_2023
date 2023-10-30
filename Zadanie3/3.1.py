# 3.1
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# ODP: Podany kod nie jest poprawny składniowo w Pythonie gdyż: użyto zbędny nawias oraz w Pythonie nie stosujemy średników

for i in "axby": if ord(i) < 100: print(i)

# ODP: Podany kod nie jest poprawny składniowo w Pythonie gdyż po ':' brakuje przejsc do nowej linii i wciec
# Ponadto nie jest to poprawna skladnia trojargumentowa


for i in "axby": print (ord(i) if ord(i) < 100 else i)
# ODP: Podany kod jest poprawny składniowo w Pythonie, jest to poprawne użycie instrukcji warunkowej w jednej linii
