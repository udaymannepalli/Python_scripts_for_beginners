def sort(nums):
    for i in range(5):#first loop we have to reach till 4
        minpos = i #when i start with 0 it is 0 and it will reach till 4 
        for j in range(i,6): #nested loop, after every iteration we are creating sorted array and we have to readuce our unsorted array. start with i and end with 6 as we have 6 values
            if nums[j]<nums[minpos]:#only thing is we have to find the min value, we defined min value i starting with 5 and we will find the min value and swap accordingly
                minpos = j#the moment you find the value which is less that minpos we will change the position 

        temp = nums[i]     # we are taking 3rd variable temp for swapping and doing it for i because we need a fixed value after outer loop iteration. If we do it for j it keeps on swapping and never ends.   
        nums[i] = nums[minpos] #this will result in sorted array
        nums[minpos] = temp
        print(nums)
#starting steps
nums = [5,3,8,6,7,2]
sort(nums)
print(nums)