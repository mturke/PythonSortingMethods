import timeit

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


list = []
MergeStringList.add("5")
MergeStringList.add("3")
MergeStringList.add("2")
MergeStringList.add("1")
MergeStringList.add("4")
MergeStringList.add("7")
MergeStringList.add("6")

print(" ")
print("Unsorted list:")
print(list)
print(" ")

MergeStringList.mergeSort(list)
print(" ")
print("Sorted list: ")

for i in range(len(list)):
    print("%s" %list[i], end=" ")
print(" ")

print(" ")
time1 = timeit.timeit((MergeStringList), number = 1000)
print(" ")
print("Run time:", time1)
