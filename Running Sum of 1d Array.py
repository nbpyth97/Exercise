

class Solution:
    def runningSum():
        nums = [1,2,3,4]
        output =[nums[0],]
        i = 0
        x = 1
        for a in range(len(nums)-1):
            add = output[i] + nums[x]
            output.append(add)

            
            i += 1
            x += 1
    runningSum()

