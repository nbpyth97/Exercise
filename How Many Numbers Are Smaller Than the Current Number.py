# =============================================================================
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# =============================================================================


def problem(array):
    a = 0
    b = 0
    i = 0
    Sum = int()
    output = []
    for i in range(int(len(array))-1):
        if array[0] != array[b]:
            if array[0] > array[b]:
               Sum = Sum + 1
        b = b + 1
    output.append(Sum)
    print(output)
problem([8,1,2,2,3])
    


