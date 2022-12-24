class Solution:
    def twoSum(self, nums, target):
        dic = {}

        
        for i in xrange(0, len(nums)):
            try:
                dic[nums[i]].append(i)
            except:
                dic[nums[i]] = []
                dic[nums[i]].append(i)

        try:
            for items_1 in dic[nums[i]]:
                for items_2 in dic[target-nums[i]]:
                    if(items_1+1 != items_2+1):
                        l = []
                        if(items_2+1 > items_1+1):
                            l.append(items_1+1)
                            l.append(items_2+1)
                        else:
                            l.append(items_2+1)
                            l.append(items_1+1)
                        return l
        except:
            pass
