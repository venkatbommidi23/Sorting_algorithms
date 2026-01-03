#https://www.geeksforgeeks.org/problems/merge-sort/1

class Solution:
 
    def mergeSort(self,arr, l, r):
        # Base case: If the array has one or zero elements, it's already sorted
        if(l>=r):
            return
        # Find the midpoint to divide the array
        mid=(l+r)//2
        
        # Recursively sort the left half
        self.mergeSort(arr,l,mid)
        
        # Recursively sort the right half
        self.mergeSort(arr,mid+1,r)
        
        # Recursively sort the right half
        self.merge(arr,l,mid,r)
        
    def merge(self,arr,low,mid,high):
        temp=[]    # Temporary list to store merged elements
        left=low
        right=mid+1
        
        # Compare elements of both halves and pick the smaller one
        while(left<=mid and right<=high):
            if(arr[left]<=arr[right]):
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        # Copy remaining elements from the left half (if any 
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        
        # Copy remaining elements from the right half (if any)
        while(right<=high):
            temp.append(arr[right])
            right+=1
        # Copy the sorted elements back into the original array
        for i in range(len(temp)):
            arr[low+i]=temp[i]
            
        #Time Complexity-O(nlogn), dividing -O(logn)  merge at each level O(n)
        #Space-O(n)(overall)  ,Temp store elements -O(n),recursion depth-O(logn)
        
        
        

