import timeit

class QuickStringList():
    def add(str):
        list.append(str)
        
    def quickSort(list):
        length = len(list)
        QuickStringList.quickSortHelper(list,0,len(list)-1)
    
    def quickSortHelper(list, first, last):
        if first<last:
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

list = []
QuickStringList.add("3")
QuickStringList.add("5")
QuickStringList.add("2")
QuickStringList.add("7")
QuickStringList.add("4")
QuickStringList.add("6")
QuickStringList.add("1")
print(" ")
print("Unsorted list:")
print(list)

QuickStringList.quickSort(list)

print(" ")    
print("Sorted list:")
for i in range(len(list)):
    print("%s" %list[i],end=" ")

print(" ")
time1 = timeit.timeit((QuickStringList), number = 1000)
print(" ")
print("Run time:", time1)
