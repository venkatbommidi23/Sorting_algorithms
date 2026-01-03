#https://www.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)-1):
            min=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min]:
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
        return arr
        
# Time (Best)    O(n²)
# Time (Average)    O(n²)
# Time (Worst)    O(n²)
# Space    O(1)
