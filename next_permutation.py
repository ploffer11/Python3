def next_permutation(List):
    length = len(List)
    left = -1

    for i in range(0, length-1):
        if List[i] < List[i+1]:
            left = i

    if left < 0:
        List[:] = List[::-1]
        return False  

    right = length - 1

    while List[left] >= List[right]:
        right -= 1
    
    List[left], List[right] = List[right], List[left]
    List[left + 1 :] = List[left + 1:][::-1]
    return True


a = [1,2,3,4]

while 1:
    print(a)
    if not next_permutation(a):
        break 







