import Graph
from Graph import *
import unittest

adjacencyMatrix1=[[0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [1,0,0,0,1],
                  [0,1,0,0,0]]

adjacencyList1=[[1],
           [2],
           [3],
           [0, 4],
           [1]]

edgeList1=[[1, 0, 0, -1, 0, 0],
           [-1, 1, 0, 0, 0, -1],
           [0, -1, 1, 0, 0, 0],
           [0, 0, -1, 1, 1, 0],
           [0, 0, 0, 0, -1, 1]]

class KnownValues(unittest.TestCase):
    def testMatrixRecognition(self):
        testGraph = Graph(adjacencyMatrix1)
        self.assertEqual(MatrixType.ADJACENCY_MATRIX, testGraph.checkMatrixType(adjacencyMatrix1))

        testGraph = Graph(edgeList1)
        self.assertEqual(MatrixType.EDGE_LIST, testGraph.checkMatrixType(edgeList1))

        testGraph = Graph(adjacencyList1)
        self.assertEqual(MatrixType.ADJACENCY_LIST, testGraph.checkMatrixType(adjacencyList1))

    def testMatrixConversion(self):
        testGraph = Graph(adjacencyMatrix1)
        self.assertEqual(edgeList1, testGraph.getMatrix(MatrixType.EDGE_LIST))

        testGraph = Graph(adjacencyMatrix1)
        self.assertEqual(adjacencyList1, testGraph.getMatrix(MatrixType.ADJACENCY_LIST))

        testGraph = Graph(adjacencyMatrix1)
        self.assertEqual(adjacencyMatrix1, testGraph.getMatrix(MatrixType.ADJACENCY_MATRIX))

    def testIncorrectMatrix(self):
        #brakujący element
        adjacencyMatrix1=[[0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [1,0,0,0,1],
                  [0,1,0,0]]
        self.assertRaises(IncorrectMatrix, Graph, adjacencyMatrix1)

        #połączenie za samym sobą
        adjacencyMatrix1=[[0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [1,0,0,0,1],
                  [0,1,0,0,1]]
        self.assertRaises(IncorrectMatrix, Graph, adjacencyMatrix1)

        #wieksza ilosc połączen
        adjacencyMatrix1=[[0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [1,0,0,0,1],
                  [0,2,0,0,0]]
        self.assertRaises(IncorrectMatrix, Graph, adjacencyMatrix1)

        #nie poprawna krawędź
        edgeList1=[[0, 0, 0, -1, 0, 0],
           [-1, 1, 0, 0, 0, -1],
           [0, -1, 1, 0, 0, 0],
           [0, 0, -1, 1, 1, 0],
           [0, 0, 0, 0, -1, 1]]
        self.assertRaises(IncorrectMatrix, Graph, edgeList1)

        #nie poprawna krawędź
        edgeList1=[[3, 0, 0, -1, 0, 0],
           [-1, 1, 0, 0, 0, -1],
           [0, -1, 1, 0, 0, 0],
           [0, 0, -1, 1, 1, 0],
           [0, 0, 0, 0, -1, 1]]
        self.assertRaises(IncorrectMatrix, Graph, edgeList1)

        #nie poprawna krawędź
        edgeList1=[[1, 0, 0, -1, 0, 0],
           [-1, 1, 0, 0, 0, -1],
           [0, -1, 1, 0, 0, 0],
           [0, 0, -1, 1, 1, 0],
           [0, 0, 0, 0, -1]]
        self.assertRaises(IncorrectMatrix, Graph, edgeList1)

    def testMatrixFromString(self):
        string="""0 1 0 0 0 
                  0 0 1 0 0 
                  0 0 0 1 0 
                  1 0 0 0 1 
                  0 1 0 0 0 """
        testGraph=Graph(string)
        self.assertEqual(adjacencyMatrix1, testGraph.getMatrix(MatrixType.ADJACENCY_MATRIX))








