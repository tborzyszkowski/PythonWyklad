dic = {1: "jeden", 
    2: "dwa", 
    3: "trzy", 
    4: "cztery", 
    5: "piec", 
    6: "szesc",
    7: "siedem", 
    8: "osiem", 
    9: "dziewiec", 
    0: "zero"} 

def words(i):
    text = []
    number_string = str(i)
    for digit in number_string:
        text.append(dic[int(digit)])
    return " ".join(text)

print words(input("podaj liczbe: "))
        
