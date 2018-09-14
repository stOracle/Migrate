'''
Created on Apr 17, 2018

@author: srauner
'''
import random
def main():
    
    hand = [[4,'h'], [3,'s'], [6,'c'], [10,'s'], [9,'h']]
    score = hand[0][0] + hand[1][0]
    
    print("hand = ", hand)
    print()
    print("start of small loop")
    for i in range(len(hand)):
        print(hand[i][0])
    print()
    print("2 loops")
    for i in range(len(hand)):
        for j in range (len(hand[i])):
            print("i = {}; j = {}, hand[{}][{}] = {}".format(i, j, i, j, str(hand[i][j])))
    print()
    print("hand[0] = ", hand[0])
    print("hand[0][0] = ", hand[0][0])
    print("hand[1][1] = ", hand[1][1])
    print(score)
    
    
    
main()