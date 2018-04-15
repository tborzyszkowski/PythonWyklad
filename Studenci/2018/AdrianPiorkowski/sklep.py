class listaz():
    nazwa=0
    ilosc=0

    def __repr__(self):
        opis=str(self.nazwa)+' '+str(self.ilosc)
        return opis

class produkty():
    cena=0
    ilosc=0

class sklep():
    produkt={}
    produkt['a']=produkty()
    produkt['a'].cena=10
    produkt['a'].ilosc=20

    produkt['b']=produkty()
    produkt['b'].cena = 10
    produkt['b'].ilosc = 20

    produkt['c']=produkty()
    produkt['c'].cena = 10
    produkt['c'].ilosc = 20

    produkt['d']=produkty()
    produkt['d'].cena=10
    produkt['d'].ilosc=20

    def kup(self,a):
        if self.produkt.has_key(a.nazwa):
            if a.ilosc<=self.produkt[a.nazwa].ilosc:
                self.produkt[a.nazwa].ilosc-=a.ilosc
                cena=self.produkt[a.nazwa].cena*a.ilosc
                a.ilosc = 0
                return cena
            else:
                cena=self.produkt[a.nazwa].cena*self.produkt[a.nazwa].ilosc
                a.ilosc-=self.produkt[a.nazwa].ilosc
                self.produkt[a.nazwa].ilosc =0
                return cena
        else:
           return 0

s=sklep()
lista={}
lista[0]=listaz()
lista[0].nazwa='a'
lista[0].ilosc=3
lista[1]=listaz()
lista[1].nazwa='d'
lista[1].ilosc=3
lista[2]=listaz()
lista[2].nazwa='c'
lista[2].ilosc=3
cena=0
for i in range(0,lista.__len__()):
    cena+=s.kup(a=lista[i])
else:
    print (cena)
    print (lista)
