
# a ,b, c =  (1, 2, 1)

# wynik = ""
# if a == 0:
#     if b == 0:
#         if c == 0:
#             wynik = "NW"
#         else:
#             wynik = "B"
#     else:
#         wynik = "Jedno"
# else:
#     if (b * b - 4 * a * c) < 0:
#         wynik = "B"
#     else:
#         if (b * b - 4 * a * c) > 0:
#             wynik = "Dwa"
#         else:
#             wynik = "Jedno"


testy=  [(0, 0, 0, "NW"), (1, 2, 1, "Jedno")]

for t in testy:
    a, b, c, w = t
    wynik  = ( ( "NW" if c == 0 else "BR" ) if b==0 else "Jedno"
                    if a == 0 else
            "B" if (b * b - 4 * a * c) < 0 else
                ( "Dwa"  if (b * b - 4 * a * c) > 0 else "Jedno"
                    )
           )
    print wynik, w


# zamienic:
#       ( a if bool else b )
#  na:
#       (bool and [a] or [b])[0]