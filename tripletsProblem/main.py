def solution(a=[],b=[]):
    f_player = 0
    s_player = 0 
    for i,j in zip(a,b):
        if i>j:
            f_player += 1
        elif i<j:
            s_player += 1
        else:
            pass
    return f_player,s_player


if __name__ == '__main__':
    A = str(input('Enter the player 1 score separated by space example = 1 2 4 : '))
    B = str(input('Enter the player 2 score separated by space example = 3 4 5 : '))
    As = []
    Bs = []
    try:
        for _ in A.split(' '):
            if _.isdigit() and int(_) > 1 and int(_) < 100:
                As.append(int(_))
            else:
                raise ValueError
        for _ in B.split(' '):
            if _.isdigit() and int(_) > 1 and int(_) < 100:
                Bs.append(int(_))
            else:
                raise ValueError
    except:
        print('Invalid input')
        exit()
    result = solution(As,Bs)
    
    print('Player 1 won {} times and Player 2 won {} times'.format(result[0],result[1]))