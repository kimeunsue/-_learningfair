Front="""                *******                
             **         **          
            **    ㅡㅡ   **         
           **     l       **       
           *      lㅡ      *       
           **     l       **   
            **    l      **         
             **         **
                *******
     """

Back="""                *******
             **         **
            **    ㅡ     **
           **    ㅣ ㅣ    ** 
           *     ㅣㅡ      *
           **    ㅣ ㅣ    **
            **     ㅡ    **
             **         **
                *******
      """

game= """                *******                 *******
             **         **           **         **
            **    ㅡㅡ   **         **    ㅡ     **
           **     l       **       **    ㅣ ㅣ    ** 
           *      lㅡ      *       *     ㅣㅡ      *
           **     l       **       **    ㅣ ㅣ    **
            **    l      **         **     ㅡ    **
             **         **           **         **
                *******                 *******
       """
chance=0

print(game)

print("동전 던지기 게임에 오신 것을 환영합니다.")

while True:
    import random
    coin=random.randint(0,1)
    choice=int(input("친구와 누가 더 많이 맞힐지 겨뤄보세요! 기회는 10번입니다  0:앞면, 1:뒷면 \n"))
     
    
    print("던진 동전: ")
    if coin==0:
        print(Front)
    else:
        print(Back)

    print("나의 선택: ")
    if choice==0:
        print(Front)
    else:
        print(Back)

    print("던진 동전과 나의 선택의 결과: ")
    chance+=1
    if coin==choice:
        print("맞혔습니다.실행 횟수=", chance)
       
    else:
        print("틀렸습니다. 실행 횟수=", chance)

    

    if chance>9:
        break
