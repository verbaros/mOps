def union (*args, sort=True):    
    if all([hasattr(a, '__iter__') for a in args]):
        result = []
        [result.extend(s) for s in args]
        if (sort):
            result.sort()
        return result        
    else:
        raise TypeError('Set must be iterable')
        
U=union

def intersection(*args):
    if all([hasattr(a, '__iter__') for a in args]):
        result = list(set.intersection(*map(set,args)))  
        result.sort()
        return result
    else:
        raise TypeError('Set must be iterable')

I = intersection