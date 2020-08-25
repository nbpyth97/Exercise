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

nums = [8,1,2,2,3]
count = []
output = []
a = 0

for i in range(len(nums)):
    for x in nums:
        if nums[a] > x:
            count.append(1)
    output.append(len(count))
    count.clear()

    a += 1

print(output)

    


