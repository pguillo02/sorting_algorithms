def insertion(l: list[int]):

    for i in range(1, len(l)):
        
        j: int = 0


def bubble(l: list[int]):
    
    while True:

        swapped: bool = False

        for i in range(1, len(l)):

            if l[i] < l[i-1]:
                
                l[i], l[i-1] = l[i-1], l[i]
                swapped = True
            
        if not swapped: 
            break   
    
    return l