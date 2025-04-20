def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


def buble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j=i-1
        while j>=0:
            if arr[j] < current:
                break
            else:
                arr[j+1] = arr[j]
                arr[j] = current
                j = j-1
    return arr
def merge(l1,s,m,e):
    temp = list()
    i = s
    j = m+1
    while i<= m and j<=e:
        if l1[i]<l1[j]:
            temp.append(l1[i])
            i+=1
        elif l1[i]>l1[j]:
            temp.append(l1[j])
            j+=1
        elif l1[i]==l1[j]:
            temp.append(l1[i])
            temp.append(l1[j])
            i+=1
            j+=1
    while i<=m:
        temp.append(l1[i])
        i+=1
    while j<=e:
        temp.append(l1[j])
        j+=1
    
    startoftemp = 0
    startofl1 = s
    while startofl1<=e:
        l1[startofl1] = temp[startoftemp]
        startofl1+=1
        startoftemp+=1
    return
            
            
def merge_sort_helper(l1,s,e):
    if s>=e:
        return
    m = s+(e-s)//2
    merge_sort_helper(l1,s,m)
    merge_sort_helper(l1,m+1,e)
    
    merge(l1,s,m,e)
    return

def merge_sort(l1):
    return merge_sort_helper(l1,0,len(l1)-1)
# l1 = [1,10,3,6,9,15]
# merge_sort(l1)
# print(l1)
# unsorted_list = [12,25,11,34,90,22]
# sorted_list = insertion_sort(unsorted_list)
# print("Sortred Elements: ",sorted_list)


######################################################
## Quick Sort

def partition(l1,s,e):
    # PI = e
    # i,j = s,e
    # while i<j:
    #     if l1[i]>l1[PI]:
    #         l1[i],l1[PI] = l1[PI],l1[i]
    #         PI=i
    #         i+=1
    #     elif l1[i]<l1[PI]:
    #         i+=1
    #     elif l1[i]==l1[PI]:
    #         i+=1
    
    pivot = l1[e]
    i = s
    rightPosition = s
    
    while(i<=e-1):
        if l1[i]<pivot:
            rightPosition+=1
        i+=1
    l1[rightPosition],l1[e] = l1[e],l1[rightPosition]
        
    pivotIndex =  rightPosition
    
    start = s
    end = e
    
    while start<pivotIndex and end>pivotIndex:
        if l1[start]<pivot:
            start+=1
        elif l1[end]>=pivot:
            end-=1
        else:
            l1[start],l1[end] = l1[end],l1[start]
            start+=1
            end-=1
    return pivotIndex
        

def quick_sort(l1,s,e):
    if s>=e:
        return
    
    PI = partition(l1,s,e)
    
    quick_sort(l1,s,PI-1)
    quick_sort(l1,PI+1,e)
    
    return
l1 = [1,10,3,6,9,15]
quick_sort(l1,0,len(l1)-1)
print(l1)