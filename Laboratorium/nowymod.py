def liczbaZnakow(napis):
    x=open(napis, 'r') #zmienna x pod ktora zostal utworzony obiekt
    z=x.read() # zmienna w ktora czyta obiekt
    print 'Liczba znakow w pliku wynosi: ', len(str(z))

liczbaZnakow(r'D:\users\tomek\UG\Zajecia\Python\Wyklad\src\lab\aaa.txt')

def liczbaLini(napis):
    x=open(napis, 'r') #zmienna x od ktra zostal utworzony obiekt
    z=x.readlines() # zmienna w ktora czyta obiekt, f-cja readline
#zrzuca tresc pliku do listy a nastepnie dzieli na nowe linie
    print 'Liczba lini w pliku wynosi: ', len((z))

liczbaLini(r'D:\users\tomek\UG\Zajecia\Python\Wyklad\src\lab\aaa.txt')

def test(napis):
    liczbaZnakow(napis)
    liczbaLini(napis)

test(r'D:\users\tomek\UG\Zajecia\Python\Wyklad\src\lab\aaa.txt')
