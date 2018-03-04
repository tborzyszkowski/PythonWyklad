
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


a ,b, c =  (0, 0, 0)

wynik  = ( ( "NW" if c == 0 else "BR" ) if b==0 else "Jedno"
                    if a == 0 else
            "B" if (b * b - 4 * a * c) < 0 else
                ( "Dwa"  if (b * b - 4 * a * c) > 0 else "Jedno"
                    )
           )
print wynik