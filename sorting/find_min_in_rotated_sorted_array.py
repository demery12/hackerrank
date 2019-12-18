def findMin(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[len(nums)-1]:
        return nums[0]
    i1 = 0
    i2 = (len(nums)-1)//2
    min_left = 0
    max_right = len(nums)-1
    while(nums[i1]<nums[i1+1]):
        #if the endpoints are in order, everything inside is garbage
        if(nums[i1]<nums[i2]):
            min_left = i2
            i1 = min_left
            i2 = min_left + ((max_right-min_left) //2)

        #if the endpoints are out of order, everything to the outside is irrelevant
        else:
            max_right = i2
            i2 = min_left + ((max_right-min_left) //2)

    return nums[i1+1]
