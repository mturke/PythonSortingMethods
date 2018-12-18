class BubbleStringList():
    def add(str):
        list.append(str)

    def bubbleSort(list):
        lst = len(list)

        for i in range(len(list)-1,0,-1):
            for j in range(i):
                if list[j] > list[j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp


class MergeStringList():

    def add(str):
        list.append(str)

    def mergeSort(list):
        print("Splitting ", list)
        
        if len(list) > 1:
            mid = len(list) //2
            lefthalf = list[:mid]
            righthalf = list[mid:]

            MergeStringList.mergeSort(lefthalf)
            MergeStringList.mergeSort(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    list[k] = lefthalf[i]
                    i += 1
                else:
                    list[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                list[k]=lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                list[k] = righthalf[j]
                j += 1
                k += 1
                
        print("Merging ", list)


class QuickStringList():

    def add(str):
        list.append(str)
        
    def quickSort(list):
        length = len(list)
        QuickStringList.quickSortHelper(list,0,len(list)-1)
    
    def quickSortHelper(list,first,last):
        if first < last:
            splitpoint = QuickStringList.partition(list, first, last)

            QuickStringList.quickSortHelper(list, first, splitpoint-1)
            QuickStringList.quickSortHelper(list, splitpoint+1, last)


    def partition(list, first, last):
       pivotvalue = list[first]

       leftmark = first + 1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and list[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while list[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = list[leftmark]
               list[leftmark] = list[rightmark]
               list[rightmark] = temp

       temp = list[first]
       list[first] = list[rightmark]
       list[rightmark] = temp

       return rightmark

    

