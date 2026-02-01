#https://www.geeksforgeeks.org/problems/insertion-sort/1

#Insertion sort ante enti ante left part already sorted ani assume chesko 1st element ki Tarvatha left part elano sorted gane untadi
#ipudu next element ni pick chesko,deni position ekkado insert cheyalo select chey daniki loops and conditions raayi

# i loop second element nunchi start chesko enduku ante already 1st di sorted ani assume chesko
# key emo current element "ith" index tisko,e element ni manam correct position lo pick petali
# "j" emo "i" kanna mundu index nunchi start chey, loop until j >=0 and arr[j] > key:  mundu unna elements key kanna pedadhi ayithe avvi okay index right is shift cheyali 
#j ni decrease cheyali.

# last ki ekada ayithe e condition fail avutado akada "key" ni insert cheyali




👉 Left part is already sorted
👉 Insert current element into correct place

class Solution:
    def insertionSort(self, arr,n=None):
        
        #Recursive Insertion Sort
        
        # if n is None:
        #     n=len(arr)
        # if n<=1:
        #     return
        # self.insertionSort(arr,n-1)
        
        # key=arr[n-1]
        # j=n-2
        # while(j>=0 and arr[j]>key):
        #     arr[j+1]=arr[j]
        #     j-=1
        # arr[j+1]=key
        
        
        #NORMAL INSERTION SORT
        
        for i in range(1, len(arr)):      # start from the 2nd element (index 1)
            key = arr[i]                  # current element to be inserted
            j = i - 1                     # start comparing with the previous elements
            
            while j >= 0 and arr[j] > key:  # shift elements greater than key to the right
                arr[j + 1] = arr[j]
                j = j - 1                  # move one step left
                
            arr[j + 1] = key              # place key in the correct sorted position

