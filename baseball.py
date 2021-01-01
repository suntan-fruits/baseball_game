#-*- coding:utf-8 -*-

from src.play import choose_to_start
    
if __name__=='__main__':
    while True : 
        print('게임 시작하기 : 1 \n게임 끝내기 : 2')
         
        choice = int(input('숫자를 입력하세요: '))
        choose_to_start(choice)
