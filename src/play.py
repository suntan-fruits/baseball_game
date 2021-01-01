import sys
import random

def start_game() :
    answer = random.sample(list(range(10)), 4)
    
    n = 0

    while True:
        guess_a = list(input('예상하는 숫자 4개를 입력하세요:'))
        guess = [int(i) for i in guess_a]
        
        strike = 0
        ball = 0
        n = n + 1

        for i in range(4) :
            if guess[i] in answer :
                if guess[i] == answer[i] :
                    strike = strike + 1
                else:
                    ball = ball + 1

        print(f'strike = {strike} ball = {ball}')
        
        if strike == 4 :
             print('정답입니다')
             break
        
        else :
            print(f'남은 횟수 ={10-n}')
        
        if n == 10:
            print('게임 실패')
            break
from src.game import start_game

def choose_to_start(choice):   
    if choice == 1 :
        return start_game()
    if choice == 2 : 
        return sys.exit(0)
