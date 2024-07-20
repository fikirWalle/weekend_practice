

def distnictArray(arrays:list[int]):
    uniqueValues={ abs(val)for val in arrays}

    if len(uniqueValues)<len(arrays):
        return False
    return True

print(distnictArray([1,2,3,4]))