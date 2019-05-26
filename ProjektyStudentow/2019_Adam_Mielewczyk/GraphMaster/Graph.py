import statistics
import copy
import time
import math
from operator import methodcaller
import colorama
from colorama import Fore, Style

class GraphError(Exception): pass
class IncorrectMatrix(GraphError): pass

from enum import Enum
class MatrixType(Enum):
    EDGE_LIST=1
    ADJACENCY_MATRIX=2
    ADJACENCY_LIST=3


# transpozycja macierzy
# wymaga poprawnej macierzy
def matrixTranspose(matrix):
    transposeMatrix=[]
    for k in range(len(matrix[0])):
        transposeMatrix.append([])
        for l in range(len(matrix)):
            transposeMatrix[k].append(matrix[l][k])
    return transposeMatrix

class Graph():
    def __init__(self,matrix):
        if(isinstance(matrix,list)):
            self.__matrix=matrix
        elif(isinstance(matrix,str)):
            self.__matrix = [list(map(int,row)) for row in list(map(methodcaller("split"),list(map(str, matrix.split("\n")))))]

        self.matrixType = Graph.checkMatrixType(self.__matrix)
        self.checkCorrectness()
        if(self.matrixType!=MatrixType.ADJACENCY_MATRIX):
            self.__matrix=self.getMatrix(MatrixType.ADJACENCY_MATRIX)
            self.matrixType=MatrixType.ADJACENCY_MATRIX
        if(self.isDirectional()):
            raise IncorrectMatrix('Grafy skierowane będą obsługiwane w przyszłości')

    def getGraphicPosition(self,squareSize):
        vertexRadius=28
        radius=(squareSize)/2-vertexRadius
        radiansDistanceBetweenVertex=2.0*math.pi/self.vertexCount()
        vertexsPosition=[[2*radius+2*vertexRadius-(radius*math.cos(i*radiansDistanceBetweenVertex)+radius+vertexRadius),
                        2*radius+2*vertexRadius-(radius*math.sin(i*radiansDistanceBetweenVertex)+radius+vertexRadius)] for i in range(self.vertexCount())]
        edgeListT=matrixTranspose(self.getMatrix(MatrixType.EDGE_LIST))
        edgesPositions=[]
        for i  in range(len(edgeListT)):
            temp=[]
            temp.append(vertexsPosition[edgeListT[i].index(1)][0])
            temp.append(vertexsPosition[edgeListT[i].index(1)][1])
            temp.append(vertexsPosition[edgeListT[i].index(-1)][0])
            temp.append(vertexsPosition[edgeListT[i].index(-1)][1])
            edgesPositions.append(temp)
        graphPositions=[]
        graphPositions.append(vertexsPosition)
        graphPositions.append(edgesPositions)
        return graphPositions

    #TODO
    def __eq__(self, other):
        pass

    def __invert__(self, other):
        pass
    def __add__(self, other):
        pass

    def __str__(self):
        string=""
        for i in self.__matrix:
            for j in i:
                string+=(str(j)+" ")
            string+="\n"
        return string


    @staticmethod
    def checkMatrixType(matrix):
        isEdgeList=0
        for row in matrix:
            if(row.count(-1)!=0):
                isEdgeList=1
                break
        if(isEdgeList):
            return MatrixType.EDGE_LIST
        isAdjacencyList=0
        for row in matrix:
            for element in row:
                if(element>1):
                    isAdjacencyList=1
                    break
            if(isAdjacencyList):
                isAdjacencyList=1
                break
        if(isAdjacencyList):
            return MatrixType.ADJACENCY_LIST
        if(len(matrix)==len(matrix[0])):
            return MatrixType.ADJACENCY_MATRIX

    def checkCorrectness(self):
        if(self.matrixType==MatrixType.ADJACENCY_MATRIX):
            for i in range(len(self.__matrix)):
                if(len(self.__matrix)!=len(self.__matrix[i])):
                    raise IncorrectMatrix('Brakuje elementów w macierzy')
                for j in range(len(self.__matrix[i])):
                    if(not(self.__matrix[i][j] == 0 or self.__matrix[i][j] == 0 if i == j else 1)):
                        raise IncorrectMatrix('Nie poprawne wartości w macierzy')
        elif(self.matrixType==MatrixType.ADJACENCY_LIST):
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    if(not(self.__matrix[i][j] in range(len(self.__matrix)) and self.__matrix[i][j] != i)):
                        raise IncorrectMatrix('Nie poprawne wartości w macierzy')
        elif(self.matrixType==MatrixType.EDGE_LIST):
            for i in range(len(self.__matrix)):
                if(len(self.__matrix)!=len(self.__matrix[i])):
                    raise IncorrectMatrix('Brakuje elementów w macierzy')
            tempMatrix=matrixTranspose(self.__matrix)
            for row in tempMatrix:
                if(not(row.count(1)==1 and row.count(-1)==1 and row.count(0)==len(tempMatrix)-2)):
                    raise IncorrectMatrix('Nie poprawne wartości w macierzy')

    def isDirectional(self):
        for i in range(0,len(self.__matrix)):
            for j in range(i,0,-1):
                if(self.__matrix[i][j]!=self.__matrix[j][i]):
                       return 1

    #liczy wierzchołki grafu
    def vertexCount(self):
        return len(self.__matrix)

    def getMatrix(self, toType):
        if(self.matrixType==toType):
            return self.__matrix
        #TODO sprawdzenie zmiany prędkości wykonywania sprawdzenia izomorficznośći na listach
        if(self.matrixType==MatrixType.ADJACENCY_MATRIX and toType==MatrixType.EDGE_LIST):
            tempMatrix=[] #macierz wymagająca transpozycji
            for i in range(self.vertexCount()):
                for j in range(self.vertexCount()):
                    if(self.__matrix[i][j]!=0):
                        tempMatrix.append(tuple((0 if (k!=i and k!=j) else 1 if k==i else -1) for k in range(self.vertexCount())))
            newMatrix=matrixTranspose(tempMatrix)
            return newMatrix

        if(self.matrixType==MatrixType.ADJACENCY_MATRIX and toType==MatrixType.ADJACENCY_LIST):
            newMatrix=[]
            for i in range(self.vertexCount()):
                newMatrix.append([])
                for j in range(self.vertexCount()):
                    if(self.__matrix[i][j]!=0):
                        newMatrix[i].append(j)
            return newMatrix

        if(self.matrixType==MatrixType.ADJACENCY_LIST and toType==MatrixType.ADJACENCY_MATRIX):
            newMatrix=[]
            for i in range(self.vertexCount()):
                newMatrix.append([])
                for j in range(self.vertexCount()):
                    newMatrix[i].append(1 if j in self.__matrix[i] else 0)
            return newMatrix



        if(self.matrixType==MatrixType.EDGE_LIST and toType==MatrixType.ADJACENCY_MATRIX):
            tempMatrix=list(map(list, zip(*self.__matrix)))
            newMatrix=[[0 for i in range(self.vertexCount())]for j in range(self.vertexCount())]
            for k in range(len(self.__matrix[0])):
                i=tempMatrix[k].index(1)
                j=tempMatrix[k].index(-1)
                newMatrix[i][j]=1
            return newMatrix

        #TODO zrobić bezpośrednie przejśćia

        if(self.matrixType==MatrixType.EDGE_LIST and toType==MatrixType.ADJACENCY_LIST):
            tempMatrix=self.getMatrix(MatrixType.ADJACENCY_MATRIX)
            return self.getMatrix(MatrixType.ADJACENCY_LIST)

        if(self.matrixType==MatrixType.ADJACENCY_LIST and toType==MatrixType.EDGE_LIST):
            tempMatrix=self.getMatrix(MatrixType.ADJACENCY_MATRIX)
            return self.getMatrix(MatrixType.EDGE_LIST)


    #obliczanie ilości krawędzi
    #ilość krawędzi to ilość wszystkich możliwych krawędzi - ilość braku krawędzi
    #to podejście uwzględnia zapis innych liczb od 1 jako krawędzie
    def edgeCount(self):
        return int((self.vertexCount() ** 2 - sum([row.count(0) for row in self.__matrix]))/2)

    def getDegree(self,vertex):
        return self.vertexCount() - vertex.count(0)

    #oblicznie wszystkich stopni
    #użycie wyrażenia generującego do utworzenia listy stopni
    def getDegrees(self):
        return [self.getDegree(vertex) for vertex in self.__matrix]

    #obliczanie średniego stopnia
    #statistics.mean() - funkcja licząca średnią z elementów listy (w tym przypadku stopni wierzchołków)
    def getAverageDegree(self):
        return statistics.mean(self.getDegrees())

    #sprwdzanie czy ścieżka
    #z twierdzenia że ścieżka ma 2 wierchołki stopnia 1 i resztę stopnia 2
    def isPathGraph(self):
        return (self.getDegrees().count(2) == (self.vertexCount() - 2)) & (self.getDegrees().count(1) == 2)

    #sprawdzanie czy graf pełny
    #z twierdzenia że każdy wierzchołek musi być połączony z każdym innym
    def isCompleteGraph(self):
        return self.getAverageDegree() == self.vertexCount() - 1

    #sprawdzanie czy graf jest cyklem
    #z twierdzenia że cykl musi mieć wszystkie stopnie równe 2
    def isCycleGraph(self):
        return self.getDegrees().count(2) == self.vertexCount()

    #sprawdzanie czy graf jest drzewem
    #drzewo ma o jedną krawędz mniej od ilości wierzchołków oraz nie zawiera nie połączonych wierzchołków
    ## nie zaaktualizoane po zmianie edgeCount
    def isTree(self):
        return (self.edgeCount()==(self.vertexCount()-1)) & (self.getDegrees().count(0)==0)

