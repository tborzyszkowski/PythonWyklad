#!/usr/bin/env python3

def dotproduct(*vectors):
    return sum(a*b for a,b in zip(vectors[0], vectors[1]))

def main():
    # https://www.wolframalpha.com/input/?i=dotproduct+of+%5B2,1,5%5D++%5B2,6,6%5D
    print("Should be 40")
    print(dotproduct([2, 1, 5],[2, 6, 6]))

if __name__ == "__main__":
    main()
