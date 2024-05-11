import secrets

# if __name__ == "__main__":

#     def menu():
#         positionToDelte = []
#         positionPawn =[0,0]
#         size = int(input("Podaj wymiar planszy(szerokość i wysokość są takie same): "))
#         board = [[' ' for x in range(size)] for y in range(size)]
#         hetman = int(input(f"Podaj ilośc hetmanów które mają pokazać się na planszy liczba nie może być większa niż{(size**2)-1}: "))
#         print("1 - Zamiana hetmana na inną randomową pozycje\n 2 - ")
#         choice = int(input("Wybierz opcje która chcesz wykonać: "))
#         match choice:
#             case 1:
#                 print("XD")
#             case 2:
#                 print("xd")
#             case _:
#                 print("Wybrano niepoprawna cyfrę :( Proszę wpisać liczbę z zakresu: )")


if __name__ == "__main__":
    hetman = 5
    size = 8
    positionPawn = [0, 0]
    board = [[' ' for x in range(size)] for y in range(size)]
    positionToDelte = []


def createPlaces(size, board, hetman, pawn=0):     # create board with pawn or hetmans
    if pawn == 1:
        whatIsIt = 'P'
        xy = [secrets.randbelow(size), secrets.randbelow(size)]

    else:
        whatIsIt = 'H'
        xy = [secrets.randbelow(size), secrets.randbelow(size)]

    if board[xy[0]][xy[1]] == 'H' or board[xy[0]][xy[1]] == 'P':
        createPlaces(size, board, hetman)

    board[xy[0]][xy[1]] = whatIsIt
    return xy


def changePawn(size, board, position):
    board[position[0]][position[1]] = ' '
    return createPlaces(size, board, 0, 1)


# create Pawn 1st pawn and also chage position of pawn
positionPawn = changePawn(size, board, positionPawn)


def createHetman(size, board, n):
    positions = []
    for i in range(n):
        positions.append(createPlaces(size, board, 1))
    print(positions)
    return positions


# create Hetmans and storage theit positions in 2 D array
positionsHetman = createHetman(size, board, hetman)


positionToDelte = [int(input("PODAJ OS Y (wartośći od góry liczone): ")), int(
    input("PODAJ OS X (wartośći od góry lewej): "))]


def changeHetmans(positions, position, board, size):
    for i in range(len(positions)):
        if positions[i][0:len(positions[0])] == position[0:len(position)]:
            positions.pop(i)
            break
        else:
            return "Podano złe wartości taki Hetman nie Istnieje"

    board[position[0]][position[1]] = 'D'
    positions.append(createPlaces(size, board, 1))
    return positions


positionsHetman = changeHetmans(positionsHetman, positionToDelte, board, size)


def printBoard(size):  # printing a board with X elements in row
    for i in range(size):
        print(board[i][0:size])


printBoard(size)


def bicie():
    pass