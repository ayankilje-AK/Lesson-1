class Pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num],i)
            lookup[num] = i
value = int(input("Enter a integer: "))
print("index1=%d, index2=%d" % Pair_elements().twoSum((10,20,30,40,50,60,70),value))