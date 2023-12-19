def follow_pipe(arr, ind, dir):
    if arr[ind] in ["|", "-"]:
        return dir
        
    elif arr[ind] == "L":
        if dir == (1,0):
            return (0,1)
        elif dir == (0,-1):
            return (-1,0)
        
    elif arr[ind] == "J":
        if dir == (1,0):
            return (0,-1)
        elif dir == (0,1):
            return (-1,0)
    
    elif arr[ind] == "7":
        if dir == (-1,0):
            return (0,-1)
        elif dir == (0,1):
            return (1,0)
    
    elif arr[ind] == "F":
        if dir == (-1,0):
            return (0,1)
        elif dir == (0,-1):
            return (1,0)
    
    elif arr[ind] == ".":
        return [0,0]

def within_bounds(arr, ind):
    if ind[0] >= 0 and ind[0] < arr.shape[0] and ind[1] >= 0 and ind[1] < arr.shape[1]:
        return True 
    return False