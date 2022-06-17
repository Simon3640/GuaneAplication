import os

def icecreamParlor(m, arr):
    for _ in arr:
        for j in arr:
            if _+j == m:
                return [arr.index(_)+1,arr.index(j)+1]
                break
    return [-1,-1]

if __name__ == '__main__':
    fptr = open('response.txt', 'w')
    try:
        t = int(input('Enter the number of trips to the ice cream parlor : ').strip())
        if t > 50 or t < 1:
            
            raise ValueError

        for t_itr in range(t):
            
            m = int(input(f'Enter the amount of money they have pooled : ').strip())
            
            if m < 2 or m > 1e4:
                
                raise ValueError

            arr = list(map(int, input('Enter space-separated integers denoting the cost of each flavor : ').rstrip().split()))
            
            if len(arr) < 2 or len(arr) > 1e4:
                
                raise ValueError
            
            if any(i < 1 or i > 1e4 for i in arr):
                
                raise ValueError

            result = icecreamParlor(m, arr)
            fptr.write(' '.join(map(str, result)))
            fptr.write('\n')
    except ValueError:
        print('Invalid input')


    fptr.close()