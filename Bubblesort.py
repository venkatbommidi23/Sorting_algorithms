#https://www.geeksforgeeks.org/problems/bubble-sort/1
# 👉 Compare adjacent elements and swap if wrong
# 👉 Biggest element moves to the end in each pass

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr,last=None):
        if last is None:
            last=len(arr)-1
        if last==0:   #Base Case when last is 0, it means the array is fully sorted
            return  
        
        n=len(arr)
        if n==1: #Edge Case if Array has one element
            return
        swapped=False
        for j in range(last):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            return
        self.bubbleSort(arr,last-1)
        
        
        
        #Iterative Method
        
        # for i in range(len(arr)):
        #     swapped=False
        #     for j in range(len(arr)-i-1):
        #         if arr[j+1]<arr[j]:
        #             arr[j],arr[j+1]=arr[j+1],arr[j]
        #             swapped=True
        #     if not swapped:
        #         break
        # return arr
        
        # Time Complexity
        
        # Best Case-O(n) - Array when Sorted
        # Worst Case -O(n*2) 
        
        #Space Complexity- O(1)
        
        
        
        
