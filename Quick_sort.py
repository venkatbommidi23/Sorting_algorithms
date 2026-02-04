#Core Idea of Quick Sort
# Pick a pivot element
# Place pivot at its correct position
# All smaller elements → left side
# All larger elements → right side
# Repeat recursively for left and right parts

#Quick Sort picks a pivot, places it in correct position,
#partitions array into smaller and larger elements, and recursively sorts both parts

class Solution:
    def quickSort(self,arr,low,high):
        # If low < high, it means array has more than one element
        if(low<high):  # or We can right (low<=high) return and write code in next lines both works.
            
            # Partition the array and get pivot index
            # After partition:
            # pivot is in its correct sorted position
            
            p_index=self.partition(arr,low,high)
            
            # Recursively sort elements on left of pivot
            self.quickSort(arr,low,p_index-1)
            
            # Recursively sort elements on right of pivot
            self.quickSort(arr,p_index+1,high)
    
    # Partition function (Lomuto partition scheme)
    
    # We will choose last element as pivot and start from low element initial there is no low so take i=low-1
   
    #check the elements that are less than pivot and if less than pivot increment i and swap with the current index element that is less
    
    # and at last swap the pivot with next index of the element that is smaller.

    #enduku ante manam pivot return cheyali pivot kanna left lo unna values anni less than pivot untai and right side anni greater 
    
    #we need to return i+1 as pivot,because ith index lo pivot kanna takkuva unna last index value untadi.
  
    
    
    def partition(self,array,low,high):
        # Step 1: Choose pivot
        # Here we choose the last element as pivot
        
        pivot = array[high]
        
        # Step 2: i keeps track of the last index of smaller elements
        # Initially no smaller elements, so i = low - 1
        i=low-1
        
        # Step 3: Traverse elements from low to high-1
        for j in range(low,high):
            
            # If current element is <= pivot
            if array[j]<=pivot:
                # Move i forward
                i=i+1
                # Swap smaller element to the left side
                (array[i],array[j])=(array[j],array[i])
            
        # Step 4: Place pivot at its correct position
        # i+1 is the correct index for pivot

        (array[i + 1], array[high]) = (array[high], array[i + 1])
        
        # Return pivot index
        return i + 1
        
        #Time Complexity-O(nlogn)
        #In Quick Sort, work per level is O(n)(j loop) and number of levels is logn
        #( auxillary space due to recursion)
        #so total time is O(n log n).
        
        #Space-O(logn)--best/average case
        # O(n)--worst case
