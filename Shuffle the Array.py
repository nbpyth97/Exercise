from random import randrange, randint

'''letcode'''

# =============================================================================
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# =============================================================================


def problem():
    global array,limit,final
    
    array = []
    final =[]
    limit = int(input(":"))
    
    while (limit % 2) != 0 or limit <= 3:
        limit = int(input(":")) 
    
    for i in range(limit):
        nums = randint(0,10)
        array.append(nums)
        
    print(array)
problem()

def lala():
    
    i = 0
    a = int((len(array)/2))
    
    while i < int(limit/2):
        x = array[i]
        y = array[a]
        
        final.append(x)
        final.append(y)
        print(x)
        print(y)
        i += 1
        a += 1
    print(final)        
lala()



