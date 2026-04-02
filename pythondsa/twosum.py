class solutions:
    def twosum(self,nums : list[int],target : list[int])-> list[int]:
        seen={}
        for i in range(len(nums)):
            current_num=nums[i]
            diff=target-current_num

        if diff in seen:
            return [seen[diff],i]
        seen[current_num]=i
        
        return[]
    

