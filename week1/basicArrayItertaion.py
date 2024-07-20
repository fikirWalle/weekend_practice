#def printArray(array: list[int]) -> None:
#def printEveryOtherValue(array: list[int]) -> None:
#def printEveryOtherValueSkipFirst(array: list[int]) -> None:
#def printEveryKth(array: list[int], k: int) -> None:
#def printReverse(array: list[int]) -> None:
#def printReverseEveryOtherValue(array: list[int]) -> None:
#def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
#def printReverseEveryKth(array: list[int], k: int) -> None:#


def printArray(array: list[int]) :
    i=0
    while i< len(array):
        print(array[i],end=",")
        i+=1

print(printArray([1,2,3,4,5,6,7,8,9]))

def printEveryOtherValue(array: list[int]):
    i=0
    while(i<len(array)):
        print(array[i],end=",")
        i+=2
print(printEveryOtherValue([1,2,3,4,5,6,7,8,9]))    

def printEveryOtherValueSkipFirst(array: list[int]) :

    i=1
    while(i<len(array)):
        print(array[i],end=",")
        i+=2
print(printEveryOtherValueSkipFirst([1,2,3,4,5,6,7,8,9]))            
def printEveryKth(array: list[int], k: int):
    i=0;
    while i<len(array):
        print(array[i],end=",")
        i+=k
print(printEveryKth([1,2,3,4,5,6,7,8,9],3))            
       
def printReverse(array: list[int]):

    i=len(array)-1
    while i>=0:
        print(array[i],end=',')
        i-=1
def printReverseEveryOtherValue(array: list[int]):
    i=len(array)-1
    while(i>=0):
        print(array[i],end=',')
        i-=2    

def printReverseEveryOtherValueSkipLast(array: list[int]):
    i=len(array)-2
    while(i>=0):
        print(array[i],end=",")
        i-=2        

def printReverseEveryKth(array: list[int], k: int):
    i=len(array)-1
    while(i>=0):
        print(array[i],end=',')
        i-=k

