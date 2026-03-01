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
