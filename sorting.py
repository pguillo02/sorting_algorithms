import math

def insertion(l: list[int]):
    """
    Implementation of the insertion sort algorithm.

    Recieves:
        l[int]: int = list of integers to be sorted.

    Returns: 
        l: list[int] = the same list that it recieved sorted.
    """
    
    for i in range(1, len(l)):
        key: int = l[i]
        j: int = i - 1

        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1

        l[j+1] = key

    return l

def bubble(l: list[int]):
    """
    Implementation of the bubble sort algorithm. The idea is for the function to modify the recieving list in-place by swapping pairs of elements.

    Recieves: 
        l: list[int] = list of integers to be sorted.

    Returns: 
        l: list[int] = the same list that it recieved sorted.
    """

    while True:

        swapped: bool = False

        for i in range(1, len(l)):

            if l[i] < l[i-1]:               
                l[i], l[i-1] = l[i-1], l[i]
                swapped = True
            
        if not swapped: 
            break   
    
    return l

def selection(l: list[int]):
    """
    Implementation of the selection sort algorithm.

    Recieves:
        l[int]: int = list of integers to be sorted.

    Returns: 
        l: list[int] = the same list that it recieved sorted.
    """
    
    for i in range(len(l)-1, 0, -1):
        max_index: int = i
        
        for j in range(i+1):
            if l[j] > l[max_index]:
                max_index = j

        l[max_index], l[i] = l[i], l[max_index]

    return l 

def merge(l: list[int]):
    pass

def heap(l: list[int]):
    pass
