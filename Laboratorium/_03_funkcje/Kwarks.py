def fcja(x=1, *arguments, **keywords):
    print(arguments)
    print(keywords)


fcja(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, a=11, b=12, c=13)
