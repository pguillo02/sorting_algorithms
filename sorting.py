def insertion(l: list[int]):
    pass


def bubble(l: list[int]):
    """
    Implementation of the bubble sort algorithm. The idea is for the function to modify the recieving list in-place by swapping pairs of elements.

    Recives: 
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