class GraphGenerator():
    def edgeCountInFullGraph(self,vertexCount):
        return int(vertexCount*(vertexCount-1)/2)

    # Przyjmuje macierze krawędzi
    def checkIsomorphic(self, matrix, matrix2):
        # nie ma sensu sprawdzać jeśli liczba krawędzi lub wierzchołków się nie zgadza
        if (len(matrix)!=len(matrix2)):
            return 0
        elif (len(matrix[0])!=len(matrix2[0])):
            return 0
        else:
                    isDiffrentFromAll=1
                    # przgotuj wszystkie permutacje wierzchołków
                    P=self.getAllPermutation(list(range(0,len(matrix))))
                    # iteracja po permutacjach
                    for l in range(len(P)):
                        isDiffrent=0
                        # zapisuje permutacja wierzchołków macierzy
                        testMatrix=[]
                        for m in range(len(matrix)):
                            testMatrix.append([])
                            for n in range(len(matrix2[0])):
                                testMatrix[m].append(matrix[P[l][m]-1][n])

                        # wykonuje transpozycje żeby łatwo posprawdzać czy zawiera dane krawędzie
                        # użycie funkcji mocno spowalnia
                        #tTempMatrix=matrixTranspose(matrix2)
                        #tTestMatrix=matrixTranspose(matrix)
                        tTempMatrix=[]
                        for k in range(len(matrix2[0])):
                            tTempMatrix.append([])
                            for l in range(len(matrix2)):
                                tTempMatrix[k].append(matrix2[l][k])

                        tTestMatrix=[]
                        for k in range(len(testMatrix[0])):
                            tTestMatrix.append([])
                            for l in range(len(testMatrix)):
                                tTestMatrix[k].append(testMatrix[l][k])

                        for m in range(len(matrix2[0])):
                            if(not(tTestMatrix[m] in tTempMatrix)):
                                #różni się od tego co aktualnie mam
                                isDiffrent=1
                                break

                        #jeśli wyszło że jest taki sam co jakiś graf [i] to na pewno dalej już nie ma co sprawdzać
                        if(isDiffrent==0):
                            isDiffrentFromAll=0
                            break

                    return isDiffrentFromAll





    def decimalToInvertedBinList(self,decimal,length):
        invertedBin=[]
        while (decimal!=0):
            invertedBin.append(decimal%2)
            decimal//=2
        for i in range(length-len(invertedBin)):
            invertedBin.append(0)
        return invertedBin


    def getAllPermutation(self,P):
        out=1
        allPermutations=[]
        elements=len(P)
        while out:
            allPermutations.append(copy.deepcopy(P))
            i=elements-1
            while(P[i-1]>=P[i]):
                i-=1
                if(i==0):
                    return allPermutations
            j=elements-1
            while ( j>i and P[j]<=P[i-1] ):
                j-=1
            P[i-1], P[j] = P[j], P[i-1]

            newPart=[]
            for k in range(elements-i):
                newPart.append(P[elements-(k+1)])
            newP=[]
            for k in range(elements):
                if(i>k):
                    newP.append(P[k])
                else:
                    newP.append(newPart[k-i])
            P=newP

    def findAllNotIsomorphic(self,vertexCount):
        #rozpoczynam odmierzanie czasu
        start = time.time()
        # Lista (pierwszy wymiar określa ilość krawędzi) z listami grafów zapisanych w postaci macierzy krawędzi
        # wstępne uzupełnienie
        notIsomorphicGraphs=[[] for i in range(self.edgeCountInFullGraph(vertexCount)+1)]
        # okręlenie ilości kombinacji
        print(f"Wykonane zostanie {2**self.edgeCountInFullGraph(vertexCount)} iteracji")
        # uśpienie aby uzytkownik zobaczył długość procesu
        #time.sleep(1)
        # numer iteracji jest kombinacją reprezentującą dolny trójkąt w macierzy sąsiedztwa
        for currentCombination in range(2**self.edgeCountInFullGraph(vertexCount)):
            # informacja o postępie
            if (currentCombination%10==0):
                print(Fore.BLUE+"kombinacaja",currentCombination)
            # zapisuje aktualną kombinacje binarnie ale odwrotnie, szybciej i nie ma znaczenia na wynik
            edgeOccur=self.decimalToInvertedBinList(currentCombination,self.edgeCountInFullGraph(vertexCount))
            # przyszła macierz krawędzi
            tempMatrix=[] #macierz wymagająca transpozycji
            # potrzebne by sprawdzić następną krawędź gdy pętle jeżdżą po dolnym trójkącie macierzy
            edgeNumber=0
            # pierwsze indeksy macierzy sąsiedztwa (te po lewej)
            for i in range(vertexCount-1):
                # prawe indeksy tworzące dolny trójkąt macierzy sąsiedztwa
                for j in range(i+1):
                    # do macierzy krawędzi zapisuje tylko te krawędzie które występują
                    if(edgeOccur[edgeNumber]!=0):######## dla siekowanych               ELSE -1
                        tempMatrix.append(tuple((0 if (k!=i+1 and k!=j) else 1 if k==i+1 else 1) for k in range(0,vertexCount)))
                    edgeNumber+=1

            # transponuje tylko niepuste macierze
            if(tempMatrix!=[]):
                newMatrix=[]
                for k in range(len(tempMatrix[0])):
                    newMatrix.append([])
                    for l in range(len(tempMatrix)):
                        newMatrix[k].append(tempMatrix[l][k])
                tempMatrix=newMatrix

            if(len(tempMatrix)==0):
                notIsomorphicGraphs[len(tempMatrix)].append(tempMatrix)
            elif (notIsomorphicGraphs[len(tempMatrix[0])]==[]):
                notIsomorphicGraphs[len(tempMatrix[0])].append(tempMatrix)
            else:
                #pętla po wszystkich zebranych grafach o ilości wierzchołków aktualnie sprawdzanej macierzy

                for i in range(len(notIsomorphicGraphs[len(tempMatrix[0])])):
                    currentMatrix=notIsomorphicGraphs[len(tempMatrix[0])][i]
                    isDiffrentFromAll=self.checkIsomorphic(currentMatrix,tempMatrix)
                    if (isDiffrentFromAll==0):
                        break

                if (isDiffrentFromAll):
                    notIsomorphicGraphs[len(tempMatrix[0])].append(tempMatrix)
        end = time.time()
        print(Fore.RED+"Wykonano w czasie",end - start)
        return notIsomorphicGraphs


gen = GraphGenerator()
wynik=gen.findAllNotIsomorphic(3)
for i in range(len(wynik)):
    ile=0
    print(Fore.WHITE+f"\nGrafy o {i} krawędziach",Fore.GREEN)
    if(len(wynik[i])!=0):
        for j in range(len(wynik[i])):
            if(len(wynik[i][j])!=0):
                for k in range(len(wynik[i][j])):
                    print(wynik[i][j][k])
            else:
                print(wynik[i][j])
            print("\n")
    else:
        print(wynik[i])
    print("\n")




""" rekurencyjne szukanie permutacji
def permutacja(k,P):
    if (k==1):
        print(P)
        #allPermutations.append(copy.deepcopy(P))
    else:
        for i in range(0,k):
            nP=copy.deepcopy(P)
            nP[i], nP[k-1] = nP[k-1], nP[i]
            permutacja(k-1,nP)

print(permutacja(len(P),P))
print(allPermutations)
"""


