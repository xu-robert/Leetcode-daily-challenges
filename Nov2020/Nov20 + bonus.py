# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 08:21:12 2020
2 problems: Search in rotated sorted array and search in rotated sorted array II. First is without duplicates.

#1:
The central idea is that if the array has been rotated and we dont need to worry about duplicates, when we split the
array at a midpoint, at least one of the halves will be sorted. Unless the different between right and left is less than 2,
in which case you could have a configuration like [9, 0]. For both halves, first we check if it the half is sorted by
comparing the midpoint with the endpoint. If the half is sorted and our target is within the lower and upper bounds
of the half, then we know that if the target exists, it will be in that half, so we narrow down our search space.
If the half is sorted but the target is outside the boundaries of the half, we carry on the search in the other half.

A few key things though: Even though both halves are potentially sorted, we only check the one that possibly contains
target. If both halves are sorted, only one could possibly contain target, since there are no duplicates. Secondly:
why can we keep carrying on the search in the other half using the same algorithm?
Well there are essentially only two ways we can proceed in the while loop: either we search in a sorted array or an
unsorted array. If the array is sorted, the algorithm essentially carries out normal binary search. If not, we just
keep reducing that array either until we reach a sorted array or until the array size is less than or equal to 2.

So the special case where the array size is 2: this means that the rotation happened within the array, so we just
check the boundaries.

#2:
Essentially the same question, but the worst case complexity is O(n) because duplicates may be present. In this case
we just skip over duplicates from the left and right side.

@author: Robert Xu
"""
class Solution1(object):
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        
        while right - left > 1:
            
            mid = (left+right)//2
                        
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                
                else:
                    left = mid+1
            
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                
                else:
                    right=mid-1
            
        if nums[left] == target: return left
        elif nums[right] == target: return right
        return False

class Solution2(object):
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        
        if nums == []: return False
        
        while right - left > 1:
            
            
            while left < right and nums[left] == nums[left+1]:
                left += 1
            
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            
            mid = (left+right)//2
            
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                
                else:
                    left = mid+1
            
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                
                else:
                    right=mid-1
            
        return (nums[left] == target) or (nums[right] == target)
    
a = Solution2()
b = a.search2([1,2,0,0,1],3)