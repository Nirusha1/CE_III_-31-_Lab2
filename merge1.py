def merge_sort(arrays):
    n=len(arrays)
    if n==1:
        return 1
    mid_value=n // 2
    Left_half=arrays[:mid_value]
    Right_half=arrays[mid_value:]
    
    merge_sort(Left_half)
    merge_sort(Right_half)

    i=0
    j=0
    k=0
    while i < len(Left_half) and j < len(Right_half):
        if Left_half[i] < Right_half[j]:
            arrays[k]=Left_half[i]
            i=i+1
        else:
            arrays[k]=Right_half[j]
            j=j+1
        k=k+1

    while i < len(Left_half):
        arrays[k]=Left_half[i]
        i=i+1
        k=k+1

    while j < len(Right_half):
        arrays[k]=Right_half[j]
        j=j+1
        k=k+1

if __name__=='__main__':
    arrays = [54,26,93,17,77,31,44,55,20]
    merge_sort(arrays)
    print(arrays)



