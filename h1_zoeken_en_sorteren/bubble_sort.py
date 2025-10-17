def bubble_sort(a):
    for i in range(0,len(a)-1):
        for j in range (len(a)-1,i+2):
            if a[j-1]>a[j]:
                a[j-1] = a[j]

a = [int(_) for _ in input().split()]
bubble_sort(a)

