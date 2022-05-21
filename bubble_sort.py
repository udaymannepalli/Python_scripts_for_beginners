def sort(nums):
    for i in range(len(nums)-1, 0, -1):#outer loop and len(nums)-1, we have to reach till 0 which is first index value, -1 to reduce the values one by one
        for j in range(i): #inner loop for the first iteration we have to go till end(8), we have to start with zero and reach till 5. In the next iteration we have to go from 0 to 4, next 0 to 3...which will place the maximum values at the end.
            if nums[j]>nums[j+1]:#in this step we will find to swap or not to swap. If the first value is greater than 2nd value - swap.
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
#starting steps
nums = [5,3,8,6,7,2]
sort(nums)
print(nums)