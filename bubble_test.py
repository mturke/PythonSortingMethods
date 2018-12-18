import timeit

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


list = []
BubbleStringList.add("2")
BubbleStringList.add("6")
BubbleStringList.add("3")
BubbleStringList.add("7")
BubbleStringList.add("4")
BubbleStringList.add("1")
BubbleStringList.add("5")

print(" ")
print("Unsorted list:")
print(list)
print(" ")

BubbleStringList.bubbleSort(list)
print("Sorted list: ")

for i in range(len(list)):
    print(list[i], end=" ")
    
print(" ")
time1 = timeit.timeit((BubbleStringList), number = 1000)
print(" ")
print("Run time:", time1)


