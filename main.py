import numpy as np

def calculate(list):
# Validate length
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
# Convert the list into a 3 x 3 Numpy array
    arr = np.array(list).reshape(3, 3)
    
# The dictionary 
    stats_fns = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    
# Compute all stats
    calculations  = {}
    for name, fn in stats_fns.items():
        cols = fn(arr, axis=0).tolist()  
        rows = fn(arr, axis=1).tolist()   
        flat = fn(arr).tolist()           
        
        calculations [name] = [cols, rows, flat]
    
    return calculations 